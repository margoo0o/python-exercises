# Yay! You made it 💪🏻 Now onto the next piece of Python programming - loops!
# Programmers are pretty lazy and we don't want to have to repeat lines of code over and over again
# This is pretty inefficient...
import random


print("1")
print("2")
print("3")
print("4")
print("5")

# So we can use a loop to write the same code! We'll look at for loops first.
# for loops are made up of:
# the first line which tells us how many times to run the loop 
# the block of code to repeat

# Always start with the for keyword
# then define your iterator variable - this time we called it 'number'
# finally choose how long to run your loop for - we'll run it 5 times
for number in range(5):
    print(number)

# QUESTION - Do you notice anything different about the output from the print statements vs. the for loop?
# How do you think we might fix it?


# We can also create variables inside a for loop
for number in range(5):
    square_number = number ** 2
    print(str(square_number))

# The counter don't always have to go up the way, it can count down too:
# We can also add an 'else' statement to a for loop that runs once the countdown is done!
for countdown_number in range(10, 0, -1):
    print(countdown_number)
else:
    print("Blast off! 🚀")

# We don't have to use the counter variable in our code, though it can be useful.
for i in range(3):
    print("Welcome to Insider!")

# TASK - Write your own for loop and repeat something! It can be a print statement, a sum, whatever!


# BONUS CHALLENGE - Can you make a loop inside a loop? What happens when you do?


# Let's write a loop to print a triangle:
for i in range(6):
    print(i * '*')

# TASK - Can you make a loop that can print a different shape? How about a square or rectangle?


# Next, let's look at while loops. While loops are different from for loops, which are only repeated a set number of times.
# While loops run while a condition is true.
# They can be tricky, because we can easily run into infinite loops!
# We need to remember to add code in the while loop so that eventually, the condition isn't true
stop_number = 6
num = 0
while num < stop_number:
    print("I'm still working...")
    num+=1 # TASK - Remove this line of code - what happens?
print("I'm done!")

# We can also use boolean variables to control our while loop. Boolean variables can either be True or False.
is_story_published = False

while is_story_published == False:
    print("Still waiting on that story!")
    if random.randint(0,10) >= 8: # Here we're randomly generating a number between 0 and 10
        is_story_published = True # Once this is true, we stop the loop
print("The story's done!")

# TASK - Try writing your own while loop!


# Finally, let's look at lists. Lists are a great way to store lots of related items together.
# Instead of having to create lots of different variables, we can put them in one list.
# Lists can hold any data type.

lotto_numbers = [ 8, 13, 26, 29, 34, 44]
journalist_names = ["Ann Author", "Tamara Knight", "J Jonah Jameson", "Shanda Lear"]
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]

# QUESTION - Can different types be put in the same list? Try making your own list and see what happens!

# To access a specific item in a list, we use it's index. 
# The index number starts at 0 and goes up to but not including the length of the list.

# In this example there are 6 items in the list, so the indexes go from 0 to 5.
# INDEX                       0                1          2       3        4         5
insider_article_categories = ['politics', 'finance', 'beauty', 'news', 'travel', 'culture']

# The notation for accessing a specific item is to put the index in square brackets after the name of the list
first_item = insider_article_categories[0]
print(first_item)

last_item = insider_article_categories[5]
print(last_item)

# Uncomment this code!
# other_item = insider_article_categories[10]
# print(other_item) # QUESTION - What happens here? Why do you think the output is the way it is?

# In theory, we could use the square bracket notation above and go through each item of the list individually.
# OR... We could use loops!
# Loops over lists look slightly different. We still use a for loop, but we can say "for each item in the list, do something".
# Our code looks like this:
for category in insider_article_categories:
    print(category)

# TASK - Make your own list and loop over it. You don't have to print the variables - you could change them too!


# Finally let's combine our loops with if statements!
articles = ["Top 10 Headphones", "How to survive a Zombie Apocalypse", "Top 5 movies to watch on Netflix tonight",
    "Are Driverless cars the Future?"]
for article in articles:
    if article.find("Driverless") >= 0: # If the number is >= 0, it's in the string. If the number is -1 it's not in the string.
        print("Found the article: ", article)
    else:
        print(article, "isn't a match!")

# TASK - Time to make your own! Try and combine all the things we've learned so far - loops, if statements, and inputs!

# And voila! Now you've learned lists AND loops. Give yourself a pat on the back.