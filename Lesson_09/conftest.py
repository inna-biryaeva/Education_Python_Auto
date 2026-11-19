import pytest
from db_client import Subject_db_client

@pytest.fixture(scope="session")
def db_client():
    connection_string = "postgresql+psycopg2://postgres:1103@localhost:5432/QA"
    return Subject_db_client(connection_string)
