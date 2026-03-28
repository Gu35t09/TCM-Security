# Variables and methods

age = 22 # This is a variable, 35 is an object living on the age container
name = "Mattia" # string variable
gpa = "3.7" # float
print(age)
age = 23
print(int(age))
print(int(35.1))
print(int(35.9)) # It will not round


print('\n') 
qoute = "All is fair in love and war."
print(qoute)

# Method
# It's basically a function associated with an object 
print(qoute.upper())
print(qoute.lower())
print(qoute.title ())
print(len(qoute)) #count characters (all of them, even spaces and dot)


# Some other concatenation but with variables
print('\n') 
print("My name is " + name + ".")
print("My name is " + name + " and I am " + str(age) + " years old.")

birthday = 1
age += birthday

print(age)