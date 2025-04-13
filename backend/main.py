import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydub import AudioSegment

app = FastAPI()

# Folder to save uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/api/listen")
async def listen_audio(file: UploadFile = File(...)):
    # Save uploaded audio file to the uploads folder
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    # Process the uploaded audio file (convert to WAV)
    try:
        audio = AudioSegment.from_file(file_location)  # Reads file
        processed_file_location = file_location.replace(".wav", "_processed.wav")
        audio.export(processed_file_location, format="wav")  # Save as processed file
        return {"message": f"Audio file '{file.filename}' received, saved, and processed.", "processed_file": processed_file_location}
    except Exception as e:
        return {"message": "Error processing audio file", "error": str(e)}

@app.get("/api/download/{file_name}")
async def download_file(file_name: str):
    file_path = f"uploads/{file_name}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/wav", filename=file_name)
    return {"message": "File not found"}
