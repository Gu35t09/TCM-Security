# Conditional Statements - if/else

def nl(): #new line
    print('\n')

def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "No drink for you!"
    
print(drink(3))
print(drink(1))

def alcohol(age, money):
    if (age >= 18) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 18) and (money < 5):
        return "Come back with more money."
    elif (age < 18) and (money >= 5):
        return  "Nice try, kid!"
    else:
        return "You're too young and too poor!!!"

print(alcohol(18,5))
print(alcohol(18,4))
print(alcohol(17,5))
print(alcohol(17,4))