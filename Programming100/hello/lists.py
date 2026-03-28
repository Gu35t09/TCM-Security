# Lists - Have brackets [] - everything inside is called an item

movies = ["The Gorge", "BladeRunner 2049", "Ready Player One", "Fast & Furious"]

print(movies[1]) # Return the second item, because we start with 0

print(movies[1:3]) # Return "BladeRunner 2049", "Ready Player One"
print(movies[1:4]) # Return "BladeRunner 2049", "Ready Player One", "Fast & Furious"

print(movies[1:]) # Return 1 to end so "BladeRunner 2049", "Ready Player One", "Fast & Furious"
print(movies[:1]) # Return everything before item 1 so it return ['The Gorge']

print(movies[-1]) # Grab the last item of the list so Fast & Furious

print(len(movies)) # Count item in the list

movies.append("Mission Impossible")
print(movies[-1]) # Grab the last item of the list so Mission Impossbile 

movies.insert(2, "Wolf of Wallstreet") # Put on the 2 position
print(movies)
 
movies.pop(2) # Removes the 2 item on the list
print(movies)

friend_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + friend_movies # combine lists

print(our_favorite_movies)


# ----------------------------------------------------------------------

# Netsted lists
grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)

grades[0][1] = 83
print(grades)