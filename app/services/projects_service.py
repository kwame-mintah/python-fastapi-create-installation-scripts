from fastapi import HTTPException


class ProjectsService:
    stub_data = {
        "projects": [
            {"projectId": "bxsHg", "projectName": "Cartoon Network"},
            {"projectId": "fPvAb", "projectName": "Jetix"},
        ]
    }

    stub_data_details = {
        "projectId": "bxsHg",
        "projectName": "Cartoon Network",
        "details": {
            "softwarePackages": [
                {"name": "Java", "version": "openjdk-13"},
                {"name": "Node", "version": "18.16.1"},
                {"name": "Python", "version": "3.9"},
            ]
        },
    }

    def return_stub_data(self):
        return self.stub_data

    def return_stub_data_id(self, identifier: str):
        if identifier != self.stub_data_details["projectId"]:
            raise HTTPException(status_code=404, detail="Project not found")
        return self.stub_data_details
