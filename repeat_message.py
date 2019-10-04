def repeat(message, number):
    print()
    for  i in range(number):
        print(message)
        #growing number before message
    print()

finish = False
while finish == False:
    print()
    print("Give a message, please:")
    #Retrieves the message given by a user:
    message = input()
    print("Give a number, please")

    try:
        number = int(input())#error if function is not integer
        repeat(message, number)#function call
    except ValueError:
        print("Not an Intiger!")

        #print("Want to try again (yes/no)?")
    m = input("Want to try again (yes/no)?")
    if (m != "yes"):
        finish = True
