import webrtcvad
import wave
import math

# Load WAV file
audio = wave.open("./python/audioDetector/audio.wav", "rb")

# Sensitivity settings
    # Vad(0): Less sensitive (accurate but may miss quiet voices)
    # Vad(1): Normal sensitivity
    # Vad(2): Sensitive (detects even low-volume voices)
    # Vad(3): Most sensitive (may falsely detect background noise as speech)
vad = webrtcvad.Vad(3)

frame_duration = 30  # ms
frame_size = int(audio.getframerate() * frame_duration / 1000)
num_frames = math.ceil(audio.getnframes() / frame_size)

speech_time = 0

for i in range(num_frames):
    frame = audio.readframes(frame_size)
    if len(frame) < frame_size * audio.getsampwidth():
        frame = frame.ljust(frame_size * audio.getsampwidth(), b'\0')
    if vad.is_speech(frame, audio.getframerate()):
        speech_time += frame_duration / 1000

total_duration = audio.getnframes() / audio.getframerate()
silence_time = total_duration - speech_time

print(f"Total duration: {total_duration:.2f} seconds")
print(f"Speech duration: {speech_time:.2f} seconds")
print(f"Silence duration: {silence_time:.2f} seconds")
