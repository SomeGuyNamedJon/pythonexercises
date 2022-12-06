def confirmation(a):
    for i in range(1,6):
        ans = a[0]
        match ans.lower():
            case "yes!"|"yes"|"y":
                return 1
            case "no!"|"no"|"n":
                return 0
            case other:
                if(i == 5):
                    print("I'm sorry we couldn't understand each other")
                    return -1
                elif(i < 4):
                    a = input("Sorry... I didn't understand that\n").split(' ')
                else:
                    a = input("Gonna give you one more chance\n").split(' ')


name = input("What is your name?\n")

if(name != ""):
    #Input validation
    while not name.isalpha():
        name = input("Enter only letters please:\n")

    match len(name):
        case 1:
            print("Your name is very efficient!")
        case 2|3:
            print("One syllable, nice!")

    if name.lower() == "jon" or name.lower() == "jonathan":
        answer = input("For real?\n").split(' ')
        if(confirmation(answer) > 0):
            print("Me too")
        else:
            print("Oh... well then")
            print(f"Well I'm just going to call you {name} anyways")

    elif name.lower() == "megan":
        answer = input("Wait! What really?\n").split(' ')
        result = confirmation(answer)
        if(result == -1):
            print(f"Well I'm just going to call you {name} anyways")
        elif(result):
            print("I know another Megan, she's pretty cool")
        else:
            print("Eh? But you said...")
            print(f"Well I'm just going to call you {name} anyways")
    else:
        print("It's a cool name")
    
    print("Hello", name)
else:
    print("Hello World")
