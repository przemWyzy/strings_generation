from random import randint, choice

from gener_alphabet import get_alphabet_dict


def generate_name():
    alphabet = get_alphabet_dict("alphabets.json")["english"]
    vowels = list(alphabet["vowels"])
    consonants = list(alphabet["consonants"])
    new_name = ""
    for i in range(randint(1, 4)):
        for j in range(randint(0, 2)):
            new_name += choice(consonants)
        new_name += choice(vowels)
        for j in range(randint(0, 2)):
            new_name += choice(consonants)
    return new_name.capitalize()


if __name__ == "__main__":
    for _ in range(10):
        print(generate_name())
