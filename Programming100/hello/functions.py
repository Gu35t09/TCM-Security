# Functions - Reusable block of code (like a mini program)

# Version 1
def who_am_i():
    name = "Mattia" # Local variable of this function, it doesn't exist outsite
    age = 23
    print(f"My name is {name} and I am {age} years old") # Better way of concatenating

who_am_i()

# Version 2
def who_am_i(name, age):
    print(f"My name is {name} and I am {age} years old") # Better way of concatenating

who_am_i("Mattia",23)

# Version 3
#def who_am_i(name, age):
#    print(f"My name is {name} and I am {age} years old") # Better way of concatenating

#input_name = input("What is your name? ")
#input_age = int(input("How old are you? "))
#who_am_i(input_name, input_age)

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

print(multiply(7,7))

result2=(multiply(8,8))
print(result2)


def square_root(x):
    print(x ** .5)

square_root(64)

def nl(): #new line
    print('\n')

nl()