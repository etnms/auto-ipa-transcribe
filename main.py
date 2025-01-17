from transcribe_audio import transcribe_large_audio_file
from write_to_file import write_text
from create_elan_file import create_empty_elan_file
from video_to_audio import convert_video_to_audio
from pathlib import Path
import argparse


def main(input_file):
    video_formats = [".mp4", ".mkv", ".webm",
                     ".flv", ".avi", ".mov", ".wnv", ".m4v"]
    is_video = False
    # Convert input_file to a Path object
    file_path = Path(input_file)

    # Check if the file suffix (extension) is in the video_formats list
    if file_path.suffix.lower() in video_formats:
        output_path = file_path.with_suffix('.wav')
        input_file = convert_video_to_audio(str(file_path), str(output_path))
        is_video = True

    text, ipa_text, chunks_information = transcribe_large_audio_file(
        input_file)

    # text = transcribe_audio("files/test_sample.wav")

    # Write final text output
    write_text("outputs", "output_text.txt", text)

    # Write IPA final output
    write_text("outputs", "output_ipa.txt", ipa_text)

    # Check if the file was a video file again, if so reinitialize input file
    # This approach is not optimal at all but temporary
    if is_video == True:
        input_file = "files/test_video.mov"

    # Usage
    create_empty_elan_file("empty_elan_file.eaf", "en",
                           input_file, chunks_information)


if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Process an audio/video file.")

    # Add an argument for the input file
    parser.add_argument(
        "input_file", help="Path to the input audio/video file")

    # Parse the command line arguments
    args = parser.parse_args()

    # Pass the input file argument to the main function
    main(args.input_file)
