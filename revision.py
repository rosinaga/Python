import random

finish = False
while finish == False:
    ceiling = int(input("Give a ceiling intiger"))
    number = int(input("How many questions?"))

    a_values = []
    b_values = []
    questions = []
    userans = []
    answers = []
    score = 0
    def product():
        for i in range(number):
            a = random.randint(1, ceiling)
            b = random.randint(1, ceiling)
            a_values.append(str(a))
            b_values.append(str(b))
            questions.append("Question " + str(i+1) + "/" + str(number) + ": " + str(a) + " x " + str(b) + " = ?")
            answers.append("Q" + str(i+1) + ") " + str(a) + " x " + str(b) + " =" + str(a*b))
    product()

    for elem in questions:
        userans.append(int(input(elem)))

    for j in range(number):
        if (userans[j] == int(a_values[j])*int(b_values[j])):
            score = score + 1
            print(str(answers[j]) + ". User answered " + str(userans[j]) + ". The answer was correct")
        elif (userans[j] != int(a_values[j])*int(b_values[j])):
            print(str(answers[j]) + ". User answered " + str(userans[j]) + ". The answer was wrong")
    print(str(score) + "/" + str(number))

    stop = input("Do you want to try again? (yes/no)")
    if (stop != "yes"):
        finish = True
