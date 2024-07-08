import eng_to_ipa as ipa
from transcribe_audio import transcribe_audio, transcribe_large_audio_file
from write_to_file import write_text
from create_elan_file import create_empty_elan_file


# Audio file to work with
audio_file = "files/test_sample.wav"


text, ipa_text, chunks_information = transcribe_large_audio_file(
    audio_file)

# text = transcribe_audio("files/test_sample.wav")

# Write final text output
write_text("outputs", "output_text.txt", text)

# Write IPA final output
write_text("outputs", "output_ipa.txt", ipa_text)

# Usage
create_empty_elan_file("empty_elan_file.eaf", "en",
                       audio_file, chunks_information)
