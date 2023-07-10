# UoW Backend App

This project provides a way to download installation scripts for your projects. This will create a shell script (`.sh`) or a configuration file (`.config`) to be run on your machine.
This application provides a simplified and abstracted RESTful API that can be easily consumed by the [UoW Frontend App](https://dev.azure.com/k-space/uow/_git/uow-frontend-app).

## Getting Started

### Project structure

```markdown
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   └── routers          # "routers" is a "Python subpackage"
│      ├── __init__.py  # makes "routers" a "Python subpackage"
│      └── dashboard.py     # "dashboard" submodule, e.g. import app.routers.dashboard
│      └── notifications.py     # "notifications" submodule, e.g. import app.routers.notifications
│      └── projects.py     # "projects" submodule, e.g. import app.routers.projects
│      └── setting.py     # "setting" submodule, e.g. import app.routers.setting
│      └── user.py     # "user" submodule, e.g. import app.routers.user
```

### Usage

1. Install python packages used for the service
    ```console
   pip install - requirements.txt
    ```
2. Run the FastAPI server, which will run on port 8000
    ```console
   python app/main.py
    ```
   Endpoint documentation are available on http://127.0.0.1:8000/docs

### Tests

Unit tests are located in `/tests` directory.
