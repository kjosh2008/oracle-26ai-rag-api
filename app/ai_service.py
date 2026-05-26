import os
import oracledb
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.2")
OLLAMA_HOST = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Create Ollama client with explicit host
client = Client(host=OLLAMA_HOST)

def get_connection():
    return oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        host=os.getenv("ORACLE_HOST"),
        port=int(os.getenv("ORACLE_PORT")),
        service_name=os.getenv("ORACLE_SERVICE")
    )

def embed_text(text: str) -> list[float]:
    response = client.embeddings(model=EMBED_MODEL, prompt=text)
    return response["embedding"]

def store_document(title: str, content: str, doc_type: str = "general"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO documents (title, content, doc_type)
        VALUES (:1, :2, :3)
        RETURNING doc_id INTO :4
    """, [title, content, doc_type, cursor.var(oracledb.NUMBER)])
    doc_id = cursor.bindvars[3].getvalue()[0]
    chunks = [content[i:i+500] for i in range(0, len(content), 500)]
    for chunk in chunks:
        embedding = embed_text(chunk)
        vector_str = "[" + ",".join(str(x) for x in embedding) + "]"
        cursor.execute("""
            INSERT INTO embeddings (doc_id, chunk_text, embedding)
            VALUES (:1, :2, TO_VECTOR(:3))
        """, [doc_id, chunk, vector_str])
    conn.commit()
    conn.close()
    print(f"Stored doc_id={doc_id} with {len(chunks)} chunks")
    return doc_id

def semantic_search(query: str, top_k: int = 5) -> list[dict]:
    embedding = embed_text(query)
    vector_str = "[" + ",".join(str(x) for x in embedding) + "]"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.chunk_text, d.title,
               VECTOR_DISTANCE(e.embedding, TO_VECTOR(:1), COSINE) AS score
        FROM   embeddings e
        JOIN   documents d ON e.doc_id = d.doc_id
        ORDER  BY score ASC
        FETCH  FIRST :2 ROWS ONLY
    """, [vector_str, top_k])
    results = []
    for row in cursor.fetchall():
        results.append({
            "chunk": row[0].read() if hasattr(row[0], 'read') else row[0],
            "title": row[1],
            "score": float(row[2])
        })
    conn.close()
    return results

def rag_chat(question: str) -> dict:
    context_docs = semantic_search(question, top_k=3)
    if context_docs:
        context = "\n\n".join([
            f"[{d['title']}]: {d['chunk']}" for d in context_docs
        ])
        prompt = f"""Use this context to answer the question:

Context:
{context}

Question: {question}

Answer:"""
    else:
        prompt = question
    
    response = client.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}])
    return {
        "answer": response["message"]["content"],
        "sources": [d["title"] for d in context_docs],
        "context_used": len(context_docs) > 0
    }

if __name__ == "__main__":
    print("Testing embed...")
    emb = embed_text("Hello Oracle 26ai!")
    print(f"Embedding dim: {len(emb)} ✅")
    print("\nTesting RAG chat with Ollama...")
    result = rag_chat("What is this application about?")
    print(f"Answer: {result['answer']}")
    print(f"Sources: {result['sources']}")
