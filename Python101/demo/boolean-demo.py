valid = True
not_valid = False

print(valid)
print(not_valid)

print(valid == True) # True
print(not_valid == True) # False
print(valid != True) # False

print(not valid) # False

space = "-" * 50
print(space)

print(10 > 5 and 10 < 5) # False
print(10 > 5 or 10 < 5) # True

# Bit level comparison
x = 13
print(bin(x))
print(bin(x)[2:].rjust(4, "0")) # Remove 0b at the start so return 1101

y = 5
print(bin(y))
print(bin(y)[2:].rjust(4, "0")) # Remove 0b at the start so return 0101

# Compare 1101 and 0101 at the bit level and return 1 when there are 2 1 in the same position
# 1101 
# 0101
print(bin(x & y)[2:].rjust(4, "0"))  # AND - the "second" and "forth" digit from the start are the same in eache string so the result is 0101
print(bin(x | y)[2:].rjust(4, "0"))  # OR - just one of the two digits need to be 1 so it return 1101

space = "-" * 50
print(space)

# Bit right shift 
x = 13 # 1101
print(bin(x >> 1)[2:].rjust(4, "0")) # Move all the bit to one position right --> from 1101 to 0110 
print(bin(x >> 2)[2:].rjust(4, "0")) # Same thing but 2 position

print(bin(x << 1)[2:].rjust(4, "0")) # Oppisite direction