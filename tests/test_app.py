import re
import pytest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_time_endpoint_format(client):
    """Test that /time returns a timestamp in the expected format.
    Expected format: YYYY/MM/DD HH:MM:SS +HH:MM
    """
    response = client.get('/time')
    assert response.status_code == 200, "Expected status code 200"
    json_data = response.get_json()
    assert 'timestamp' in json_data, "Response JSON should contain 'timestamp' key"
    timestamp = json_data['timestamp']
    # Regex to match the required format
    pattern = r"^\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2} [+-]\d{2}:\d{2}$"
    assert re.match(pattern, timestamp), f"Timestamp '{timestamp}' does not match expected format"
