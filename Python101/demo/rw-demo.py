# read mode
f = open('top-100.txt')
print(f)

# read text
f = open('top-100.txt', 'rt')
print(f)

# print(f.read()) # read all file in a single string
print(f.readlines()) # with this we have an array with each line
print(f.readlines()) # return empty list []

# to read the file again
f.seek(0) # go back at the top
print(f.readlines()) 

f.seek(0)
for line in f:
    print(line.strip())

f.close()

# read bigger file
with open('rockyou.txt', encoding='latin-1') as f:
    for line in f:
        pass

# write mode
f = open("test.txt", "w")
f.write("test line!") # overwrite everything in the file
f.close

# append mode
f = open("test.txt", "a")
f.write("test line two!")
f.close

print(f.name)
print(f.closed) # True because we did f.close
print(f.mode)

# create mode

