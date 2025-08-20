#!/usr/bin/env python
# coding: utf-8

# # Python Basics: A Hands‑On Tutorial (Jupyter Notebook)
# 
# > Tip: Run a cell with **Shift+Enter**. Edit any cell and re-run to experiment.

# ## 1) Hello, Python
# 
# The classic first program is printing a message.

# In[ ]:


print("Hello, world!")


# ### Variables & Basic Types
# Python variables are created by assignment. Types are dynamic (no need to declare).
# 
# Common types:
# 
# - int:     integers (whole numbers, positive or negative)
# 
# - float:   floating point numbers (decimals) 64-bit double precision  
# 
# 
# - complex: complex numbers with real and imaginary parts
# 
# - str:     strings (text enclosed in quotes)
# 
# - bool:    boolean type, logical values (True/False)
# 
# Note: C or C++ have different float types
# 
#               float (32-bit, single precision)
#               double (64-bit, double precision)
#               long double (extened precision, depends on complier/architecture)

# In[ ]:


name = "Ada"
age = 31
height_m = 1.70
is_engineer = True

print(type(name), type(age), type(height_m), type(is_engineer))


# In[ ]:


import sys
print(sys.float_info)


# ### Type Conversion
# Convert between types with constructors: `int()`, `float()`, `str()`, `bool()`.

# In[ ]:


# Try converting string to float and integer
pi_str = "3.14159"
pi_f = float(pi_str)
pi_i = int(pi)

print(pi_str, pi_f, pi_i)
print(type(pi_str), type(pi_f), type(pi_i))


# Converting to integer always rounds off
pi_f = 3.99
pi_i = int(pi_f)
print(pi_f, pi_i)

# Reassign pi_i to the float value (pi_f) again
# (Note: this is not renaming, just assigning a new value)

pi_i = pi_f
print(pi_i, type(pi_i))

# Calculate the area of a circle with radius 2
radius = 2
area = pi * radius ** 2
area_str = str(area)
area, area_str
#"The area of a circle with radius " + str(radius) + " is " + area_str + "."


# ## 2) Strings
# Work with text using `str`. Common operations include slicing and methods.

# In[ ]:


# Define a string
s = "CP&E701 makes me happy"

# Slice: take characters from index 0 up to (but not including) 8
print(s[:8])

# Convert the string to all upper/lower case letters
print(s.upper())
print(s.lower())

# Replace a word ("happy") with another ("productive")
# -> "Python makes me productive"
print(s.replace("happy", "productive"))

# Split the string into a list of words (by default split on spaces)
# -> ["Python", "makes", "me", "happy"]
print("words:", s.split())

s2 = "Python<makes<me<happy"
print(s2.split("<"))

# Strings can be added up (concatenation)
a = "I am"
b = "Happy"
c = a + " " + b + "!"
print(c)   # I am Happy!



# f-string formatting: insert variables directly into a string
thing = "CP&E701"
why = "fun"
print(f"Learning {thing} is {why}!")

pi = 3.14159
print(f"Pi is approximately {pi:.2f}")


# ## 3) Numbers & Operators
# - Arithmetic: `+ - * / // % **`
# - Comparisons: `== != < <= > >=`
# - Logical: `and or not`

# In[ ]:


a = 7
b = 3

#a, b ,c = 7, 3, "good"

# Arithmetic operators
print("add:", a + b)        # addition -> 10
print("sub:", a - b)        # subtraction -> 4
print("mult:", a * b)       # multiplication -> 21
print("div:", a / b)        # true division -> 2.333...
print("floor div:", a // b) # floor division (rounds down) -> 2
print("floor div:", -a // b) # floor division (rounds down) -> 2
print("mod:", a % b)        # modulus (remainder) -> 1
print("power:", a ** b)     # exponentiation (7^3) -> 343

# Comparison operators
print("compare:", a > b, a == b)
# a > b -> True (7 > 3)
# a == b -> False (7 is not equal to 3)

# Logical operators
print("logic:", (a > 0) and (b > 0))
# (a > 0) -> True, (b > 0) -> True
# True and True -> True


# In[ ]:





# ## 4) Collections: Lists, Tuples, Sets, Dicts
# - **List**: ordered, mutable (can be changed after it is created)
# - **Tuple**: ordered, immutable (cannot be changed after it is created)
# - **Set**: unordered, unique items, mutable
# - **Dict**: key → value mapping, mutable

# In[ ]:


# List
nums = [10, 20, 30]
nums.append(40)
nums[1] = 22
print(nums, len(nums), nums)
#nums, len(nums), nums[-1]


# In[ ]:


# Tuple (immutable)
pt = (3, 4)
x, y = pt  # unpacking
print(pt, x, y)
#pt[0] = 5
#print(pt, x, y)


# In[ ]:


# Set (unique elements)
a = {1, 2, 3}
b = {3, 4, 5}

print (a | b)              # {1, 2, 3, 4, 5}
print (a.union(b))         # {1, 2, 3, 4, 5}

print (a & b)              # {3}
print (a.intersection(b))  # {3}

print (a - b )             # {1, 2}

print (a ^ b)              # {1, 2, 4, 5}
print (a.symmetric_difference(b))  # {1, 2, 4, 5}

a.add(10)
a.remove(1)
print(a)

# Sets are unordered collections, do not maintain an index
#a[0] = 2 will fail



# In[ ]:


# Dict (mapping) - dictionary stores key–value pairs
person = {"name": "Ada", "age": 31}

# Add a new key–value pair: key = "city", value = "London"
person["city"] = "London"

# Convert all key–value pairs into a list of tuples
# Example: [("name", "Ada"), ("age", 31), ("city", "London")]
print(list(person.items())  )

# Update the value for the key "city" to be a list instead of a string
# Now "city" -> ["London", "Lawrence"]
person["city"] = ["London", "Lawrence"]

# Safely retrieve the value of "city" (no error if key doesn't exist)
print(person.get("city"))   # Output: ["London", "Lawrence"]


# ## 5) Control Flow: `if`, `for`, `while`
# Use conditions and loops to control execution.

# In[ ]:


# If, else if, else

temperature_f = 82  # Fahrenheit

if temperature_f > 86:            # >30 °C
    status = "hot"
elif temperature_f >= 68:         # 20–30 °C
    status = "pleasant"
else:
    status = "cool"

print(status)


# In[ ]:


# for-loop
squares = [] # List
for n in range(5):
    squares.append(n*n)

print(squares)


# In[ ]:


n = 0
evens_under_10 = [] # define a list to store values

while True:        # infinite loop (must break manually)
    #n += 1         # increase n by 1 each time
    n = n + 1
    print(n)

    if n % 2 != 0: # if n is odd...
        print(f"{n} is odd number")
        continue  # skip the rest of the loop and go to next iteration

    print(f"{n} is even number")
    evens_under_10.append(n)   # only runs if n is even

    if n >= 10:    # stop condition
        break      # exit the loop completely

print(evens_under_10)


# ## 6) Functions
# Wrap reusable logic in functions. Use docstrings to explain behavior.

# In[ ]:


def greet(name):

    output="Hello, " + name + "!"

    return output

print(greet("CP&E 701"))        # Hello,
print(greet("world!"))          # Hello,

for people in ["Ada", "Grace", "Alan"]:
    print(greet(people))


# In[ ]:


def factorial(n: int) -> int:
    """Compute n! for n >= 0."""
    if n < 0:
        raise ValueError("n must be non-negative")   # factorial undefined for negatives
    result = 1

    for k in range(2, n+1):   # loop from 2 up to n
        result = result * k   # multiply result by k
        #result *= k
    return result

factorial(2)


# ## 7) Exceptions (Try/Except)
# Handle errors gracefully instead of crashing the program.

# In[ ]:


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')  # or handle another way

print(f"10/2 is {safe_divide(10, 2)}")
print(f"10/0 is {safe_divide(10, 0)}")


# ## 8) File I/O
# Read and write text files using context managers (`with`).

# In[ ]:


text_path = "example.txt"

# Writing to the file
with open(text_path, "w") as f:
    f.write("first line\nsecond line\n")

# Reading from the file
with open(text_path, "r") as f:
    content = f.read()

print(content)


# ## 9) Modules & Packages
# Use the standard library or third‑party packages (installed via `pip` or `conda`).

# In[ ]:


import math
values = [0, math.pi/6, math.pi/4, math.pi/2]
[math.sin(v) for v in values]


# ## 10) Bonus: List Comprehensions
# Pythonic ways to transform collections and create small anonymous functions.

# In[ ]:


# Create a list of numbers from 0 to 9
nums = list(range(10))

# List comprehension: multiply each number by 2
doubles = [n * 2 for n in nums]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# List comprehension with condition: include only even numbers
evens = [n for n in nums if n % 2 == 0]  # [0, 2, 4, 6, 8]

# Output the results
doubles, evens


# ---
# ### Appendix: Tips for Jupyter
# - **Shift+Enter** to run, **Esc** then **A/B** to insert cells above/below, **M/Y** to toggle Markdown/Code.
# - Restart kernel via the menu if things act weird.
# - Save your work often.
# - Convert notebook to python
# 
#       jupyter nbconvert --to script XXX.ipynb
# 
