import responses

base_URL = "https://api.yougile.com/api-v2"

@responses.activate
def test_create_project_positive(api_client):
    responses.add(
        responses.POST,
        base_URL + "/projects",
        json={"id": "proj_12345", "name": "Test Project", "team_id": "team_123"},
        status=201
    )
    payload = {"name": "Test Project", "team_id": "team_123"}
    response = api_client.create_project(payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Test Project"

@responses.activate
def test_create_project_negative(api_client):
    responses.add(
        responses.POST,
        base_URL + "/projects",
        json={"error": "Field 'name' is required"},
        status=400
    )
    payload = {"team_id": "team_123"}
    response = api_client.create_project(payload)
    assert response.status_code == 400
    assert "error" in response.json()

@responses.activate
def test_get_project_positive(api_client):
    project_id = "proj_12345"
    responses.add(
        responses.GET,
        base_URL + "/projects/" + project_id,
        json={"id": project_id, "name": "New Project"},
        status=200
    )
    response = api_client.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["id"] == project_id

@responses.activate
def test_get_project_negative(api_client):
    fake_id = "invalid_id_00000"
    responses.add(
        responses.GET,
        base_URL + "/projects/" + fake_id,
        json={"error": "Project not found"},
        status=404
    )
    response = api_client.get_project(fake_id)
    assert response.status_code == 404

@responses.activate
def test_update_project_positive(api_client):
    project_id = "proj_12345"
    responses.add(
        responses.PUT,
        base_URL + "/projects/" + project_id,
        json={"id": project_id, "name": "Updated Project Name"},
        status=200
    )
    payload = {"name": "Updated Project Name"}
    response = api_client.update_project(project_id, payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Project Name"

@responses.activate
def test_update_project_negative(api_client):
    fake_id = "invalid_id_00000"
    responses.add(
        responses.PUT,
        base_URL + "/projects/" + fake_id,
        json={"error": "Project not found"},
        status=404
    )
    payload = {"name": "Should Not Work"}
    response = api_client.update_project(fake_id, payload)
    assert response.status_code == 404
