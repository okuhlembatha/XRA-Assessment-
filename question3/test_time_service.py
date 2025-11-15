import pytest
import json
from datetime import datetime
from time_service import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_time_endpoint_exists(client):
    """Test that the /time endpoint exists and returns 200."""
    response = client.get('/time')
    assert response.status_code == 200


def test_time_endpoint_returns_json(client):
    """Test that the /time endpoint returns JSON."""
    response = client.get('/time')
    assert response.content_type == 'application/json'


def test_time_endpoint_structure(client):
    """Test that the response has the correct structure."""
    response = client.get('/time')
    data = json.loads(response.data)
    
    assert 'current_date' in data
    assert 'current_time' in data


def test_time_endpoint_date_format(client):
    """Test that the date is in the correct format (YYYY-MM-DD)."""
    response = client.get('/time')
    data = json.loads(response.data)
    
    # Validate date format
    try:
        datetime.strptime(data['current_date'], '%Y-%m-%d')
        assert True
    except ValueError:
        assert False, f"Date format is incorrect: {data['current_date']}"


def test_time_endpoint_time_format(client):
    """Test that the time is in the correct format (HH:MM:SS)."""
    response = client.get('/time')
    data = json.loads(response.data)
    
    # Validate time format
    try:
        datetime.strptime(data['current_time'], '%H:%M:%S')
        assert True
    except ValueError:
        assert False, f"Time format is incorrect: {data['current_time']}"


def test_time_endpoint_returns_current_date(client):
    """Test that the endpoint returns approximately the current date."""
    response = client.get('/time')
    data = json.loads(response.data)
    
    current_date = datetime.now().strftime('%Y-%m-%d')
    assert data['current_date'] == current_date