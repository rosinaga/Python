import random

finish = False
while finish == False:
    ceiling = int(input("Give a Ceiling Value"))
    total = int(input("How many questions?"))

    a_values = []
    b_values = []
    questions = []
    userans = []
    answer = []
    score = 0

    def product():
        for i in range(total):
            a = random.randint(1, ceiling)
            b = random.randint(1, ceiling)
            a_values.append(str(a))
            b_values.append(str(b))
            questions.append("Question " + str(i+1) + "/" + str(total) + ": " + str(a) + " x " + str(b) + " = ?")
            answer.append("Q" + str(i+1) + ") " + str(a) + " x " + str(b) + " = " + str(a*b))
    product()

    for elem in questions:
        userans.append(int(input(elem)))

    for j in range(total):
        if(userans[j] == int(a_values[j]) * int(b_values[j])):
            score = score + 1
            print(str(answer[j]) + ". User answered " + str(userans[j]) + ". The answer was correct")
        elif(userans[j] != int(a_values[j]) * int(b_values[j])):
            print(str(answer[j]) + ". User answered " + str(userans[j]) + ". The answer was wrong")

    stop = input("Do you want to try again? (yes/no)")
    if(stop != "yes"):
        finish = True
