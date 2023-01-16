import json

"""
vowel - smogłoska
consonant - spółgłoska
"""


def read_alphabets(fh):
    return json.load(fh)


def concat_alphabets(aphs, new_name, new_aph):
    aphs[0][new_name] = new_aph


def write_alphabets(fh, aphs):
    json.dump(aphs, fh, indent=4)


def add_alphabet(file_name, alphabet_name, new_alphabet):
    with open(file_name, 'r') as fh:
        all_alphabets = read_alphabets(fh)
        concat_alphabets(all_alphabets, alphabet_name, new_alphabet)
    with open(file_name, 'w') as fh:
        write_alphabets(fh, all_alphabets)


def generate_file(file_name, alphabet_name, new_alphabet):
    with open(file_name, 'w') as fh:
        write_alphabets(fh, [{alphabet_name: new_alphabet}])


def create_alphabet(vowels, consonants):
    return {"vowels": vowels, "consonants": consonants}


def print_alphabets(file_name):
    with open(file_name, 'r') as fh:
        aphs = read_alphabets(fh)
    print("All alphabets:")
    for key in aphs[0].keys():
        print(f"{key}:\n  vowels:     {aphs[0][key]['vowels']}\n  consonants: {aphs[0][key]['consonants']}")


def get_alphabet_dict(file_name):
    with open(file_name, 'r') as fh:
        return read_alphabets(fh)[0]


if __name__ == "__main__":
    # alphabet = create_alphabet("eyuioaęóą", "qwrtpsdfghjklzxcvbnmśłżźćń")
    # alphabet = create_alphabet("a", "bc")
    # add_alphabet("alphabets.json", "polish", alphabet)
    # generate_file("alphabets.json", "minimal", alphabet)
    print(get_alphabet_dict("alphabets.json"))
