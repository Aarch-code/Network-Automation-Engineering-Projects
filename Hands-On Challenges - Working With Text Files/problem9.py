"""Challenge #9
Consider this dictionary file american-english.txt.
Write a Python script that reads the file in a dictionary. The words in the file will be the dictionary keys and the length of each word the corresponding values."""

with open('american-english.txt') as f:
    words = {
        word: len(word)
        for word in f.read().splitlines()
    }

with open('new_dict.txt', 'w') as f2:
    for word, length in words.items():
        f2.write(f'{word}: {length}\n')