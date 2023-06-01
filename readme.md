# UoW Backend App

This service provides a... And provides a simplified and abstracted RESTful API that can be easily consumed by the
[UoW Frontend App]().

## Getting Started

### Project structure

```markdown
.
├── app                  # "app" is a Python package
│   ├── __init__.py      # this file makes "app" a "Python package"
│   ├── main.py          # "main" module, e.g. import app.main
│   └── routers          # "routers" is a "Python subpackage"
│      ├── __init__.py  # makes "routers" a "Python subpackage"
│      └── users.py     # "users" submodule, e.g. import app.routers.users
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
