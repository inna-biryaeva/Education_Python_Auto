import requests

class APIclient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

    def create_project(self, payload: dict):
        url = self.base_url + "/projects"
        return requests.post(url, json=payload, headers=self.headers)

    def get_project(self, project_id: str):
        url = self.base_url + "/projects/" + project_id
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id: str, payload: dict):
        url = self.base_url + "/projects/" + project_id
        return requests.put(url, json=payload, headers=self.headers)
