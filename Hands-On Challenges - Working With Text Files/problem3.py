"""Challenge #3
Create a Python script that removes all empty lines including those that contain only spaces from file.txt"""

with open('file.txt') as f:
    content_list = f.readlines()
    # print(content_list)

tmp_list = [line for line in content_list if line.strip() != '']
print(tmp_list)

with open ('file_without_spaces.txt', 'w') as f:
    f.write(''.join(tmp_list))