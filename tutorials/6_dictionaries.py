# Woooo, on to tutorial number 6! 👏
# Throughout these tutorials, you've seen a whole bunch of data types:
# Strings, ints, floats, booleans and eventually lists.
# There are loads of different data types in Python, and we don't have the time to cover them all
# But we are going to look at Dictionaries specifically.

# Dictionaries 📖 are a really great way to store data about a single entity.
# Dictionaries are made up of key-value pairs. The key name is always on the left, and the value is on the right.
# Rather than using equals signs, we use colons for key-value pairs.
# Dictionaries use curly braces {} to hold their data.

# We can store any type as the value in a key-value pair - even lists and other dictionaries!
journalist = {
    "name": "Ann Author",
    "handle": "@an_author",
    "is_active_journalist": True,
    "total_articles": 72,
    "total_listicles": 128,
    "top_articles": ["Top 10 Dog Halloween Costumes", 
        "After I ghosted a man after several bad dates, I started seeing him everywhere.",
        "Your favorite iced summer coffee could contain 46 teaspoons of sugar — the same as drinking 5 cans of Coke"],
    "emergency_contact": { # A dictionary inside a dictionary is known as a nested dictionary!
        "name": "Matt Murdock",
        "phone": "(555)-212-3273",
        "email": "notdaredevil@marvel.com",
        "verified": True,
    }
}

# We can print out the whole dictionary...
print(journalist)

# We can also use a loop to print out the individual items...
for item in journalist:
    print(journalist[item])

# ... Or just pick a specific property to print. We use the key to get the value.
print(journalist["name"])
print(journalist["total_articles"])
print(journalist["top_articles"])

# QUESTION - How would we print a property inside the nested dictionary? Hint - more square brackets!

# QUESTION - What happens if you try to access a key that doesn't exist in the journalist dictionary?

# TASK - Now it's your turn to create your own dictionary! Create one with a few values - they can be any of the data types
# we've learned so far. Try printing out different values from your dictionary.
# As a bonus challenge, try adding the same key twice with different values. What do you notice about your dictionary?


# Now that you've made your own dictionary, let's look at and change the data in it.
# We can change the value the way we would normally set a variable.
journalist["name"] = "J. Jonah Jameson"
print(journalist["name"])

# If you don't want to use the square bracket way of getting the value, you can also use the get function:
print(journalist.get("total_listicles"))

# We can also add new key-value pairs...
journalist["awards_won"] = 2
print(journalist["awards_won"])

# ...And delete values we don't want using the pop() function
journalist.pop("handle")
print(journalist)

# If you don't want any elements at all in the dictionary - use the clear() function
journalist.clear()
print(journalist)

# QUESTION - Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print() # Put your code in here!