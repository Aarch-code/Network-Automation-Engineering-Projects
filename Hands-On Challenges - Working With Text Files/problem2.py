"""Challenge #2
Create a Python script that reads sample_file.txt into a list and then converts the list into a string that has the entire file content."""

with open('sample_file.txt') as f:
    content = f.read().splitlines()
    my_str = '\n'.join(content)
    print(my_str)