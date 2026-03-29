set1 = {"a", "b", "c"}
print(set1) # the output change each time since set aren't ordered
print(type(set1))

# Can't do print(set1[0])

set2 = {"a", "a", "a"}
print(set2) # {'a'}
print(len(set2)) # 1

set3 = {"a", 1, 2.0}
print(set3)

set4 = set(("b", 1, False))
print(set4)

set1.add("d")
print(set1)

set3.update(set4)
print(set3)

list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

set = {4, 5, 6}
set6 = set4.union(set4)
print(set6)

set4.remove(4) # will give an error if the object 4 is not present
print(set4)

set4.discard(4) # as above but will skip if the object 4 is not present
print(set4)
