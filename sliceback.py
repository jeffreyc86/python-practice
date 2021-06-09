letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)    #zyxwvutsrqponmlkjihgfedcb

backwards = letters[25:-1:-1]
print(backwards)    #empty string

backwards = letters[25::-1]
print(backwards)    #zyxwvutsrqponmlkjihgfedcba

backwards = letters[::-1]  #python idiom to reverse a sequence
print(backwards)    #zyxwvutsrqponmlkjihgfedcba

print(letters[16:13:-1])    #qpo
print(letters[4::-1])    #edcba
print(letters[25:17:-1]) #zyxwvuts

#idiom to get the end of a sequence - slice with a negative first value and no second value
print(letters[-4:])    #wxyz

#idiom to get first few items in a sequence - slice without a first value and a positive second value
print(letters[:5])  #abcde

