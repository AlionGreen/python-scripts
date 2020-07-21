from pwn import *

host, port = '10.10.147.219',3404
s = remote(host,port)
s.recvline()

while 1:
    op = s.recvline()
    op = op.decode('utf-8')
    print(op)
    if 'flag' in op:
        print(op)
        msg = s.recvall()
        msg = msg.decode('utf-8')
        print(msg)
        break
    solve = op.split(' ')
   
    if 'add' == solve[1]:
        res = int(solve[0])+int(solve[2])
    if 'minus' == solve[1]:
        res = int(solve[0])-int(solve[2])
    if 'multiply' == solve[1]:
        res = int(solve[0])*int(solve[2])

    print(res)
    s.sendline(str(res))

s.close()