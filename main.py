from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "👋 Hello from FastAPI!"}

@app.get("/api/v1/greeting")
async def greeting(name: str = "World"):
    return {"message": f"Hello, {name}!"}

@app.get("/api/v1/users")
async def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

@app.post("/api/v1/users")
async def create_user(user: dict):
    user["id"] = 3
    return user
