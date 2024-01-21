import random
def guess(x,y):
    random_number=random.randint(1,x)
    difficulty_attempts={'E' : '10' ,'M' : '7' ,'H' : '5'}
    for key in difficulty_attempts.keys():
        if (y==key):
            chances=difficulty_attempts[key]
    print(f"ONLY {chances} GUESSES !!!! GOOD LUCK ")        
    guess=0
    attempts=0
    flag=0
    while guess != random_number:
        guess=int(input(f'Make your guess between 1 and {x} :'))
        if guess<random_number:
            print("Guessed number is lower !!!")
        elif guess>random_number:
            print('Guess is too high !!!')
        attempts=attempts+1
        if(attempts==chances):
            flag=1
            break
    if(flag==1):
        print("You lost the game  :( ")
    else:
        print(f"Congrats you guessed the number {random_number} correctly !!!")
welcome="WELCOME TO THE GUESSING GAME"
print(welcome.center(400))
Difficulty_level=input("Enter the diificult level (Easy(E)/Medium(M)/High(H)) :")
guess(random.randint(10,100),Difficulty_level)           

