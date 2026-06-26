# Python Fundamentals Part 1
# Run using: python basics.py  or  python3 basics.py


# PYTHON VS JAVA - WHAT IS DIFFERENT (read this every time you switch languages)
#
# 1. No semicolons. Python ends lines with just a newline.
#    Java:   System.out.println("hi");
#    Python: print("hi")
#
# 2. No curly braces. Indentation defines blocks in Python.
#    Java uses {} for everything. Python uses whitespace. Get this wrong and you get errors.
#
# 3. No type declarations. Python figures out the type on its own.
#    Java:   int age = 19;
#    Python: age = 19
#
# 4. Naming convention is snake_case not camelCase.
#    Java:   firstName, studentGpa
#    Python: first_name, student_gpa
#
# 5. Logical operators are words not symbols.
#    Java:   && || !
#    Python: and  or  not
#
# 6. True and False are capitalized in Python.
#    Java:   true / false
#    Python: True / False
#
# 7. Division behaves differently.
#    In Python, / ALWAYS returns a float even if result is whole: 10 / 2 = 5.0
#    In Python, // is floor division (rounds down): 10 // 3 = 3, -7 // 2 = -4
#    In Java,   / between two ints gives int: 10 / 2 = 5, -7 / 2 = -3 (truncates toward zero)
#
# 8. Exponent is ** not Math.pow().
#    Java:   Math.pow(2, 3) = 8.0
#    Python: 2 ** 3 = 8
#
# 9. input() always returns a string. No exceptions.
#    Java scanner has nextInt(), nextDouble() which return the right type directly.
#    Python: you must manually wrap with int() or float() like int(input("Enter: "))
#
# 10. String + non-string throws an error in Python. Java handles it automatically.
#     Java:   "Age: " + 19  works fine
#     Python: "Age: " + 19  throws TypeError, you need str(19) or an f-string
#
# 11. Getting the ASCII value of a character:
#     Java:   (int) 'A'   (typecasting)
#     Python: ord('A')    (built-in function, don't try to typecast)
#
# 12. Python has truthy and falsy values. Java doesn't.
#     In Python: 0, "", [], None are all falsy. Everything else is truthy.
#     bool("hello") → True,  bool("") → False,  bool(0) → False
#     Java booleans are strictly true or false only.
#
# 13. No main method needed. Python runs top to bottom directly.


# PRINTING
print("Hello world")


# VARIABLES
# Python figures out the type for you, no need to declare int/String/double etc.
name = "geetansh"
age = 19
student_gpa = 3.5
is_above_18 = True


# ORD FUNCTION
# ord() returns the ASCII / Unicode value of a character
# don't use (int) typecasting like Java here, ord() is the Python way
a = "A"
print(ord(a))  # 65


# STRING CONCATENATION
# + works but you must convert non-strings manually with str()
print("Hi everyone, my name is " + name + ". I am " + str(age) + " years old.")

# using comma in print() just separates values with a space, no conversion needed
name2 = "yanika"
age2 = 18
print(name2, age2)

# f-strings are the cleanest way to do this (preferred modern approach)
print(f"Hi, my name is {name} and I am {age} years old.")


# BOOLEANS
bool_val = 5 > 7
print(bool_val)  # False

# checking types using type()
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(student_gpa))  # <class 'float'>
print(type(bool_val))  # <class 'bool'>


# USER INPUT
# input() always returns string no matter what the user types
# user_num1 = int(input("Enter the first number: "))
# user_num2 = int(input("Enter the second number: "))
# print(user_num1 + user_num2)

# use float(input()) if the user might enter a decimal
# int(input()) will crash if user types "3.5" because int("3.5") is invalid
# you'd need float(input()) first and then convert to int if needed


# ARITHMETIC OPERATORS
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...  always float in Python
print(a % b)  # 1    (remainder)
print(a**b)  # 1000 (exponent, Java equivalent is Math.pow(a, b))
print(a // b)  # 3    (floor division, covered below)


# RELATIONAL / COMPARISON OPERATORS (return boolean)
x = 15
y = 17
print(x > y)  # False
print(x < y)  # True
print(x >= y)  # False
print(x <= y)  # True
print(x == y)  # False
print(x != y)  # True


# ASSIGNMENT OPERATORS
a = 6
a += 1  # same as a = a + 1
print(a)  # 7

b = 12
b *= 2  # same as b = b * 2
print(b)  # 24


# LOGICAL OPERATORS
# Python uses words: not, and, or
# Java uses symbols: !, &&, ||
print(not is_above_18)  # False
print((3 < 8) and (5 > 3))  # True
print(False or False)  # False


# TRUTHY AND FALSY (Python only, no equivalent in Java)
# falsy: 0, 0.0, "", [], None
# truthy: anything that isn't falsy
print(bool(0))  # False
print(bool(""))  # False  (empty string is falsy, not True)
print(bool("hello"))  # True
print(bool(5))  # True


# OPERATOR PRECEDENCE (high to low)
# 1. ()          parentheses always go first
# 2. **          exponent (right to left: 2**3**2 = 2**9 not 8**2)
# 3. * / // %   multiplication and division (left to right)
# 4. + -         addition and subtraction (left to right)
# 5. < > <= >= == !=   comparisons
# 6. not
# 7. and
# 8. or
#
# quick tip: not beats and beats or, same as ! beats && beats || in Java


# FLOOR DIVISION
# // divides and rounds the result DOWN toward negative infinity
print(10 // 3)  # 3
print(7 // 2)  # 3
print(-7 // 2)  # -4  (Python floors down, not toward zero like Java)
# Java int division: -7 / 2 = -3 (truncates toward zero)
# Python floor division: -7 // 2 = -4 (goes further down)


# TYPE CONVERSION AND CASTING
# Python can automatically convert compatible types (int + float = float)
result = 5 + 2.5
print(result)  # 7.5

# manual casting using built-in functions
print(int(5.9))  # 5  (decimal just gets cut, not rounded)
print(float(5))  # 5.0
print(str(25))  # "25"
print(int("10"))  # 10
print(bool(0))  # False
print(bool("text"))  # True


# PRACTICE QUESTIONS

# Q1 - operator precedence
x = 2 + 3 * 4**2
print(x)  # 50  (4**2 = 16, 3*16 = 48, 48+2 = 50)

# Q2 - arithmetic precedence
y = 10 - 3 + 2 * 5
print(y)  # 17  (2*5=10, then left to right: 10-3=7, 7+10=17)

# Q3 - exponent precedence (right to left)
z = 4**2**2 + 10 // 3
print(z)  # 259  (2**2=4, 4**4=256, 10//3=3, 256+3=259)

# Q4 - logical operator precedence
a = not False and False or True
print(a)  # True  (not False = True, True and False = False, False or True = True)

# Q5 - combined comparison and logical
b = (5 + 3) * 2 > 10 and 4 * 2 == 8 or False
print(
    b
)  # True  (16>10 = True, 8==8 = True, True and True = True, True or False = True)

# Q6 - floor division
print(10 // 3)  # 3
print(-7 // 2)  # -4

# Q7 - assignment operators combined
a = 6
a += 1
b = 12
b *= 2
print(a + b)  # 31  (a=7, b=24)

# Q8 - / always returns float
print(10 / 2)  # 5.0 not 5, this is a common mistake coming from Java

# Q9 - program to find average of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
average = (num1 + num2) / 2
print("The average is:", average)
