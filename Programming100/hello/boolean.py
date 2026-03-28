def nl(): #new line
    print('\n')

# Boolean Expressions (True of False)

bool1 = True
bool2 = 3*3 == 9 # This is going to be true
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
# True, True, False, False

print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

# Relational and Boolean Operators

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7
equals = 7 == 7
not_equals = 7 != 8

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) # True
test_not = not True #False