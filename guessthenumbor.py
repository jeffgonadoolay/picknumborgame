import random
turns = 5
playerguess = 0

print("time to play guess the numbor game!")
print("the computer will now choose a number...")
print("a number between 1 and 20 has been selected")
computersnumber = random.randint(1, 20)

print("make a guess:")
print("turns left:")
print(turns)
while True:
    try:
        playerguess = int(input())
        turns -= 1
        if playerguess == computersnumber:
            print("you guessed correctly")
            break
        else:
            print("you guessed wrong")
            if turns == 0:
                print("out of turns")
                break
            else:
                print("turns left:")
                print(turns)
                if playerguess > computersnumber:
                    print("try lower")
                else:
                    print("try higher")
    except:
        print("That's not a number!")
