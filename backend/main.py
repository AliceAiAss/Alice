from fastapi import FastAPI
from backend.core.processor import process_input

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ALICE is online!"}

@app.post("/ask")
def ask_alice(payload: dict):
    user_input = payload.get("query", "")
    response = process_input(user_input)
    return {"response": response}
