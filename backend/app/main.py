from fastapi import FastAPI
from app.routes.users import router as user_router

app = FastAPI(
    title="Market9ja API",
    version="1.0.0"
)

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Welcome to Market9ja"}

