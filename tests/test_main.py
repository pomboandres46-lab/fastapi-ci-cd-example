from fastapi.testclient import TestClient
import sys

sys.path.insert(0, ".")
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_read_2_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}


def test_read_3_root():
    response = client.get("/stats")
    assert response.status_code == 200
    assert response.json() == {"message": "Aqui veras las estadisticas"}


def test_read_4_root():
    response = client.get("/graf")
    assert response.status_code == 200
    assert response.json() == {"message": "Aqui veras las graficas"}
