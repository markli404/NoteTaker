import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import os


class Recorder:
    def __init__(self, duration=15, sample_rate=44100, filename='test'):
        self.duration = duration
        self.sample_rate = sample_rate
        self.filename = filename

    def record_audio(self):
        print(f"Recording for {self.duration} seconds...")
        recording = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=2, dtype='int16')
        sd.wait()  # Wait until recording is finished
        write('{}.wav'.format(self.filename), self.sample_rate, recording)  # Save as WAV file
        print(f"Recording saved as {self.filename}.wav")

    def get_audio(self):
        self.record_audio()
        file = open(f'{self.filename}.wav', "rb")

        return file