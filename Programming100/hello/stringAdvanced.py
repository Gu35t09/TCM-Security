# Advanced Strings

my_name = "Mattia"
print(my_name[0]) # First letter of the name
print(my_name[-1]) # Last letter

sentence = "This is a sentence"
print(sentence[:4])

print(sentence.split()) #delimiter - default is space

sentence_split = sentence.split() # split each word separeted by space
sentence_join = '-'.join(sentence_split) # put a - after each word
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)

quote2 = "He said, \"give me all your money\""
print(quote2)

too_much_space = "                                 hello               "
print(too_much_space.strip()) # default is space, but we can remove commas for example

print("A" in "Apple") # return True
print("a" in "Apple") # return False, it is case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

#user_input = input("Enter yes or no: ").lower().strip()
#if user_input == "yes":
#    print("You agree!")
#else:
#    print("You disagree!")

movie = "The Gorge"
print("My favorite movie is {}.".format(movie)) 
print("My favorite movie is %s." % movie)
print(f"My favorite movie is {movie}") # This is the best in my opinion