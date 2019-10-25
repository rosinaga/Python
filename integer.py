import random
def randintlist(len, ceiling):
    list = []
    for i in range(len):
        number = random.randint(0, ceiling)
        list.append(number)
    return list

print(randintlist(5, 82))
