import random
import sys

def is_positive_integer(s):
    if s.isdigit() and int(s)>0:
        return True
    else:
        return False

while True:

        n=input("Level: ")
        if not is_positive_integer(n):
            continue
        n=int(n)
        digit=random.randint(1, n)

        while True:
            guess=input("Guess: ")
            if not is_positive_integer(guess):
                continue
            guess=int(guess)
            if guess>n:
                continue
            elif guess<digit:
                print("Too small!")
                continue
            elif guess>digit:
                print("Too large!")
                continue
            elif guess==digit:
                sys.exit("Just right!")