#!/usr/bin/python3
from pwn import *

session = ssh(host='pwnable.kr',user='col',password='guest',port=2222)

payload = p32(0x08080808)*4 + p32(0x1bce9cc)
process = session.process(executable='./col',argv=['col',payload])
print(process.recvall().decode("utf-8"))

session.close()
