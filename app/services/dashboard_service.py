class DashboardService:
    stub_data = {
        "assignedProjects": 2,
        "securityHotspots": {
            "critical": 1,
            "medium": 0,
            "low": 1,
        },
    }

    def return_stub_data(self):
        return self.stub_data
