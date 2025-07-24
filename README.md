# 🚀 FastAPI on Heroku – Deployment Guide

This guide walks you through deploying a basic FastAPI app to Heroku using `gunicorn` and `uvicorn.workers.UvicornWorker`.

---

## 📁 Project Structure

```
fastapi-heroku-demo/
├── main.py
├── requirements.txt
├── Procfile
└── runtime.txt (optional)
```

---

## 1️⃣ main.py

```python
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
```

---

## 2️⃣ requirements.txt

```txt
annotated-types==0.7.0
anyio==4.9.0
click==8.2.1
fastapi==0.116.1
gunicorn
h11==0.16.0
idna==3.10
pydantic==2.11.7
pydantic_core==2.33.2
sniffio==1.3.1
starlette==0.47.2
typing-inspection==0.4.1
typing_extensions==4.14.1
uvicorn==0.35.0
```

---

## 3️⃣ Procfile (no file extension)

```
web: gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
```

---

## 4️⃣ (Optional) runtime.txt

Specify the Python version (optional but recommended):

```
python-3.11.8
```

---

## ✅ Local Test (optional)

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🚀 Deploy to Heroku (No Docker)

### 1. Login to Heroku

```bash
heroku login
```

---

### 2. Create Heroku App

```bash
heroku create fastapi-hello-demo
```

Or let Heroku assign a random name.

---

### 3. Push Code to Heroku

```bash
git init
git add .
git commit -m "Initial FastAPI deploy"
git push heroku master
```

If you're using `main` branch:

```bash
git push heroku main
```

---

### 4. Open Your App

```bash
heroku open
```

Or visit:

```
https://fastapi-hello-demo.herokuapp.com/
https://fastapi-hello-demo.herokuapp.com/docs
```

---

## 🧠 Notes

* Heroku sets `$PORT` automatically. You must bind Gunicorn to `0.0.0.0:$PORT`.
* No `Procfile` = Heroku fails to start your app.
* FastAPI’s interactive Swagger docs will be available at `/docs`.

---

## ✅ Summary

| Item               | Purpose                          |
| ------------------ | -------------------------------- |
| `main.py`          | FastAPI app definition           |
| `requirements.txt` | Heroku uses this to install deps |
| `Procfile`         | Tells Heroku how to run your app |
| `gunicorn`         | Production-grade WSGI server     |
