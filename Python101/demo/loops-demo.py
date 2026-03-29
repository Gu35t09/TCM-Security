a = 1 
print(a)

while a < 5:
    a += 1
    print(a)

# Method 1
for i in [0, 1, 2, 3 ,4]:
    print(i+6)

print("---")

# Method 2
for i in range(5):
    print(i+6)


for i in range(3):
    for j in range(3):
        print(i,j)

# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# Brakes
print("---")

for i in range(5):
    if i == 2:
        break # stop the loop at 2
    print(i)

print("---")

for i in range(5):
    if i == 2:
        continue # skip the loop execution
    print(i)

print("---")

for i in range(5):
    if i == 2:
        pass # nothing changes and go on
    print(i)

# String

print("---")
for c in "string":
    print("c")

# You can iterate also over dictionary