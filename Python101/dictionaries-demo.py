dict1 = {"A": 1, "B":2, "C":3} 
print(dict1) # {'A': 1, 'B': 2, 'C': 3}
print(type(dict1))
print(len(dict1))

print(dict1["A"]) # 1
print(dict1.get("A")) # 1

print(dict1.keys()) # dict_keys(['A', 'B', 'C'])
print(dict1.values()) # dict_values([1, 2, 3])
print(dict1.items()) # dict_items([('A', 1), ('B', 2), ('C', 3)])

dict1["A"] = 1
print(dict1) # {'A': 1, 'B': 2, 'C': 3} --> remain the same since there can't be duplicates

dict1["D"] = 4 # but we can add key:value pair
print(dict1)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4}
 
dict1["A"] = 0 # we can also update values
print(dict1) # {'A': 0, 'B': 2, 'C': 3, 'D': 4}

dict1.update({"A":1}) # another method to update values
print(dict1) # {'A': 1, 'B': 2, 'C': 3, 'D': 4}

dict1.pop("D")
print(dict1) # {'A': 1, 'B': 2, 'C': 3}

del dict1["C"]
print(dict1) # {'A': 1, 'B': 2}