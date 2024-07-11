import eng_to_ipa as ipa
from transcribe_audio import transcribe_audio, transcribe_large_audio_file
from write_to_file import write_text
from create_elan_file import create_empty_elan_file
from video_to_audio import convert_video_to_audio
from pathlib import Path


# Audio file to work with
input_file = "files/test_video.mov"
video_formats = [".mp4", ".mkv", ".webm",
                 ".flv", ".avi", ".mov", ".wnv", ".m4v"]

# Convert input_file to a Path object
file_path = Path(input_file)

# Check if the file suffix (extension) is in the video_formats list
if file_path.suffix.lower() in video_formats:
    output_path = file_path.with_suffix('.wav')
    input_file = convert_video_to_audio(str(file_path), str(output_path))

'''

text, ipa_text, chunks_information = transcribe_large_audio_file(
    input_file)

# text = transcribe_audio("files/test_sample.wav")

# Write final text output
write_text("outputs", "output_text.txt", text)

# Write IPA final output
write_text("outputs", "output_ipa.txt", ipa_text)

# Usage
create_empty_elan_file("empty_elan_file.eaf", "en",
                       input_file, chunks_information)
'''
