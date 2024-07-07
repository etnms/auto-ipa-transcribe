import pympi


def create_empty_elan_file(output_file, language_code):
    '''
    Function to create default Elan file, with output file name as parameter, and 
    language code for tier name (ex en or English)
    '''
    # Create a new EAF object
    eaf = pympi.Elan.Eaf()

    # Add linguistic type
    eaf.add_linguistic_type('transcription')

    # Add an empty tier
    eaf.add_tier(f'Transcription ({language_code})', ling='transcription')

    # Save the EAF to file
    eaf.to_file(output_file)

    print(f"Empty ELAN file created: {output_file}")


def add_annotations():
    '''
    Function to automatically add annotations for transcription and IPA
    '''
    pass


# Usage
create_empty_elan_file("empty_elan_file.eaf", "en")
