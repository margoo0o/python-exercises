# Alright! You're nearly a Python expert now. We've covered a lot so give yourself a pat on the back
# for all the amazing work you've put in so far!

# So far, each file has been a pretty standard Python file. Python files run the code from top to bottom.
# So the first line runs, then the second, and so on until it reaches the end.
# If the runner encounters an error, it stops at that point - it doesn't skip the code.
# This is fine - but what if we have code we want to write, but not run til later in the code?
# Enter - functions!

# We already discussed how lazy software engineers are. We don't want to repeat ourselves, but code can be repetitive.
# We can put repetitive or useful code inside a function, and call it when we want.
# functions always start with the 'def' keyword, followed by the name of the function, brackets and a colon.
# Like loops and conditional statements, the code inside the function is indented.
def say_hello():
    print("This is the code inside the say_hello function")
print("Now this is the code running outside the function!")

# You'll notice when you run the code above, only the statement outside the function is printed. So how do you call a function?
# To call a function, specify the function name, followed by the brackets (we'll talk more about the brackets in a bit!)
say_hello()

# TASK - Make your own function! It can do whatever you want - maybe it prints something or does a calculation and shows the result.
# Don't forget to call your function to make sure it works!

# We use functions to avoid repetition, and also minimise change. If we reference our function and need to change it's behaviour,
# we only have to do it inside the function, and the behaviour change happens everywhere the function is called.

# We can also pass arguments to a function. An argument is a variable that we send to the function when we call it.
# This means we don't have to hardcode data, so our code is more flexible!
def greetings_name(name):
    print(f"Hello {name}! 👋🏻 You're nearly done all these tutorials!")

# This time when we call the function, we pass an argument to the function
greetings_name("Ringo")
greetings_name("John")
greetings_name("George")
greetings_name("Paul")

# TASK - call the greetings_name() function yourself and pass in a different argument!
# Bonus points if you use input() to get the user's input.


# QUESTION - What happens if we don't pass any arguments, but the function expects one?

# We can have multiple arguments, which we split up with commas
# We can also return a value from a function. Rather than printing to get our value,
# We can do some calculations inside a function, return the result, and then use it later.
def calculate_monthly_bills(rent, groceries, tv_subscriptions):
    return rent + groceries + tv_subscriptions

total_money = 1200
total_costs = calculate_monthly_bills(600, 200, 40)
if total_costs < total_money:
    print("We have enough money this month!")
else:
    print("Uh oh, we're broke 😬")


# Finally, we can also have default parameters. This means if a value isn't supplied, the function will fallback to the default
def my_home_country(country = "the UK"):
    print("I am from " + country)

my_home_country("France")
my_home_country("Germany")
my_home_country()