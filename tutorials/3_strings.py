# On to the the next tutorial! We did a lot of comparisons in the last exercise, which led to if/else statements.
# This tutorial is about manipulating strings!
# Strings are letters, characters, numbers and symbols - we can tell if a variable is a string because the value is in quote marks
this_is_a_string = "1"
this_isnt_a_string = 1

# Even though the "value" looks the same, these variables aren't equal because they have different data types
print(this_is_a_string == this_isnt_a_string)

# Python gives us lots of handy functions to quickly manipulate strings. For example, we can make strings all caps or all lowercase.
print("lord of the rings: the two towers".upper())
print("Lord of the Rings: The Fellowship of the Ring".lower())
print("LORD OF THE RINGS: RETURN OF THE KING".title()) # capitilize the first letter of every word

# TASK - try printing your own strings, using some of the string functions!

# QUESTION - what does string.capitalize() do?

# There are also functions we can use to check if a string can be converted to another type. 
# Most of these functions start with "is"
viewer_count = "323786"
print(viewer_count.isdigit())

word_count = "Two thousand and thirty-nine"
print(word_count.isdigit())

# Once we know if a variable can be converted to a type, we can convert it!
total_cost = "3299"
print(type(total_cost))
if total_cost.isnumeric():
    total_cost = float(total_cost)
    print(type(total_cost))
    print(total_cost)

# There are tons of other really interesting string functions!
# We can count the number of times a word appears in a string...
news_article = "Disney's first ship, the Magic, set sail back in 1998, so embarking on the Wish, which had its maiden voyage in July 2022, was quite the upgrade. \
Passengers are immersed in everything new and dazzling on the Wish as soon as they enter the Grand Hall.\
The other Disney ships have a central atrium where guests embark and are welcomed aboard. But the Wish's Grand Hall is open and airy — more of a multipurpose space with a stage and balcony. \
The Disney Wish is the fleet's first Triton Class ship, meaning it has a different layout from Disney's previous ships in the Magic and Dream classes. \
After three sailings on the Wonder, two on the Magic, and two on the Dream, we had those deck plans down pat."

print("Number of times Disney is mentioned:", news_article.count("Disney"))
print("Number of times ship is mentioned:", news_article.count("ship"))

# We can replace words or characters in a string...
movie_article= "Greta Gerwig's 'Barbie' and Christopher Nolan's 'Oppenheimer' are releasing on the same day in theaters in an event that's become known as 'Barbenheimer' online, but it's not the first time two big-budget studio films have been released on the same day. \
This isn't even Nolan's first time as part of a big summer-film showdown. \
There are only so many release dates per year and, sometimes, it's perfect for counter-programming. \
Universal Pictures and Warner Bros. previously battled at the box office 15 years ago when Universal's film, 'Mamma Mia!' went up against Nolan's critically beloved film, 'The Dark Knight' in July 2008."

print(movie_article.replace("film", "movie"))

# We can also remove spaces from a string at the start and the end using strip()
password = "    mySuperSecretPassword   "
print(password.strip())

# We can get subsections of a string using slices.
# Slices can take up to 3 numbers - the starting position, the end position and the step size
headline = "A man who survived jumping off the 1,083-foot-tall Eiffel Tower with a parachute now faces criminal charges"

print(headline[:]) # make a slice that goes from the start of the slice to the end
print(headline[51:63]) # get a subsection of the string
print(headline[::-1]) # reverse the whole string

# Finally, we can also split a string. When you split a string, it puts each item into a list (we'll go into more detail on
# lists later on)
# The split() function uses a delimiter. This is a character or word which lets Python know where to split the string
movie_quote = "My name is Inigo Montoya. You killed my father. Prepare to die."

print(movie_quote.split(".")) # Split each sentence
print(movie_quote.lower().split("my")) # make whole sentence lower case then split by letter. This is also an example of chaining functions!

# TASK - PALINDROME CHECKER!
# Below is a variable which takes a user's important. 
# Your goal is to create a piece of code that checks if what the user enters is a Palindrome!
# As a refresher, a palindrome is a string that is the same reversed as it is normally.
# Bonus points if you can get your code to ignore spaces, capital letters and punctuation!
# Some examples:
# - "racecar"
# - "kayak"
# - "A man, a plan, a canal - Panama"
# - "Taco cat"

user_string = input("Enter your word/phrase: ")

# HINT: use the string functions shown above to reverse your string!

# if is_palindrome:
#     print("Your string is a palindrome!")
# else:
#     print("Sorry, not a palindrome")