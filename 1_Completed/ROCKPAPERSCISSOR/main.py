import random

def game():
    user_choice=input("Enter the choice r-rock,s-scissor,p-paper :")
    comp_choice=random.choice(['r','p','s'])

    if user_choice==comp_choice:
        return 'tie'
    if winner(user_choice,comp_choice):
        return "User is the winner !!"
    return "Cmputer won and you lost XD"

def winner(x,y):     #USER WIN CASES ARE S===>P  , P===>R ,R===>S   
    if(x=='s' and y=='p') or (x=='p' and y=='r') or (x=='r' and y=='s'):
        return True
print(game())