import os
import pytest
from dotenv import load_dotenv
from api_client import APIclient

load_dotenv()

@pytest.fixture(scope="session")
def api_client():
    base_url = "https://api.yougile.com/api-v2"
    api_token = os.getenv("API_TOKEN")
    team_id = os.getenv("TEAM_ID")
    if not api_token or not team_id:
        raise ValueError(
            "Не найдены переменные API_TOKEN или TEAM_ID. "
            "Создайте файл .env на основе .env.example и заполните его."
        )
    client = APIclient(base_url, api_token)
    client.team_id = team_id
    return client

@pytest.fixture(scope="session")
def test_project_id(api_client):
    project_name = "TestProject_AutoTest"

    payload = {
        "title": project_name
    }
    response = api_client.create_project(payload)
    assert response.status_code in [200, 201]
    project_data = response.json()
    project_id = project_data.get("id")
    assert project_id is not None
    return project_id
