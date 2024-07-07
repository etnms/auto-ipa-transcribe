from pydub import AudioSegment
from pydub.silence import split_on_silence
import os


def split_audio_file(path):
    sound = AudioSegment.from_file(path)
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

    timestamps = []
    current_time = 0

    # process each chunk
    for i, chunk in enumerate(chunks, start=1):
        # Calculate start and end times
        start_time = current_time
        end_time = start_time + len(chunk)

        # export audio chunk and save it
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        chunk.export(chunk_filename, format="wav")

        # Store timing information
        timestamps.append({
            'chunk': i,
            'start_time': start_time,
            'end_time': end_time,
            'duration': len(chunk)
        })

        # Update current_time for the next chunk
        current_time = end_time

    print("Timestamps for each chunk:")
    for ts in timestamps:
        print(
            f"Chunk {ts['chunk']}: Start: {ts['start_time']}ms, End: {ts['end_time']}ms, Duration: {ts['duration']}ms")

    return timestamps


path = "files/test2.m4a"

timestamps = split_audio_file(path)