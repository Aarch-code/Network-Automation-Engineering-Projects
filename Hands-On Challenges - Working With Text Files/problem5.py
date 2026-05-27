"""Challenge #5
Change the solution from the previous challenge so that the script that prints out the last n lines of sample_file.txt refreshes the output every 3 seconds (as the file changes or updates). This is similar to the tail -f Linux command."""

import time
def tail(file, n):
    with open ('sample_file.txt', 'r') as f:
        content = f.read().splitlines()
        last = content[-n:]
        my_str = '\n'.join(last)
        return my_str
    
while True:
    t = tail('sample_file.txt', 5)
    print(t)
    time.sleep(3)
    print('')