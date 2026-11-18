import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Version 2"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/env-check")
def env_check():
    # Proves environment variables work 
    return {"my_secret_set": os.getenv("MY_SECRET") is not None}