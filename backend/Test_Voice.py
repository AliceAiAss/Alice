from voice.listener import listen
from voice.speaker import speak
from core.processor import process_input

def run():
    while True:
        query = listen()
        response = process_input(query)
        speak(response)

if __name__ == "__main__":
    run()
