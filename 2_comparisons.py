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
print(0 <= 0)
print(1989 >= 1993)

# We can also compare strings using these operators. Strings are compared alphabetically!
print("business insider" < "insider")
print("aardvark" > "zebra")
print("insider" >= "insider")

# TODO: If statements