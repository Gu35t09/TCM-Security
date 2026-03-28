name = "neut"
print(name)

name_length = len(name)
print(name_length)

# It is possibile to create 2 variable in one line with the comma
name2, name2_length = "mattia", 6
print(f"{name2} is {name2_length} letter")

print(type(name2)) # String
print(type(name2_length)) # Int

name_length = "4"
print(type(name_length)) # String now

name_length = int("4")
print(type(name_length)) # Integer now

# name = int("mattia") won't work

# Variables are case sensitive
name_length = 10
Name_length = 15
print(name_length)
print(Name_length)

name_list = ["Mattia", "Gu35t09"]
print(name_list)

name1, name2 = name_list
print(name1)
print(name2)


name_dictionary = {"mattia": 6, "Gu35t09": 7}
print(type(name_dictionary))

name_range = range(6)
print(type(name_range))
print(name_range)

name_bytes = b"Mattia"
print(type(name_bytes))
print(name_bytes)
