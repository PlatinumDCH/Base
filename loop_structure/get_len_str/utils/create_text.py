import os
from faker import Faker

import json

from loop_structure.get_len_str.settings import config



def generate_fake_paragraph(faker: Faker):
    return faker.paragraph(nb_sentences=10)


def generate_large_text_file(filename, parapgraphs):
    faker = Faker()
    space_count, total_lenght = 0, 0

    with open(filename, 'w') as file:
        for _ in range(parapgraphs):
            parapgraph = generate_fake_paragraph(faker)
            space_count += parapgraph.count(' ')
            total_lenght += len(parapgraph)
            file.write(parapgraph)
    
    return space_count, total_lenght

def create_metadata(filename, paragraphs, space_count, total_length):
    metadata = {
        "filename": str(filename),
        "paragraphs": paragraphs,
        "space_count": space_count,
        "total_length": total_length,
        'len_text_without_space': total_length - space_count
    }

    metadata_filename = os.path.splitext(filename)[0] + "_metadata.json"
    with open(metadata_filename, 'w') as meta_file:
        json.dump(metadata, meta_file, indent=4)

def main():
    filename = config.FILE_NAME
    paragraphs = config.NUM_PARAGRAPHS


    space_count, total_length = generate_large_text_file(
        filename, paragraphs
    )
    create_metadata(
        filename=filename,
        paragraphs=paragraphs,
        space_count=space_count,
        total_length=total_length
    )

    print(f"Generated text file: {filename}")
    print(f"Generated metadata file: {os.path.splitext(filename)[0] + '_metadata.json'}")


if __name__ == '__main__':
    main()