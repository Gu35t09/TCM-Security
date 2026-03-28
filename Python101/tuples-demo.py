# Immutable items
tuple_item = ("item1", "item2", "item3")
print(tuple_item)
print(type(tuple_item))

tuple_number = (1, 2, 3)
print(tuple_number)
print(type(tuple_number))

tuple_repeat = ('Combine!',) * 4
print(tuple_repeat)
print(type(tuple_repeat))

# Can't add item with tuple_item.append("item4")

# We can combine tuple
tuple_combained = tuple_item + tuple_number
print(tuple_combained) # ('item1', 'item2', 'item3', 1, 2, 3)
print(type(tuple_combained)) # Still <class 'tuple'>

# Check if something exists inside tuple
print("item2" in tuple_item) # True
print("item3" in tuple_number) # False

print(tuple_item.index("item2")) # 1
print(tuple_item[1]) # item2

print(tuple_item[-1]) # Last item, in this case item3
print(tuple_item[-2]) # Second last item, in this case item2 

print(tuple_item[0:2]) # Print 0 a 1 item --> ('item1', 'item2')
print(tuple_item[:2]) # same a above

string1 = "I am a string"
print(string1[:4]) # I am