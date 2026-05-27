"""Challenge #4
Create a Python function called tail that reads the last n lines of sample_file.txt. The function has two arguments: the file name and n (the number of lines to read). This is similar to the Linux `tail` command.
Example: tail('sample_file.txt', 5) will return the last 5 lines from sample_file.txt."""

def tail(file, n):
    with open (file, 'r') as f:
        content = f.read().splitlines()
        last = content[-n:]
        my_str = '\n'.join(last)
        return my_str
    

t = tail('sample_file.txt', 5)
print(t)