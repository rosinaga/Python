import random
ceiling = int(input("Give a maximum value"))
print("")

def product(a,b):
    return a*b

a = random.randint(1, ceiling)
b = random.randint(1, ceiling)

answer = int(input("What is the product of " + str(a) + " and " + str(b)))
if (answer != product(a,b)):
   print("Wrong")
elif (answer == product(a,b)):
    print("Right")
