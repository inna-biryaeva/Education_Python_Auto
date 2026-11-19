def test_create_project_positive(api_client):
    payload = {"title": "NewProject_POST_Test"}
    response = api_client.create_project(payload)
    assert response.status_code in [200, 201]
    assert "id" in response.json()

def test_create_project_negative(api_client):
    payload = {}
    response = api_client.create_project(payload)
    assert response.status_code in [400, 422]

def test_get_project_positive(api_client, test_project_id):
    response = api_client.get_project(test_project_id)
    assert response.status_code == 200
    assert response.json()["id"] == test_project_id

def test_get_project_negative(api_client):
    fake_id = "000000000000000000000000"
    response = api_client.get_project(fake_id)
    assert response.status_code == 404

def test_update_project_positive(api_client, test_project_id):
    payload = {"title": "UpdatedProject_PUT_Test"}
    response = api_client.update_project(test_project_id, payload)
    assert response.status_code == 200
    assert response.json()["id"] == test_project_id

def test_update_project_negative(api_client):
    fake_id = "000000000000000000000000"
    payload = {"title": "NoWorking"}
    response = api_client.update_project(fake_id, payload)
    assert response.status_code == 404
