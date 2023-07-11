import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import dashboard, projects, user, setting, notifications

comma_separated_origins = os.environ.get("ALLOW_CORS_ORIGINS")

app = FastAPI()
app.include_router(dashboard.router)
app.include_router(projects.router)
app.include_router(user.router)
app.include_router(setting.router)
app.include_router(notifications.router)

allow_origins = comma_separated_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)


@app.get("/")
async def root():
    return {"message": "Just smile and wave boys, smile and wave."}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
