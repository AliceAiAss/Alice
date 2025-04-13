import speech_recognition as sr

def listen(audio_file_path: str) -> str:
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)

    try:
        # Use Google's speech recognition API to transcribe
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Error with the speech recognition service"
