import wave
import math

def get_audio_length(file_path):
    with wave.open(file_path, 'rb') as audio_file:
        sample_width = audio_file.getsampwidth()
        frame_rate = audio_file.getframerate()
        num_frames = audio_file.getnframes()
        audio_length = num_frames / float(frame_rate)
        return math.ceil(audio_length)


