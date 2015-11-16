from random import randint as r
from time import sleep
from sys import exit

def clear():
    from os import name,system
    if name == 'posix':system('clear')
    if name == 'nt':system('cls')

def main():
    clear()
    print("  _____    __   __ ___  __   __     _____             __")
    print(" |  |  |  |__| |__  |  |__  |__|   |  |  |  |  |\ |  |  \ ")
    print(" |  |  |  |  |  __| |  |__  |  \   |  |  |  |  | \|  |__/ ")
    print("\n")
    print("Guess a 4-digit number\n\nO = Right number in right place\n/ = Right number in wrong place\nX = Number is not in solution\n")
    print("-----------MAKE A GUESS-----------")
    number = [r(0,9),r(0,9),r(0,9),r(0,9)]

    guess = []

    #INTERPRET
    counter = 0
    while guess != number:
        win = True
        counter += 1
        if counter > 10:
            print("GAME OVER")
            win = False
            break
        guess = []
        temp = input()
        if (len(temp) != 4) or (not temp.isdigit()):
            if temp == "banane":
                hax()
            counter -= 1
            continue
        else:
            temp = list(temp)
            for item in temp:
                guess.append(int(item))


        #CHECK
        check = zip(number,guess)
        check = list(check)
        grade = []
        
        for pair in check:
            if pair[0] == pair[1]:
                grade.append("O")
            elif pair[1] in number:
                grade.append("/")
            else:
                grade.append("X")
        print(grade)

    if win:
        print("YOU WIN!")
        sleep(1)
        print("Score: " + str(counter) + " guesses")
        sleep(1)
        if 8 <= counter <= 10:
            print("You did okay.")
        elif 6 <= counter < 8:
            print("You did pretty good.")
        elif 4 <= counter < 6:
            print("You did great!")
        elif 3 <= counter < 4:
            print("Wow! You did amazing!")
        elif 2 <= counter < 3:
            print("HOLY SHIT! NICE!")
        else:
            hax()


def hax():
    clear()
    print(".")
    sleep(1)
    clear()
    print("..")
    sleep(1)
    clear()
    print("...")
    sleep(1)
    clear()
    print("...1 guess...")
    sleep(2)
    clear()
    obscenities = "FUCKING HACKER YOU THINK THIS IS A MOTHERFUCKING GAME I WILL MESS YOUR SHIT UP YOU CANT JUST WALTZ IN HERE AND ALL WILLY NILLY WIN THIS SHIT WITHOUT ANY FUCKING EFFORT HOW FUCKING DARE YOU I SPENT LIKE 0.0002 SECONDS THINKING UP THAT NUMBER AND FROM A COMPUTERS PERSPECTIVE THATS A LOT OF FUCKING TIME BUT YOU JUST COME IN AND SLAUGHTER IT LIKE THE PIECE OF SHIT YOU ARE I CANT FUCKING BELIEVE THIS I CANT FUCKING BELIEVE YOU I FUCKING QUIT BYE"
    p = obscenities.split(" ")
    for word in p:
        print(word)
        sleep(.055)
    exit()

while True:
    main()

    sleep(1)
    again = input("Play again?(y/n): ")
    if again.lower() == "y":
        main()
    break
