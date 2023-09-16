import os
import speech_recognition as sr
from Alice import Activating 


def takecommand():
    # Initialize the speech recognition recognizer
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    
        try:
            query = r.recognize_google(audio, language="en-US")
            
        except:
            return "none"
        
        
        return query.lower()

    

while True:
    
    query = takecommand()    
    if "wake up alice" in query:
        Activating()
        break
                
    else:
        print("")