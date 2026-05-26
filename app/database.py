import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        host=os.getenv("ORACLE_HOST"),
        port=int(os.getenv("ORACLE_PORT")),
        service_name=os.getenv("ORACLE_SERVICE")
    )
    return conn

def test_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 'Oracle 26ai Connected!' FROM DUAL")
        result = cursor.fetchone()
        print(result[0])
        conn.close()
        return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_connection()
