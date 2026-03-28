t1_int = 1
t1_float = 1.0

print(type(t1_int))
print(t1_int)
print(type(t1_float))
print(t1_float)

t1_complex = 3.14j
print(type(t1_complex))
print(t1_complex)

t1_hex = 0xa
print(type(t1_hex)) # Integer
print(t1_hex) # 10

t1_octal = 0o10
print(type(t1_octal)) # Integer
print(t1_octal) # 8

print(1 + 0x1 + 0o1) # 3 --> 1+1+1

print(abs(4)) # 4
print(abs(-4)) # 4

print(round(8.4)) # 8
print(round(8.6)) # 9

print(bin(8)) # 0b1000