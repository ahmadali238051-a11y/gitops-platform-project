
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Production GitOps Platform is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
