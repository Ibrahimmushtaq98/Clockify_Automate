import requests

class ClockifyClient:
    API_BASE_URL= "https://api.clockify.me/api/v1"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "content-type": "application/json",
            "X-Api-Key": self.api_key
        }
        
    def get_user_data(self):
        url = f"{self.API_BASE_URL}/user"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_workspaces_data(self):
        url = f"{self.API_BASE_URL}/workspaces"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_project_data(self, workspace_id, filter_workspace=None):
        url = f"{self.API_BASE_URL}/workspaces/{workspace_id}/projects"
        params = {}
        if(filter_workspace != None):
            params = {
                'name': filter_workspace,
            }

        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    def add_time_entry(self, workspace_id, data):
        url = f"{self.API_BASE_URL}/workspaces/{workspace_id}/time-entries"
        response = requests.post(url, json=data, headers=self.headers)
        return response