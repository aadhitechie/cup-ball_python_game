#this is a simple game 
from random import shuffle
example = [1,2,3,4,5,6,7]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Please enter 0,1 or 2\t')
    return int(guess)
    
def check_guess(mylist,guess):
    if mylist[guess]=='0':
        print('Correct guess')
    else:
        print("Wrong guess")
    print(mylist)

mylist = [' ','0',' ']
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mylist,guess)