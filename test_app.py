import pytest
import json
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Chat Assistant!" in response.data

def test_show_employees_in_department(client):
    response = client.post('/chat', json={"query": "Show me all employees in the Sales department."})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "response" in data

def test_highest_paid_employee(client):
    response = client.post('/chat', json={"query": "Show the highest-paid employee."})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "highest-paid" in data["response"]
