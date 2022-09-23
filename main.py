import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv
import random

freq = 44100
duration = int(4)
recording = sound.rec(duration * freq,
                      samplerate=freq, channels=2)
sound.wait()
name = 'recording_' + str(random.randint(1, 1000)) + '.wav'
write(name, freq, recording)
print(name)
