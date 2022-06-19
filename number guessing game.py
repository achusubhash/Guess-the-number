import random

#Guessing number

def main():
    pc = random.randint(10, 100)
    H = random.randint(0, 5)
    Hint = pc - H or pc + H
    print("Hint is.......",Hint)
    player = int(input("Enter a number between 10-100 : "))
    if player == pc:
        print("U got it")
    elif player > pc:
        print("Higher!")
    elif player < pc:
        print("Lower!!!")
    elif player < "10":
        print("Choose above 10!")
    elif player > "100":
        print("Choose upto 100!")
    else:
        print("Number was",pc)



#Again

def again():
    again=input("Play again? : ")
    s = tuple(("Yes","yEs","yeS","YEs","YeS","yES","YES","OK","ok","Ok","oK","Yah","yAh","yaH","YAh","yAH","YaH","YAH","ys","Ys","yS"))
    d = tuple(("No","NO","no","nO","Nah","nah","NAH","nAH","NaH","NAh"))
    if again == s or again == d:
        main()
    else:
        print("Ok Bye!")
main()
again()