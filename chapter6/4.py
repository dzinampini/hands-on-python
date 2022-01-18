word = input("Enter the string:")
a1 = list(word)
b1 = []
i1 = len(a1) - 1

while i1 >= 0:
    b1.append(a1[i1])
    i1 = i1 - 1
k1 = "".join(b1)
print("Reversed string", k1)

import numpy as np

a1np = np.array(a1)
b1np = np.array(b1)

if all(a1np == b1np):
    print("Given string:", word, "is a PALINDROME")
else:
    print("Given string is not a palindrome")
