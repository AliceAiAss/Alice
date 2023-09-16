# Importing the Chatbot.
from Brain.Chatgpt import ChatGPTBrain
from Voices import speak
import pyttsx3
import speech_recognition as sr

# Initialize the microphone and TTS engine.
r = sr.Recognizer()

# Taking the command.
def Activating():
    # Initialize the speech recognition recognizer
    r = sr.Recognizer()

    # print("Allow me to Introduce myself. I am Alice, Your virtual assistant.")
    speak("Allow me to Introduce myself. I am Alice, Your virtual assistant.")

    while True:
        with sr.Microphone() as source:
            print("Listening...")

            try:
                # Use recognizer to listen to the user's input
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=5)
                query = r.recognize_google(audio, language="en-US")
                print(f"You said: {query}")

                # Send the query to the chatbot and get the response
                chatbot_response = ChatGPTBrain(query)

                if chatbot_response:
                    # Speak the chatbot's response
                    speak(chatbot_response)
                else:
                    print("Chatbot did not provide a response.")

            except sr.WaitTimeoutError:
                print("Speech recognition timed out. Please try again.")
                speak("Speech recognition timed out. Please try again.")

            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                speak("I am sorry, but I couldn't understand your request.")

            except sr.UnknownValueError:
                print("Sorry, I did not understand what you said.")
                speak("Sorry, I did not understand what you said.")

# Example usage:
if __name__ == "__main__":
    Activating()
