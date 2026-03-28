# Dictionaries - key/values pairs - {}

drinks = {"White Russian": 8, "Old Fashioned": 12, "Lemon Drop": 5} # The drink is the key the price is the value
print(drinks)

# Dictionaries with list ad key values
employess = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employess)

employess['Legal'] = ["Mr. Frond"] # Add a new key values pair
print(employess)

employess.update({"Sales": ["Andie", "Ollie"]}) # Also add a new key values pair
print(employess)

drinks['White Russian'] = 9 # modify our value
print(drinks)

print(drinks.get("White Russian"))