from audio_extract import extract_audio
import os

input_path = "./files/test_video.mov"
output_path = "./files/test_video_audio.mp3"

# Supported audio formats : WAV, OGG, MP3, AAC, FLAC, M4A, OGA, OPUS

# Supported video formats : MP4, MKV, WEBM, FLV, AVI, MOV, WMV, M4V


def convert_video_to_audio(input_path, output_path):
    # return file as wav to keep quality
    if os.path.exists(output_path):
        os.remove(output_path)
    extract_audio(input_path, output_path, "wav")
    return output_path
