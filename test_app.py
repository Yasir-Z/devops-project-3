import pytest
from app import calculate_priority, app


# UNIT TEST: Tests the logic in isolation
def test_calculate_priority():
    assert calculate_priority(10) == "High"
    assert calculate_priority(2) == "Low"


# INTEGRATION TEST: Tests the API response and logic together
def test_api_status():
    with app.test_client() as client:
        response = client.get("/status")
        data = response.get_json()

        assert response.status_code == 200
        assert data["status"] == "Active"
        assert data["priority"] == "Low"
