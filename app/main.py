import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import dashboard, projects, user, setting, notifications

frontend_origin = os.environ.get("FRONTEND_SERVICE_URL")

app = FastAPI()
app.include_router(dashboard.router)
app.include_router(projects.router)
app.include_router(user.router)
app.include_router(setting.router)
app.include_router(notifications.router)

origins = [frontend_origin]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)


@app.get("/")
async def root():
    return {"message": "Just smile and wave boys, smile and wave."}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
