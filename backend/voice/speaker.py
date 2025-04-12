import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Adjust speed
engine.setProperty('volume', 1.0)  # Max volume

def speak(text):
    print(f"🔊 ALICE: {text}")
    engine.say(text)
    engine.runAndWait()
