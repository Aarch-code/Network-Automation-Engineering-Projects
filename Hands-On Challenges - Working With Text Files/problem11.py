"""Challenge #11
Consider this dictionary file american-english.txt.
Write a Python script that finds the number of occurrences of each letter of the alphabet in all the words of the dictionary. Make a distinction between lower and uppercase letters.
You want to see how many times 'a', 'A', 'b', 'B', 'c', 'C', 'd' and so on appear in all the words in the dictionary.
Which is the most frequently used letter in English words? But the least frequently used one?"""

letters  = {}

with open('american-english.txt', encoding='utf-8') as f:
    words = f.read().splitlines()

    for word in words:
        for ch in  word:
            if ch.isalpha():
                if ch not in letters:
                    letters[ch] = 1
                else:
                    letters[ch] += 1

for letter in sorted(letters):
    print(f'{letter}: {letters[letter]}')

most_used = max(letters, key=letters.get)
least_used = min(letters, key=letters.get)

print()
print(f'Most frequent: {most_used} ({letters[most_used]})')
print(f'Least frequent: {least_used} ({letters[least_used]})')
