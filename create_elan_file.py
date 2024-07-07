import pympi


def create_empty_elan_file(output_file):
    # Create a new EAF object
    eaf = pympi.Elan.Eaf()

    # Add a default linguistic type
    eaf.add_linguistic_type('default-lt')

    # Add an empty tier
    eaf.add_tier('default')

    # Save the EAF to file
    eaf.to_file(output_file)

    print(f"Empty ELAN file created: {output_file}")


# Usage
create_empty_elan_file("empty_elan_file.eaf")
