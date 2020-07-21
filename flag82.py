from pwn import *
import base64

host, port = '10.10.147.219', 3338

ses = remote(host,port)
ses.recvline()

while 1:
    enc = ses.recvline()
    enc = enc.decode('utf-8')
    if 'flag' in enc:
        msg2 = ses.recvall()
        msg2 = msg2.decode('utf-8')
        print(enc+"\n"+msg2)
        break        
    enc = base64.b64decode(enc)
    ses.sendline(enc)
    print(enc)


print(ses.recvall())

ses.close()