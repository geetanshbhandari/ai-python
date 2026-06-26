# Question 1 - Take the user's name and age as input and display a greeting message

person_name = input("Enter your name: ")
person_age = int(input("Enter your age: "))
print("Hello " + person_name + ", you are " + str(person_age) + " years old!")


# Question 2 - Take two numbers as input and display their sum, difference, product, and quotient

first_value = float(input("Enter the first number: "))
second_value = float(input("Enter the second number: "))
print("The sum of the two numbers entered by you is:", (first_value + second_value))
print(
    "The difference of the two numbers entered by you is:", (first_value - second_value)
)
print("The product of the two numbers entered by you is:", (first_value * second_value))
print(
    "The quotient of the two numbers entered by you is:", (first_value / second_value)
)


# Question 3 - Take three numbers as input and calculate their average

score_a = float(input("Kindly enter your first number: "))
score_b = float(input("Kindly enter your second number: "))
score_c = float(input("Kindly enter your third number (can be a decimal): "))

average_score = (score_a + score_b + score_c) / 3
print("The average of the three numbers is:", average_score)


# Question 4 - Take an integer as input and demonstrate type conversion to float and then to string

input_value = int(input("Enter an integer of your choice: "))
print(input_value, type(input_value))
input_value = float(input_value)
print(input_value, type(input_value))
input_value = str(input_value)
print(input_value, type(input_value))


# Question 5 - Evaluate and print the result of the expression: 10 + 3 * 2**2

expression_result = 10 + 3 * 2**2
print(expression_result)  # Result is 22 — Python applies ** first, then *, then +


# Question 6 - Swap two numbers entered by the user using a temporary variable

original_first = int(input("Enter your first number: "))
original_second = int(input("Enter your second number: "))

temp_holder = original_first
original_first = original_second
original_second = temp_holder

print("The new value of first number:", original_first)
print("The new value of second number:", original_second)

# NOTE: Python also supports one-line swapping without a temp variable:
# original_first, original_second = original_second, original_first
# Java always requires a temp variable — Python's tuple unpacking makes it much cleaner


# Question 7 - Convert a temperature value from Celsius to Fahrenheit

celsius_input = float(input("Kindly enter the temperature in degrees Celsius: "))
fahrenheit_result = (celsius_input * (9 / 5)) + 32
print("The temperature in Fahrenheit would be:", fahrenheit_result)


# Question 8 - Calculate the area of a circle given its radius

radius_input = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * radius_input**2
print("The area of the circle with the above radius would be:", area_of_circle)


# Question 9 - Calculate simple interest given principal amount, rate of interest, and time

principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the interest rate (in %): "))
time_in_years = float(input("Enter the total duration (in years): "))

calculated_interest = (principal * annual_rate * time_in_years) / 100
print("The simple interest would be:", calculated_interest)


# Question 10 - Separate and display the integer and fractional parts of a decimal number

decimal_number = float(input("Kindly enter a decimal number of your choice: "))
integer_part = int(decimal_number)
fractional_part = decimal_number - integer_part

print("The integer part is:", integer_part)
print("The fractional part is:", fractional_part)

# NOTE: Floating point precision may show extra decimals (e.g. 45.78 - 45 = 0.7799999999999994)
# This is not a mistake — it's how floats are stored internally. Use round() to fix once learned.
