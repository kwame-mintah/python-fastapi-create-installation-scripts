class DashboardService:
    stub_data = {
        "assignedProjects": 2,
        "securityHotspots": {
            "critical": 1,
            "high": 1,
            "medium": 0,
            "low": 1,
        },
        "updates": {
            "changes": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
            "ut labore et dolore magna aliqua."
        },
    }

    def return_stub_data(self):
        return self.stub_data
