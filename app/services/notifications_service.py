class NotificationService:
    stub_data = {
        "notifications": [
            {"notificationId": 1, "message": "Just smile"},
            {"notificationId": 2, "message": "And wave"},
        ]
    }

    def return_stub_data(self):
        return self.stub_data
