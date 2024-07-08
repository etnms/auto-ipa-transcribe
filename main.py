import eng_to_ipa as ipa
from transcribe_audio import transcribe_audio, get_large_audio_transcription_on_silence
from write_to_file import write_text
from create_elan_file import create_empty_elan_file


text, ipa_text, chunks_information = get_large_audio_transcription_on_silence(
    "files/test2.m4a")

# text = transcribe_audio("files/test_sample.wav")

# Write final text output
write_text("outputs", "output_text.txt", text)

# Write IPA final output
write_text("outputs", "output_ipa.txt", ipa_text)

# Usage
create_empty_elan_file("empty_elan_file.eaf", "en", chunks_information)
