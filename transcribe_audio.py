import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from split_audio_file import clear_chunk_directory


# create a speech recognition object
r = sr.Recognizer()


# function to recognize speech in the audio file
def transcribe_audio(path):
    # use the audio file as the audio source
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        # try converting it to text
        text = r.recognize_google(audio_listened)
    return text


# a function that splits the audio file into chunks on silence and applies speech recognition
def get_large_audio_transcription_on_silence(path):
    """Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks"""

    # open the audio file using pydub
    sound = AudioSegment.from_file(path)

    # split audio sound based on silence
    chunks = split_on_silence(
        sound,
        min_silence_len=700,
        silence_thresh=sound.dBFS-14,
        keep_silence=200
    )

    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    # Initialize empty values to use throughout the function
    chunks_information = []
    current_time = 0
    whole_text = ""

    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # Calculate start and end times
        start_time = current_time
        end_time = start_time + len(audio_chunk)

        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        # recognize the chunk
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            # Store timing information
            chunks_information.append({
                'chunk': i,
                'start_time': start_time,
                'end_time': end_time,
                'duration': len(chunk_filename),
                'text': text
            })

            # Update current_time for the next chunk
            current_time = end_time

            # Display text, alone or as a whole
            text = f"{text.capitalize()}. "
            # print(chunk_filename, ":", text)

            whole_text += text

    # Clear chunk directory
    clear_chunk_directory(folder_name)

    # return the text for all chunks detected
    return whole_text, chunks_information
