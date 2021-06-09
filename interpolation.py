age = 29
print("My age is %d years old" % age)
#My age is 29 years old

# the order of string interpolation is important
major = "years"
minor = "months"
print("My age is %d %s, %d %s old" % (age, major, 10, minor))
# My age is 29 years, 10 months old

print("Pi is approximately %f" % (22/7))
# Pi is approximately 3.142857
print("Pi is approximately %1.10f" % (22/7))
# Pi is approximately 3.1428571429