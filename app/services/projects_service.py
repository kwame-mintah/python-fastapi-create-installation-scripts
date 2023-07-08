import os

from fastapi import HTTPException
from fastapi.responses import FileResponse


def remove_existing_file(name):
    os.remove(name) if os.path.exists(name) else print("file doesn't exist")


class ProjectsService:
    stub_data = {
        "projects": [
            {
                "projectId": "bxsHg",
                "projectName": "Cartoon Network",
                "projectDescription": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos blanditiis tenetur"
                "unde suscipit, quam beatae rerum inventore consectetur, neque doloribus, cupiditate"
                "numquam dignissimos laborum fugiat deleniti? Eum quasi quidem quibusdam.",
                "startDate": 1641562241,
                "endDate": 1688733111,
            },
            {
                "projectId": "fPvAb",
                "projectName": "Jetix",
                "projectDescription": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada"
                "lacus ex, sit amet blandit leo lobortis eget. Lorem ipsum dolor sit amet,"
                "consectetur adipiscing elit. Suspendisse malesuada lacus ex, sit amet blandit"
                "leo lobortis eget.",
                "startDate": 1673098241,
                "endDate": 1688736654,
            },
        ]
    }

    stub_data_details = {
        "projectId": "bxsHg",
        "projectName": "Cartoon Network",
        "details": {
            "softwarePackages": [
                {"name": "openjdk", "version": "13"},
                {"name": "node", "version": "18.16.1"},
                {"name": "python", "version": "3.9"},
            ]
        },
    }

    def return_stub_data(self):
        return self.stub_data

    def return_stub_data_id(self, identifier: str):
        self.check_project_exists(identifier)
        return self.stub_data_details

    def return_stub_data_software_packages(self, identifier: str, system: str):
        self.check_project_exists(identifier)
        name = (
            self.stub_data_details["projectName"].replace(" ", "_").lower()
            + "_"
            + system
        )
        packages = self.stub_data_details["details"]["softwarePackages"]
        if system == "macOS":
            shell = name + ".sh"
            # brew leaves > packages.txt
            # xargs brew install < packages.txt
            remove_existing_file(shell)
            for package in packages:
                with open(shell, "a") as f:
                    f.write(
                        "brew install "
                        + package["name"]
                        + "@"
                        + package["version"]
                        + "\n"
                    )
                    f.close()
            return FileResponse(path=shell, filename=shell)
        elif system == "winOS":
            # Any package name ending with .config is considered a 'packages.config' file.
            # Please see https://ch0.co/packages_config
            config = name + ".config"
            remove_existing_file(config)
            for package in packages:
                with open(config, "a") as f:
                    f.write(
                        "choco install "
                        + package["name"]
                        + " --version="
                        + package["version"]
                        + "\n"
                    )
                    f.close()
            return FileResponse(path=config, filename=config)
        elif system == "linux":
            # sudo apt-get install package1 package2 package3 -y
            shell = name + ".sh"
            remove_existing_file(shell)
            for package in packages:
                with open(shell, "a") as f:
                    f.write(
                        "apt-get install " + package["name"] + package["version"] + "\n"
                    )
                    f.close()
            return FileResponse(path=shell, filename=shell)
        else:
            raise HTTPException(
                status_code=400, detail=f"Unable to installation script for {os}"
            )

    def check_project_exists(self, identifier):
        if identifier != self.stub_data_details["projectId"]:
            raise HTTPException(status_code=404, detail="Project not found")
