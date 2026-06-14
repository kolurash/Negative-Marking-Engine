import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_valid_score():
    response = client.post(
        "/calculate-score",
        json={"correct": 8, "wrong": 2}
    )

    assert response.status_code == 200
    assert response.json() == {"final_score": 7.5}


def test_negative_values():
    response = client.post(
        "/calculate-score",
        json={"correct": -1, "wrong": 2}
    )

    assert response.status_code == 400


def test_missing_field():
    response = client.post(
        "/calculate-score",
        json={"correct": 5}
    )

    assert response.status_code == 422

def test_zero_values():
    response = client.post(
        "/calculate-score",
        json={"correct": 0, "wrong": 0}
    )

    assert response.status_code == 200
    assert response.json() == {"final_score": 0.0}