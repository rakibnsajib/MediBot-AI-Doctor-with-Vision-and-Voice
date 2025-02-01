import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")


#Step1a: Setup Text to Speech-TTS-model with gTTS
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    """
    Function to convert text to speech and save it as an MP3 file.

    Args:
    text (str): Text to convert to speech.
    output_filepath (str): Path to save the audio file.
    """
    language = "en"

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin": # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Windows": # Windows
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath], shell=True)
        elif os_name == "Linux": # Linux
            subprocess.run(['aplay', output_filepath]) # Alternative: 'mpg123', 'ffplay'
        else:
            raise OSError("Unsupported OS")
        
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = "Hello, This is a simple autoplay testing"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")



#Step1b: Setup Text to Speech-TTS-model with ElevenLabs (Alternative)
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    """
    Function to convert text to speech and save it as an MP3 file.

    Args:
    text (str): Text to convert to speech.
    output_filepath (str): Path to save the audio file.
    """
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text = input_text,
        voice = "Eric",
        output_format = "mp3_22050_32",
        model = "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin": # macOS
            subprocess.run(["afplay", output_filepath])
        elif os_name == "Windows": # Windows
            subprocess.run(["ffplay", "-nodisp", "-autoexit", output_filepath], shell=True)
        elif os_name == "Linux": # Linux
            subprocess.run(['aplay', output_filepath]) # Alternative: 'mpg123', 'ffplay'
        else:
            raise OSError("Unsupported OS")
        
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# text_to_speech_with_elevenlabs(input_text, output_filepath = "elevenlabs_testing.mp3")