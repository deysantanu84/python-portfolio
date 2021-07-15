# https://realpython.com/python-f-strings/
import timeit  # For performance measurement

name = "Sandy"
age = 37

################################################
# %-formatting
################################################
print("Hello, %s. You are %s." % (name, age))

################################################
# str.format()
################################################
print("Hello, {}. You are {}.".format(name, age))  # str.format() with in-order positional arguments
print("Hello, {1}. You are {0}.".format(age, name))  # str.format() with indexed positional arguments

person = {'name': 'Billy', 'age': 38}  # dictionary
# str.format() with dictionary access to specified keys
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))
# str.format() with dictionary access with no keys specified
print("Hello, {name}. You are {age}.".format(**person))

# f-strings --- 3.6 onwards
# formatted string literals
# https://www.python.org/dev/peps/pep-0498/ --- Eric V. Smith <eric at trueblade.com>
print("Hello, {name}. You are {age}.")  # without f-string specifier
print(f"Hello, {name}. You are {age}.")  # Lower case f-string specifier
print(F"Hello, {name}. You are {age}.")  # Upper case F-string specifier
print(f"{2 * 37}")  # f-string specifier with mathematical calculation


def to_lowercase(inputString):
    return inputString.lower()


name = 'Sandy John'
print(f"{to_lowercase(name)} is funny.")  # user defined function call
print(f"{name.lower()} is funny.")  # built-in method call


################################################
# Class objects
################################################
class Programmer:
    def __init__(self, first_name, last_name, person_age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = person_age

    # string returned by __str__() is the informal string representation of an object and should be readable
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    # string returned by __repr__() is the official representation and should be unambiguous
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"


new_object = Programmer("Sandy", "Bean", "37")
print(f"{new_object}")  # __str__()
print(f"{new_object!r}")  # __repr__()

################################################
# Multiline f-strings
################################################
name = "Sandy"
profession = "programmer"
affiliation = "Monty Python"

# f-string specifier in each line
message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)
print(message)

# f-string specifier in only one line
message = (
    f"Hi {name}. "
    "You are a {profession}. "
    "You were in {affiliation}."
)
print(message)

# Line breaks
message = f"Hi {name}. " \
          f"You are a {profession}. " \
          f"You were in {affiliation}."
print(message)

# Multiline f-string specifier within triple quotes
message = f"""
     Hi {name}.
     You are a {profession}.
     You were in {affiliation}.
"""
print(message)

# Refer indentation guidelines: https://pep8.org/
# f-strings are faster than both %-formatting and str.format()
# f-strings are evaluated at runtime rather than constant values

################################################
# Speed comparison
################################################
# Performance of %-formatting
print(timeit.timeit("""
name = "Sandy"
age = 37
'%s is %s.' % (name, age)
""", number=10000))

# Performance of str.format()
print(timeit.timeit("""
name = "Sandy"
age = 37
'{} is {}.'.format(name, age)
""", number=10000))

# Performance of f-string
print(timeit.timeit("""
name = "Sandy"
age = 37
f'{name} is {age}.'
""", number=10000))

# Quotation Marks
print(f"{'Sandy John'}")  # Double quotes around f-string
print(f'{"Sandy John"}')  # Single quotes around f-string
print(f"""Sandy John""")  # Triple (double) quotes
print(f'''Sandy John''')  # Triple (single) quotes
print(f"The \"programmer\" is {name}, aged {age}.")  # Escaping quotes
programmer = {'name': 'Sandy John', 'age': 37}
print(f"The programmer is {programmer['name']}, aged {programmer['age']}.")  # Quotes around dictionary

################################################
# Braces
################################################
print(f"{{70 + 4}}")  # Double braces
print(f"{{{70 + 4}}}")  # Triple braces
print(f"{{{{70 + 4}}}}")  # More than triple braces

################################################
# Backslashes
################################################
# Can use backslashes to escape only in the string portion of an f-string
# Cannot use backslashes to escape in the expression part of an f-string
# To overcome, evaluate the expression beforehand and use the result in f-string
print(f"{name}")

# f-string expressions should not include comments using the #-symbol - SyntaxError
# Refer https://www.python.org/dev/peps/pep-0502/ (rejected) for an extended discussion on string interpolation
# Future of f-string: refer https://www.python.org/dev/peps/pep-0536/ (draft)
