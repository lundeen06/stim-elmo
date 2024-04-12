from gtts import gTTS
import os
import getpass
import platform

def text_to_speech(text):
    # Create a gTTS object
    speech = gTTS(text=text, lang='en', tld='com-au', slow='slow')
    
    # Use getpass.getuser() to get the current user's name
    user_name = getpass.getuser()
    
    # Construct the save path using the user's name
    save_path = os.path.join(os.path.expanduser('~'), 'text_to_speech.mp3')
    
    # Ensure the directory exists
    directory = os.path.dirname(save_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Save the audio to the specified path
    speech.save(save_path)
    
    # Determine the command to open the file based on the operating system
    system = platform.system()
    if system == 'Windows':
        os.system(f'start {save_path}')
    elif system == 'Darwin': # macOS
        os.system(f'open {save_path}')
    else: # Assume Linux
        os.system(f'xdg-open {save_path}')