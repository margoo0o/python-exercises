# Welcome to your first Python program! 👋🏻
# For a lot of programming languages, the very first program a 
# developer will make is called "Hello World". It lets us know 
# everything is working as expected. We usually do that by printing "Hello World".
print("Hello World!")

# In Python we can use variables. In code, a variable holds some bit of data. It can
# be a string (characters in quotes), integers aka ints (whole numbers), floats (decimal numbers)
# and a whole bunch of other things!
name = "Peter Parker"
age = 18
height = 170.18
is_spiderman = True

# Let's print out the details. We can use string concatenation to put our variables into sentences
# NOTE: We need to convert numbers and booleans into strings to use them in strings, use the str() function
print("Hi, my name is " + name + " and I'm " + str(age) + " years old.")
print("Peter Parker height: ", height)
print("Is Peter Parker Spiderman?:" + str(is_spiderman))

# We can also override any of these variables if we want to.
is_spiderman = False
print("Is Peter Parker Spiderman?:" + str(is_spiderman))

# To print over multiple lines - use the print function multiple times, or use \n - it's a shortcut for 'new line'
print("Hello\nThere!\n")

# TASK - Over to you now! Create some new variables, or overwrite the existing ones!

# TASK - Print out your variables! Try using string concatenation to put them into a sentence!

# QUESTION - What happens if you leave the speech marks out of the print() statement? Do you see any errors? What do
# you think they mean?



# We can also perform mathematical operations in our code - don't forget we have to convert our numbers to strings!
print(str(10 + 64))
print(str(1040 - 1050))
print(str(50 * 17)) # multiplication
print(str(579 / 13)) # division

# NOTE: The division (/) up above uses float division. That means your answer can have decimal points.
# To do integer division, which removes the decimal points, use //
num1 = 1694
num2 = 13
print(str(num1 // num2)) # No decimal points
print(str(num1 / num2)) # Decimal points!

# QUESTION - What happens if we add two strings together? What does it do? Try making two string variables and adding them together

# QUESTION - What happens if you divide by 0? Is there an error? What does it mean?

# TASK - We've looked at addition, subtraction, multiplication and division. Can you figure out what these equations are doing?
num3 = 13
num4 = 2
print(num3 ** num4)

num5 = 17
num6 = 6
print(num5 % num6)