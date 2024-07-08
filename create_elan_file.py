import pympi
import os


def create_empty_elan_file(output_file, language_code, linked_file, chunks_information):
    '''
    Function to create default Elan file, with output file name as parameter, and 
    language code for tier name (ex en or English)
    '''
    delete_previous_file(output_file)
    # Create a new EAF object
    eaf = pympi.Elan.Eaf(author="auto-ipa")

    # Add a linked file based on relative path
    # This approach may need to be changed for better use from the user's end
    abs_path_file = os.path.abspath(linked_file)
    eaf.add_linked_file(abs_path_file, relpath=linked_file)

    # Add linguistic type
    eaf.add_linguistic_type("transcription")
    eaf.add_linguistic_type("ipa-transcription")

    # Define tier ids
    transcription_tier_id = f"Transcription ({language_code})"
    ipa_tier_id = f"IPA Transcription"

    # Add an empty tier
    eaf.add_tier(transcription_tier_id, ling="transcription")
    eaf.add_tier(ipa_tier_id, ling="ipa-transcription")

    # Add annotation
    add_annotations(eaf, transcription_tier_id, chunks_information, "text")
    add_annotations(eaf, ipa_tier_id, chunks_information, "ipa_text")
    # Save the EAF to file
    eaf.to_file(output_file)

    print(f"Empty ELAN file created: {output_file}")


def add_annotations(file, id_tier, chunks_information, value):
    '''
    Function to automatically add annotations for transcription and IPA
    '''
    print(chunks_information)
    for chunk in chunks_information:
        file.add_annotation(
            id_tier, chunk["start_time"], chunk["end_time"], chunk[value])


def delete_previous_file(filename):
    try:
        os.remove(filename)
    except:
        print("No file of the same name created before")
