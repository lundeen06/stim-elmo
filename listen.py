import speech_recognition as sr

def listen_and_transcribe():
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    
    while True: # This loop will keep the script running indefinitely
        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            # Listen for the first phrase and extract it into audio data
            audio_data = recognizer.listen(source, timeout=3)
            try:
                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio_data)
                print(text)
            except sr.UnknownValueError:
                print("Google Web Speech API could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API service; {0}".format(e))

# Call the function to start listening and transcribing
listen_and_transcribe()