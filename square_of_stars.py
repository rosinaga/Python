def starsquare(n):
    length = ""
    for j in range(n):
        length = length + "\n"
        for i in range(n):
            length = length + "* "
    return length

print(starsquare(20))
