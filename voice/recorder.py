import sounddevice as sd
from scipy.io.wavfile import write
import os

SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 5

def record_audio(output_path="voices/temp/current.wav"):

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("🎤 Recording...")

    recording = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="int16"
    )

    sd.wait()

    write(output_path, SAMPLE_RATE, recording)

    print("✅ Recording Saved:", output_path)

    return output_path