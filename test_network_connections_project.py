# project: test network connections

import subprocess
with open ('hosts.txt') as f:
    ip_addr = f.read().splitlines()
    # print(ip_addr)
    for ip in ip_addr:
        try:
            command = f'ping -n 1 {ip}'
            output = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(f'host {ip} is down => {e}')
        print('#' * 50)