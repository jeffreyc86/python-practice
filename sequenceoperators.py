string1 = "he's "
string2 = "probably "
string3 = "rooting "
string4 = "for the "
string5 = "knicks"

print(string1 + string2 + string3 + string4 + string5)
# above is same as
print("he's " "probably " "rooting " "for the " "knicks ")

print("hello " * 5)
# hello hello hello hello hello

# print("Hello " * 5 + 4) - will error out
print("hello " * (5+4))
# hello hello hello hello hello hello hello hello hello
print("hello " * 5 + "4")
# hello hello hello hello hello 4

# check if substring is within string
today = "friday"

print("day" in today) #True
print("fri" in today) #True
print("thur" in today) #false