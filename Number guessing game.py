import random
print("What's your name?")
name=input()
print("Hello",name,", Welcome to the number guessing game!")
print("Here, I will think of a number between 1 to 20 and you have to guessed it correctly in less than 8 guesses.")
number=random.randint(1,20)
i=8
while(i!=0):
    print("Take a guess: ")
    guess=int(input())
    i=i-1
    if(guess<number):
        print("WRONG!! your guess is less than the number")
        print("No. of guesses left: ",i)
    elif(guess>number):
        print("WRONG!! your guess is greater than the number")
        print("No. of guesses left: ",i)
    elif(guess==number):
        print("Good Job!!, You guessed the right number")
        print("No. of guesses left: ",i)
        break
    if(i==0):
        print("Sorry, the number I was thinking was ",number,"\n\t Better luck next time :)")
