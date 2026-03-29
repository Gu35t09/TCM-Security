list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

list2 = ["A", 1 ,2.0, ["A", "B"], [], list(), ("A"), False]
print(list2)
print(type(list2))

print(list1[0])
print(list1[-1])

print(list2[3][0]) # A
print(list2[3][-1]) # B

list1[0] = "X"
print(list1)

del list1[0]
print(list1)

# Method 1 to add a value
list1.insert(0, "A")
print(list1)

# Method 2 to add a value
list1 = ["A"] + list1
print(list1)

print(max(list1)) # F
print(min(list1)) # A

print(list1.index("C")) # 3
print(list1[list1.index("C")]) # C

# Method 1 to reverse a list
list1.reverse()
print(list1)

# Method 2 to reverse a list
list1 = list1[::-1]
print(list1)

print(list1.count("A"))

list1.pop()
print(list1)

list3 = ["H", "I", "J"]
print(list3)

list1.extend(list3)
print(list1)

list1.clear()
print(list1)

# Sorting list

list4 = [8, 12, 5, 6, 17, 2]
print(list4)

list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)


# List copy

list5 = list4
print(list4)
print(list5)

list5[2] = "X"
print(list5) # list5 now container X on the 2 position --> [17, 12, 'X', 6, 5, 2]
print(list4) # list4 also changed, but list5 = list4 just point list5 to list4 (it's not a copy)


# How to make a real copy

list6 = list4.copy()
print(list4)
print(list6)

list6[2] = "A"
print(list4) # [17, 12, 'X', 6, 5, 2]
print(list6) # [17, 12, 'A', 6, 5, 2]

# Map function
list7 = ["1", "2", "3"]
print(list7)

list8 = list(map(float, list7)) # take each item of the list and applied the float function
print(list8) # [1.0, 2.0, 3.0]



