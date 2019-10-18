def stars1(n):
    for i in range(5):
        print("*")
        return ""

#print(stars1(5))

def stars_in_line(n):
    stars = ""
    for i in range(5):
        stars = stars + "*"
    return stars

print(stars_in_line(5))
