######################################## PROJECT 1: TIC TAK TOE ###########################################

#import library
import random
import sys

# Create gameboard

b=[
    0,1,2,
    3,4,5,
    6,7,8
]

def print_board():
    print(b[0],'|',b[1],'|',b[2])
    print('--+---+--')
    print(b[3],'|',b[4],'|', b[5])
    print('--+---+--')
    print(b[6],'|',b[7],'|', b[8])

print_board()

print("Player is: X and Computer is :O")
#take imputs

print("****************************** Let's Start Game *******************************")
count=0
def player_input():

    player_in=int(input("Enter Position for move [0-8]:"))
    if b[player_in] !='X' and b[player_in] !='O':
        b[player_in]='X'
        count=+1


    else:
        print("Position is already filled,choose another one")




def computer_input():

    computer_in=random.randint(0,8)
    if b[computer_in]!='O' and b[computer_in]!='X':
        b[computer_in]='O'

def winner(str):
    if b[0]==b[1]==b[2]==str:
        return True


    elif b[3]==b[4]==b[5]==str:
        return True


    elif b[6] == b[7] == b[8] == str:
        return True


    elif b[0] == b[3] == b[6] == str:
        return True


    elif b[1] == b[4] == b[7] == str:
        return True


    elif b[2] == b[5] == b[8] == str:
        return True

    elif b[2] == b[4] == b[6] == str:
        return True


    elif b[0] == b[4] == b[8] == str:
        return True

def tie():
    if count>5:
        print("Game is Tie")

def play_agin():


        choice= input("Do You Want to Play again ?? (Y/N)")
        while (choice=='y' or choice=='Y'):
            player_input()
            computer_input()
            print_board()
        while(choice=='n' or choice=='N'):
            break



while True:
    player_input()
    computer_input()
    print_board()
    tie()


    if winner('X') is True:
        print(" Congratulations , You Win")
        play_agin()
        break


    elif winner('O') is True:
        print("Computer Win")
        play_agin()
        break


