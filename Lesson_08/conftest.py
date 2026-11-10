import pytest
from api_client import API_client

@pytest.fixture(scope="function")
def api_client():
    base_URL = "https://api.yougile.com/api-v2"
    temp_Token = "fake_token_for_mocking"

    return API_client(base_URL, temp_Token)
