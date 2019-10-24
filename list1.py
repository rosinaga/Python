list1 = ["Melipnos", "Meflipnos", "Albert Heijn", "Coolmanis", "Edvardas", "Bigness"]
print()

print("Default Print")
print(list1)
print()

print("Print First Element")
print(list1[0])
print()

print("Print Last Element")
print(list1[-1])
print()

print("Print Elements with  Numbers")

counter = 1
for elem in list1:
    print(counter, ":", elem)
    print(str(counter)+": "+ elem)
    print("{}:{}".format(counter, elem))
    counter = counter +1
print()
