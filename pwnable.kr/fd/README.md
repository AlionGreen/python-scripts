# challenge Description
Mommy! what is a file descriptor in Linux?

* try to play the wargame your self but if you are ABSOLUTE beginner, follow this tutorial link:
https://youtu.be/971eZhMHQQw

ssh fd@pwnable.kr -p2222 (pw:guest)

## solution
this challenge is about learning file decriptors.
you can read more in https://en.wikipedia.org/wiki/File_descriptor

in order to read the **LETMEWIN** value from the input and get the flag, we need to specify the fd variable to 0. so we should provide **4660** (0x1234 in decimal)
as the first argument of the program. then we should give **LETMEWIN** to the program to get the flag.

run fd.py to get the flag :)
