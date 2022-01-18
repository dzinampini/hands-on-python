a = input("Enter your sentence: ")
letters = digits = characters = 0
for i in a:
    if i.isalpha():
        letters=letters+1
    elif i.isdigit():
        digits=digits+1
    else:
        characters=characters+1

print("Number of letters: ", letters)
print("Number of digits: ", digits)
print("Number characters:", characters)