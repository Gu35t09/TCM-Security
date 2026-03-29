string1 = "I am a string!"
string2 = 'I am a string too'

print(string1)
print(string2)

# Multi-line string
string3 = """I am a long
long
string!"""

string4 = "I\"m a string" # I" am a string
print(string4)

string5 = "I'm a string"
print(string5)

string6 = 'I\"m a string\nI\"m on a new line!'
print(string6)

string61 = "\\ \x41\x42\x43"
print(string61)

string7 = "aaaaaaaaaa"
print(string7)
 
string7 = "a" * 10
print(string7) # aaaaaaaaaa (same as above but cleaner)

print(len(string7)) # 10

print("string" in string4) # Result is True

print(string4.startswith("I")) # Result is True

print(string4.index("string")) # 6
print(string4.upper())

messy_string = "     Messy string!   "
print(messy_string)
print(messy_string.strip())

print(messy_string.replace("!","?").strip())
print(messy_string.replace("string", "example"))

print(messy_string.split())

messy_string = "Messy,string!"
print(messy_string.split(",")) # ['Messy', 'string!']

string4 = "I am a string" 
print(string4) 
print(string4.encode()) #b'I am a string'
print(string4.encode("utf-8")) #b'I am a string'

print(string4.rjust(25)) #            I am a string
print(string4.rjust(25, "X")) #XXXXXXXXXXXXI am a string

print("I am " + "a string")
print("String 4 is "+ str(len(string4)) + " character long") # String 4 is 13 character long
print(f"String 4 is {len(string4)} character long") # same as above but cleaner code

