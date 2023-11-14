from Recorder import Recorder
from openai import OpenAI
import os

# OPENAI Setting
os.environ['OPENAI_API_KEY'] = ''
client = OpenAI()

# Load Recorder
recorder = Recorder()
audio_file = recorder.get_audio()
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format="text"
)

print(transcript)