"""
a simple program for a two-player Tic-Tac-Toe game!
"""

from random import randint
from os import system, name
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function to clear screen (code shown below works for Mac, Linux and Windows too): 
def clear():
    '''
    PURPOSE:    Clears output screen
    '''
    if name == 'nt': 
        _ = system('cls')
    else:
        _ = system('clear')

# -*- coding: utf-8 -*-


#global variables which will be used to keep track of the game events across different functions:
P1=''
P2=''
P1_charkey=-1
P2_charkey=-1
char_dict={0:'o',1:'x'}
col_dict={'a':0,'b':1,'c':2}
current_player=''
board=[['0','0','0'],['0','0','0'],['0','0','0']]
'''
To note: This variable - which tracks the board's contents - is of a nested list structure, where each list element inside the board var corresponds to each row
'''


        
def print_board(board_contents):
    '''
    INPUT:      Board variable to show elements of the game board
    PURPOSE:    To display the board's current state -i.e. all three rows- whenever required
    '''
    print('       a         b         c    ')
    print('                                ')
    

    def switch_print(num,char):
        
        '''
        INPUT:      line number to be printed in a row and character to be printed (x => X, o => O, 0 => empty space 
                    to note: each row consists of 9 lines: 
                        1 Line for Horizontal Border 
                        1 Line empty space
                        5 Lines to print character
                        1 Line empty space
                        1 Line for Horizontal Border 
        PURPOSE:    prints the differing styles of those 5 Lines reserved to print character based on the character passed as arg
                    to note: this fn is supposed to be called inside print_row() only, hence the nested declaration
        '''

        if char=='x':
            switcher={
                1:"| *   * |",
                2:"|  * *  |",
                3:"|   *   |",
                4:"|  * *  |",
                5:"| *   * |"
            }
        elif char=='o':
            switcher={
                1:"|  ***  |",
                2:"| *   * |",
                3:"| *   * |",
                4:"| *   * |",
                5:"|  ***  |"
            }
        elif char=='0':
            switcher={
                1:"|       |",
                2:"|       |",
                3:"|       |",
                4:"|       |",
                5:"|       |"   
            }
        print(switcher.get(num),end='')
   

    def print_row(board_row,row_no):
        
        '''
        INPUT:      The board row to be printed and the the row number of said row
        PURPOSE:    Displays the rest of the 9 Lines that switch_print() doesn't take care of
                    to note: this fn is supposed to be called inside print_board() only, hence the nested declaration
                             switch_print() will be called inside this function, thus all 9 Lines will be taken care of
        '''

        print('   --------- --------- ---------')
        print('   |       | |       | |       |')
        
        for lin in range(1,6):
            
            if lin==3:
                print(f'{row_no+1}  ',end='')
            else:
                print('   ',end='')
            
            for j in range(3):
                switch_print(lin,board_row[j])
                if j!=2:
                    print(' ',end='')
            
            print('')
                    
        print('   |       | |       | |       |')
        print('   --------- --------- ---------')
    
    for row_no in range(3):
        print_row(board_contents[row_no],row_no)

      
def start_game():
    '''
    PURPOSE:    Takes care of starting of each Tic-Tac-Toe game
                Takes the names of players and the toss which decides the starting player:
                    Winner of Toss gets to decide if they go first or not
                    Loser of Toss gets to decide the symbol they get to play with
    '''
    global P1
    global P2
    global P1_charkey
    global P2_charkey
    global current_player
    global board

    P1=''
    P2=''
    P1_charkey=-1
    P2_charkey=-1
    current_player=''
    board=[['0','0','0'],['0','0','0'],['0','0','0']]


    print("Hello Players, welcome to Tic-Tac-Toe!")
    P1=input('Enter your name, Player 1:')
    while True:
        P2=input('Enter your name, Player 2:')
        if P2!=P1:
            break
    P1_choice=-1
    
    #The below format ensures that bad inputs aren't accepted. Will be used again wherever controlled input is required
    while True:
        P1_choice=input('Player 1, enter 1 for Heads or 0 for Tails:')
        if P1_choice.isdigit() and int(P1_choice) in {0,1}:
            break
        
    P1_choice=int(P1_choice)
    print('\nTossing...')
    sleep(1)
    toss=1 if randint(1,101)%2==0 else 0
    toss_res='Heads' if toss==1 else 'Tails'
    print(f"\nIt's {toss_res}!")
    print('The toss loser gets to choose the symbol they get to play with')
    print('The toss winner gets to choose if they go first or not')
    
    if P1_choice==toss:
        while True:
            P2_charkey=input(f"Choose your symbol, {P2}. Enter 1 for X or 0 for O:")
            if P2_charkey.isdigit() and int(P2_charkey) in {0,1}:
                break
        P2_charkey =int(P2_charkey)
        P1_charkey =int(not P2_charkey)
        while True:
            P1_plays=input(f"{P1}, Do you wish to go first? Enter 1 for Yes or 0 for No:")
            if P1_plays.isdigit() and int(P1_plays) in {0,1}:
                break
        current_player=P1 if int(P1_plays) else P2
        
    else:
        while True:
            P1_charkey=input(f"Choose your symbol, {P1}. Enter 1 for X or 0 for O:")
            if P1_charkey.isdigit() and int(P1_charkey) in {0,1}:
                break
        P1_charkey =int(P1_charkey)
        P2_charkey =int(not P1_charkey)
        while True:
            P2_plays=input(f"{P2}, Do you wish to go first? Enter 1 for Yes or 0 for No:")
            if P2_plays.isdigit() and int(P2_plays) in {0,1}:
                break
        current_player=P2 if int(P2_plays) else P1
    
    print("Let's begin! Have Fun!\n\n")

    
def mid_game():
    '''
    PURPOSE:    begins the game properly and keeps the gameplay loop going on till an end-point (like a victory or draw) has reached
    '''
    global P1
    global P2
    global P1_charkey
    global P2_charkey
    global current_player
    global board
    
    sleep(1)
    clear()
    print_board(board)
    
    def board_update(row,col,char):
        '''
        INPUT:      character to be entered to the board and the required location where it must be done so
        PURPOSE:    updates the board by entering the player's symbol as per how the player enters the desired location
        '''
        board[row][col]=char
        sleep(1)
        clear()
        print_board(board)
  
    
    while True:
        while True:
            while True:
                row=input(f'{current_player}, choose which row you want to enter your symbol in:')
                if row in {'1','2','3'}:
                    break
            row=int(row)-1
            while True:
                col=input(f'{current_player}, choose which column you want to enter your symbol in:')
                if col in {'a','b','c'}:
                    break
            if board[row][col_dict[col]]=='0':
                break

        #the following part checks if the current player has won, and exits the gameplay loop accordingly
        if current_player==P1:
            board_update(row,col_dict[col],char_dict[P1_charkey])
            if board[row][0]==board[row][1]==board[row][2]==char_dict[P1_charkey] or board[0][col_dict[col]]==board[1][col_dict[col]]==board[2][col_dict[col]]==char_dict[P1_charkey] or board[0][0]==board[1][1]==board[2][2]==char_dict[P1_charkey]:
                print(f'Tic-Tac-Toe! {P1}, you win!')
                break
        else:
            board_update(row,col_dict[col],char_dict[P2_charkey])
            if board[row][0]==board[row][1]==board[row][2]==char_dict[P2_charkey] or board[0][col_dict[col]]==board[1][col_dict[col]]==board[2][col_dict[col]]==char_dict[P2_charkey] or board[0][0]==board[1][1]==board[2][2]==char_dict[P2_charkey]:
                print(f'Tic-Tac-Toe! {P2}, you win!')
                break

         #the following part checks if the game has been drawn, and exits the gameplay loop accordingly
        if board[0].count('0')==board[1].count('0')==board[2].count('0')==0:
            print("Well, it's a draw. Well fought, both of you!")
            break

        #if gameplay loop hasn't stopped, changes the current player to the other player
        if current_player==P1:
            current_player=P2
        else:
            current_player=P1
                
            
    
    
def TTT():
    '''
    PURPOSE: Driver Function, all other component functions will come together here
    '''
    while True:
        start_game()
        mid_game()
        while True:
            x=input('Do you want to play again? [Y/N]:')
            if x.isalpha() and x.upper() in {'Y','N'}:
                break
        if x.upper()=='N':
            break

TTT()
            
    
    