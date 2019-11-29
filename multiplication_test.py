import random

finish = False
while finish == False:
    ceiling = int(input("Give a ceiling value"))
    total = int(input("How many questions?"))

    a_values = []
    b_values = []
    questions = []
    userans = []
    answer = []
    score = 0
    def product():
        for i in range(total):
            a = random.randint(1,ceiling)
            b = random.randint(1,ceiling)
            a_values.append(str(a))
            b_values.append(str(b))
            questions.append("QUESTION " + str(i+1) + ") " + str(a) + " x " + str(b) + " = ?")
            answer.append("Q" + str(i+1) + ") " + str(a) + " x " + str(b) + " = " + str(a*b))
    product()


    for elem in questions:
        userans.append(int(input(elem)))
    score = 0
    for j in range(total):
        if (userans[j] == int(a_values[j])*int(b_values[j])):
            score = score + 1
            print(answer[j] + " the user answered " + str(userans[j]) + ". The answer was correct")
        elif (userans[j] != int(a_values[j])*int(b_values[j])):
            print(answer[j] + " the user answered " + str(userans[j]) + ". The answer was wrong")
    print(str(score) + "/" + str(total))


    end = input("Do you want to try again (yes/no)?")
    if (end != "yes"):
        finish = True
