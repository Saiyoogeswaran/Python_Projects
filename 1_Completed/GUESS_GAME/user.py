import random

def comp_end(x):
    lower_bound=1
    upper_bound=x
    reply=""
    while reply!='c':
        if lower_bound!= upper_bound:
            guess=random.randint(lower_bound,upper_bound)
        else:
            guess= lower_bound    #the case when both lower and upper bound are same ,it means the guess is made correctly
        reply=input(f"The number {guess} high?(h) or low?(l) or correct(c)? ").lower()   #to make all the inputs taken from user to be lowercase
        if reply=='h':
            upper_bound=guess-1
        elif reply=='l':
            lower_bound=guess+1
    print(f"The number {guess} is guessed correctly !!!")  

comp_end(10)             