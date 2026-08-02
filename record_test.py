from voice.recorder import record_audio

print("🎤 Recording Test...")

path = record_audio()

print(f"✅ Recording saved at: {path}")