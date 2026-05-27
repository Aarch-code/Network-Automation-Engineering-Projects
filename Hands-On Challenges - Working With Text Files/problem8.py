"""Challenge #8
Write a Python script that compares line by line two text files a.txt and b.txt and displays the lines that differ."""

with open('a.txt') as f1:
    file1 = f1.read().splitlines()

with open('b.txt') as f2:
    file2 = f2.read().splitlines()

for i, (a, b) in enumerate(zip(file1, file2), start = 1):
    if a != b:
        print(f'file1 ({i}): {a}')
        print(f'file2 ({i}): {b}')        