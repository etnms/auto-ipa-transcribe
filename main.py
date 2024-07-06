import eng_to_ipa as ipa
from transcribe_audio import transcribe_audio, get_large_audio_transcription_on_silence


text = get_large_audio_transcription_on_silence("files/test2.wav")
# text = transcribe_audio("files/test_sample.wav")
ipa_text = ipa.convert(text)
print(ipa_text)

# create an output with the IPA transcription
with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(ipa_text)
