import os
import pyttsx3

def convert_text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Create the audio folder if it doesn't exist
    folder_path = "audio"
    os.makedirs(folder_path, exist_ok=True)

    # Convert text to speech
    speech_output = os.path.join(folder_path, "output.mp3")
    engine.save_to_file(text, speech_output)
    engine.runAndWait()

# Example usage:

