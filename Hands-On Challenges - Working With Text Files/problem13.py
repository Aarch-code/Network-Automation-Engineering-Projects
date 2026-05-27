"""Challenge #13
Continue the previous challenge and find the 3 most frequently used letters in all English Words.
You should get: ('e', 67681), ('s', 50872), ('i', 50818). file to be used american-english.txt."""

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

sorted_letters = sorted(
    letters.items(),
    key=lambda item: item[1],
    reverse=True
)

top3 = sorted_letters[:3]

print(top3)