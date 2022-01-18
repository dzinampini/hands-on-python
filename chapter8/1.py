import random

i = 0
p = []

q = int(input("Enter the first cap:"))
x = int(input("Enter the second cap:"))

while i < 10:
    c = random.randint(q, x)
    b = list(str(c))
    p.append(b)
    i = i + 1

print(p)

k = 0
n = []
while k < len(p):
    n.append(int("".join(p[k])))
    k = k + 1
print(n)

f = sorted(n)
print("Sorted", f)

g = set(f)
l = list(g)
o = 0
while o < len(l):
    if l[o] < l[len(l) - 1]:
        print(l[o], "is lower than ", l[len(l) - 1])
    o = o + 1
print("Max number of the random list is:", l[len(l) - 1])
