list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

list2 = [x for x in list1]
print(list2) # ['A', 'B', 'C', 'D', 'E', 'F']

list3 = [x for x in list1 if x == "A"] 
print(list3) # ['A']

list4 = [x for x in range(4)] 
print(list4) # [0, 1, 2, 3]

