# Yay! The first exercise is over! Amazing! Now on to some slightly more complicated bits.

# We already looked at some basic arithmetic. We can also do comparisons of different variables.
# Normally in maths we would compare numbers, but in Python we can also compare strings, booleans and even objects.

# In the previous exercise, we set variables using the = sign. The variable name is on the left and the value is on the right.
my_variable = "This is the value of my variable."

# To compare two values, we use two equals signs together, ==. The comparison generates a boolean value, which we can use in our code.
# If the comparison is true, the boolean output is True. Otherwise it's false.
number1 = 5
number2 = 5
number3 = 10

print(number1 == number2) # True
print(number2 == number3) # False

# We can also check if two values are not equal, using !=

print(number1 != number3) # True
print(number1 != number2) # False

# As we said, we can also compare other types of variables such as strings! We use the same format
print("Avocado" == "Avocado")
print("Frog" == "Toad")
print("Something123" != "Something123")
print("Another" != "Thing")

# QUESTION - Will these comparisons be True or False?
print("pineapples" == "PineAPples")
print("supersecretpassword" == "SUPERSECRETPASSWORD")

# We can also use more complex comparison operators, similar to what we use in maths.
# These include: 
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

# QUESTION: What boolean value will these comparisons give?
print(5 > 3)
print(10 < 10)
print(1000 >= 764)
print(-10 <= 0) 
print(0.00001 <= 0)
print(1989 >= 1993)

# We can also compare strings using these operators. Strings are compared alphabetically!
print("business insider" < "insider")
print("aardvark" > "zebra")
print("insider" >= "insider")

# QUESTION - What happens if you compare two different types of variables?
# Think about the different types you've seen so far - strings, bools, floats and ints


# TASK - Try comparing some different values. Are the outcomes what you expected?


# Each of these comparisons generates a boolean value - True if the comparison is true, otherwise it's False.
# We can also make boolean expressions using AND, OR and NOT comparisons.
# Try changing the values of the first two booleans - what do you notice?
has_interview_happened = True
has_article_been_proofchecked = True
is_article_ready = has_interview_happened and has_interview_happened

print("Is the article ready? ", is_article_ready)

# When we do an AND comparison, BOTH of the values have to be True for the final boolean value to be True.
# Otherwise, the outcome is False.
#       | True  | False
# ______|_______|________
# True  | T     | F
# ------|-------|--------
# False | F     | F

# The other type of check is OR. For the final boolean to be True, only one of the values has to be True.
# Try changing the values of the first two booleans, what do you notice?
is_student = True
has_loyalty_card = False
is_discount_applied = is_student or has_loyalty_card

print("Does the order get a discount? ", is_discount_applied)

# When we do an OR comparison, ONE of the values have to be True for the final boolean value to be True.
# Otherwise, the outcome is False.
#       | True  | False
# ______|_______|________
# True  | T     | F
# ------|-------|--------
# False | T     | F

# Finally, we can also negate a Boolean. This means we look for the opposite value - Not True or Not False.
# We use the not keyword for this! We can use not on it's own or combine it with AND and OR operators
is_raining = input("Is it raining? ")
is_weather_good = not is_raining

print("Is the weather good? ", is_weather_good)

has_won_lottery = False
is_under_65 = True
can_i_retire = has_won_lottery and not is_under_65

print("Can I retire yet? ", can_i_retire)

# Up until now we've only compared two things at a time, but we can do multiple comparisons at once
holiday_budget = 100
deposit_cost = 101
jetski_booked = False
flights_booked = True

# We can only go on our hols if the flights are booked AND we have enough money OR we already booked the jetski package
is_holiday_ready = flights_booked and (holiday_budget >= deposit_cost or jetski_booked)

print("Can I go on holiday yet? ", is_holiday_ready)

# So what's the point of doing all these comparisons? 🤔
# We can use comparisons and that might generate different outcomes based on data to guide the users through our code.
# This is known as decision-based logic.
# This means we take a different path through the code based depending on the variables.

# QUESTION - What is the output of this code? How would you change it to run the other path?
no_of_veggies = 2
if no_of_veggies >= 5:
    print("You are super healthy! 🥦")
else:
    print("Don't forget to eat at least 5 fruit and veggies a day! 🍫")

# The piece of code above is an IF/ELSE statement. We always start with the IF statement - the condition
# on this line must be True to enter the code block below. Otherwise, it enters the code block underneath
# the ELSE statement. Think of else as a catch-all!

# We can also write ELSE-IF statements. In these statements, we might check if a different condition is True
# This means we can have lots of different paths through our code!
# Try changing the month to see the different paths.

# QUESTION + TASK - What happens when you type in a month that doesn't exist? What happens if you use all capital letters
# or all lowercase letters in current_month?
current_month = input("What month is it?")

if current_month == "March" or current_month == "April" or current_month == "May":
    print("It's Spring! 🌸🌼🍃")
elif current_month == "June" or current_month == "July" or current_month == "August":
    print("It's Summer time! ☀️🏖️")
elif current_month == "September" or current_month == "October" or current_month == "November":
    print("It's Autumn! 🍁🍂🎃")
elif current_month == "December" or current_month == "January" or current_month == "February":
    print("It's Winter! ❄️☃️🎄")

# TASK - Write an if/elif/else statement to help me decide what to make for dinner.
# The boolean variables below indicate what ingredients I have. Based on what I do or don't have,
# Suggest a recipe! Change the boolean variables so that you can check each flow of code.
# BONUS TASK - Can you update the code so that instead of having hardcoded variables, we get the user input?
has_carbs = True
has_veggies = False
has_protein = False