from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/web", StaticFiles(directory="../frontend/web"), name="web")

# ALICE API endpoint
@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    message = data.get("message")
    
    # Dummy reply (replace with actual ALICE logic)
    response = f"Received: {message}"
    
    return JSONResponse(content={"response": response})
