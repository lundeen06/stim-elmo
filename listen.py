import speech_recognition as sr

# # find mics
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def listen_and_transcribe():
    # Create a recognizer instance
    recognizer = sr.Recognizer()
    while True: # This loop will keep the script running indefinitely
        # Use the default microphone as the audio source
        with sr.Microphone(device_index=0) as source:
            # print(source)
            # Listen for the first phrase and extract it into audio data
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source, timeout=2)
            try:
                # Recognize speech using Google Web Speech API
                text = recognizer.recognize_google(audio_data)
                print(text)
            except sr.UnknownValueError:
                print("Elmo can not understand your tomfoolery and shenanigans at this moment. Repeat that again, you bumbling buffoon >:(")
            except sr.RequestError as e:
                print("Could not request results from Google Web Speech API service; {0}".format(e))
            except sr.WaitTimeoutError:
                print('speak, fool!')


# Call the function to start listening and transcribing
listen_and_transcribe()