from re import T


def check_guess(guess,answer):
    global score
    still_gussing = True
    attempt = 0
    while still_gussing and attempt <3:
        if guess.lower()== answer.lower():
            print("Correct Answer")
            score = score +1
            still_gussing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong Answer, try again")
            attempt = attempt+1
    if attempt == 3:
        print("The correct answer is ", answer)

score =0 
print("Guess the animal")
guess1 = input("Which bear lives at the north pole?")
check_guess(guess1, "polar bear")
guess2 = input("which is the fastest land animal?")
check_guess(guess2, 'cheetah')
guess3 = input("Which is the largest animal?")
check_guess(guess3,"Blue Whale")
print("your score is "+ str(score))