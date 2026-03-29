add_4 = lambda x : x + 4
print(add_4(4)) # 8

add = lambda x, y: x + y
print(add(10, 4)) # 14

# Same thing but with function
def addf(x, y):
    return x + y

print(addf(10, 4)) # 4

# One line code
print((lambda x, y: x + y)(10,4))

# Common hacking lambda: even or odd
is_even = lambda x: x % 2 == 0
print(is_even(2))
print(is_even(3))

# Common hacking lambda: break string in blocks
blocks = lambda x, y: [x[i:i+y] for i in range (0, len(x), y)]
print(blocks("string", 2)) # ['st', 'ri', 'ng']
