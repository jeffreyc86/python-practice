print('Today is a good day to learn Python')
print("Python is fun")
print("Python strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")

greeting = "Hello"
name = input("Please enter your name ")

# notes are written with #
print(greeting + " " + name)

# using f strings to string interpolate - simply put an f before the string that has interpolation
name = "Jeffrey"
age = 29
print(name + f" is {age} years old")
# Jeffrey is 29 years old

print(f"Pi is approximately {22/7:3.8f}")