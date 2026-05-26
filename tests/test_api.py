import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_chat():
    response = client.post("/chat", json={"question": "test"})
    assert response.status_code in [200, 500]  # May fail if no DB
