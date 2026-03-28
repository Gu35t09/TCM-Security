# Looping

# For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"] # List

for veggies in vegetables:
    print(veggies)

for i in range(5):
    print(i)

word = "Python"
for letter in word:
    print(letter)

# Ping sweeper in linux
#192.168.1.x
#1-254
#for ip in 1..254
#    ping 192.168.1.ip

# While loops - execute as long a True
i = 1

while (i < 10):
    print(i)
    i += 1

password = ""

while password != "spaghetti":
    password = input("Enter the secret password: ")

print("Access granted!!")