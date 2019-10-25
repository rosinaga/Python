import random
def randlist(len,ceiling):
    list = []
    for i in range(len):
        number = random.randint(0, ceiling)
        list.append(number)
    return list

#testing
print(randlist(5,20))
