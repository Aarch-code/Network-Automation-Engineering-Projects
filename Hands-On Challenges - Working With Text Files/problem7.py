"""Challenge #7
Write a Python program that calculates the net amount of a bank account based on the transactions that are saved in banking.txt.
The file format is as follows:
D:50
W:100
D means deposit while W means withdrawal.
Suppose that the following file is supplied to the program:
D:300
D:300
W:500
D:200
Then, the output should be: 300"""

with open ('banking.txt', 'r') as f:
    content = f.read().splitlines()
    # print(content)

    deposit=0
    withdrawal=0
    for items in content:
        tmp = items.split(':')
        # print(tmp)
        if (tmp[0] == 'D'):
            deposit += int(tmp[1])
        elif (tmp[0] == 'W'):
            withdrawal += int(tmp[1])
        else:
            print("File format Error")

balance = deposit - withdrawal
print(balance)