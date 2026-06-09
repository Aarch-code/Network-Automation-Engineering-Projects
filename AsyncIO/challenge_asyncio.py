import asyncio

async def run(cmd):
   proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

   stdout, stderr = await proc.communicate()

#    print(f'{cmd} exited with status code: {proc.returncode}]')  # will normally show full ping output 

# will show "address" is UP
   ip = cmd.split()[-1]
   status = "UP" if proc.returncode == 0 else "DOWN"
   print(f'{ip} is {status}')

   if stdout:
       print(f'STDOUT:\n{stdout.decode()}')

   if stderr:
       print(f'STDERROR:\n{stderr.decode()}')

async def main(net_addr):
   tasks = []
   for cmd in net_addr:
        command = f'ping -n 1 {cmd}'
        tasks.append(run(command))

   await asyncio.gather(*tasks)

net_addr = ('8.8.8.8', '1.1.1.1', '208.67.222.222', '192.168.0.1')
asyncio.run(main(net_addr))