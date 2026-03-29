test = input("Enter the IP: ")
print(test)

print("---")

while True:
    test = input("Enter the IP: ")
    print(">>> {}".format(test))
    if test == "exit":
        break
    else:
        print("exploiting...")
