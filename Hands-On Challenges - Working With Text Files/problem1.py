"""Challenge #1
Consider macs.txt that contains multiple duplicate MAC addresses.
Create a new file that contains only unique MAC addresses. Each MAC should be on its own line."""

with open('macs.txt', 'r') as f:
    content = f.read().split()
    print(content)

    content = list(set(content))
    print(content)

with open('unique_macs.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')