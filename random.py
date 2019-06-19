import random
chars='abcdefghABCDEFGH'
length=int(input("Enter the length of the password:\n"))
cnt=int(input("Enter the number of passwords you want?"))
for p in range(cnt):
    pas=' '
    for c in range(length):
        pas=pas+random.choice(chars)
    print(pas)
