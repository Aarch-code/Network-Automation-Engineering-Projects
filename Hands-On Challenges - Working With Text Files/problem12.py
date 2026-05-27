"""Challenge #12
Change the solution from the previous challenge so that the script considers all letters lowercase (it makes no distinction between lower and uppercase letters). file to be used american-english.txt."""

letters  = {}

with open('american-english.txt', encoding='utf-8') as f:
    words = f.read().splitlines()

    for word in words:
        for ch in  word:
            if ch.isalpha():
                ch = ch.lower()
                                
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