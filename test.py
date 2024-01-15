from gtts import gTTS
import os

# Sample text to be converted to speech
text_to_speak = "Hello, this is a test of the TTS library."

# Create a gTTS object
tts = gTTS(text_to_speak, lang='en')

# Save the audio file
tts.save("test.mp3")

# Play the audio file (this command may vary based on your OS and installed applications)
os.system("start test.mp3")

