a=input("Enter sentence: ")
b=a.rsplit()
c=set(b)
for i in c:
    print("Count of ", i, ":" , b.count(i))  