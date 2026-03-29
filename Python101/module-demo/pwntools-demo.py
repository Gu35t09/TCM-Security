from pwn import *

print(cyclic(50))
print(cyclic_find('laaa'))

print(shellcraft.sh())
#    /* execve(path='/bin///sh', argv=['sh'], envp=0) */
#    /* push b'/bin///sh\x00' */
#    push 0x68
#    push 0x732f2f2f
#    push 0x6e69622f
#    mov ebx, esp
#    /* push argument array ['sh\x00'] */
#    /* push 'sh\x00\x00' */
#    push 0x1010101
#    xor dword ptr [esp], 0x1016972
#    xor ecx, ecx
#    push ecx /* null terminate */
#    push 4
#   pop ecx
#    add ecx, esp
#   push ecx /* 'sh\x00' */
#    mov ecx, esp
#    xor edx, edx
#    /* call execve() */
#    push SYS_execve /* 0xb */
#    pop eax
#    int 0x80

print(hexdump(asm(shellcraft.sh())))
# 00000000  6a 68 68 2f  2f 2f 73 68  2f 62 69 6e  89 e3 68 01  │jhh/│//sh│/bin│··h·│
# 00000010  01 01 01 81  34 24 72 69  01 01 31 c9  51 6a 04 59  │····│4$ri│··1·│Qj·Y│
# 00000020  01 e1 51 89  e1 31 d2 6a  0b 58 cd 80               │··Q·│·1·j│·X··│
# 0000002c
            
# Local process
# p = process("/bin/sh")
# p.sendline("echo hello;")
# p.interactive()
# p.close()

# Remote connection
# r = remote("127.0.0.1", 1234)
# r.sendline("hello!")
# r.interactive()
# r.close()

print(p32(0x13371337))
print(hex(u32(p32(0x13371337))))

l = ELF('/bin/bash')
print(hex(l.address))
print(hex(l.entry))

print(hex(l.got['write']))
print(hex(l.plt['write']))

for address in l.search(b'/bin.sh\0x00'):
    print(hex(address))

print(next(l.search(asm('jmp esp'))))
print(hex(next(l.search(asm('jmp esp')))))

r = ROP(l)
print(r.rbx)

print(xor(xor("A", "B"),"A"))

# Base64 encode
print(b64e(b"test"))
# Base64 dcode
print(b64d(b"dGVzdA=="))

# HASH
print(md5sumhex(b"hello"))
print(sha1sumhex(b"hello"))

print(bits(b'a'))
print(unbits([0, 1, 1, 0, 0, 0, 0, 1]))