"""Challenge #10
Consider the dictionary file from the previous challenge american-english.txt.
Write a Python script that finds the first 100 longest words in the file.
Tip: See how to get a sorted view of a dictionary."""

with open('american-english.txt') as f:
    words = {
        word: len(word)
        for word in f.read().splitlines()
    }

# sort by length (largest first)
sorted_words = sorted(
    words.items(),
    key=lambda item: item[1],
    reverse=True
)

# first 100
for word, length in sorted_words[:100]:
    print(f'{word}: {length}')

