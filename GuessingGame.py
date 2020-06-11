import random
Valid_Consent = ["yes","no"]
consent=""
win=0
while consent != "no":
    consent=""
    highest=0
    while highest<=9:
        print("minimum betting amount is Rs10")
        highest = int(input("How much money do you want to bet : "))
    valid_input=[*range(1,highest+1)]
    answer = random.randint(1,highest)
    #print(answer) #TODO remove after testing
    print(" Enter a number between 1 and {}".format(highest))
    print("You have 3 chances!")
    count=0
    trial=0
    while trial != answer:
        count+=1
        if count>3:
            win=win-highest
            print("The lucky number is {}".format(answer))
            print("You loose Rs {0}! Your total win is {1}".format(highest,win))
            while consent not in Valid_Consent:
                consent=input("do you want to bet again? (yes/no) : ")
            break
        while trial not in valid_input:
            trial=float(input("Enter a valid Trial{} : ".format(count)))
        if count<3:
            if trial<answer:
                print("Guess a higher number")
            elif trial > answer:
                print("Guess a lower number")
            else:
                continue
        if trial!=answer:
            trial=0


    if count<=3:
            win=win+highest
            print("Congrats! You Won {0}! Your Total Win Is {1} ".format(highest,win))
            while consent not in Valid_Consent:
                consent=input("do you want to bet again? (yes/no) : ")

print("Thank You for palying with us!")
if win>0:
    print("You collect Rs{}".format(win))
elif win<0:
    print("Pay Rs{} before leaving!".format(win*-1))
else:
    print("Bye! Come Again")

exit=input("Press any key to exit!")

