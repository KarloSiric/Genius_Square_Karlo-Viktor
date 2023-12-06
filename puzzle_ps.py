'''
@ASSESSME.USERID: KarloSiric
@ASSESSME.AUTHOR: Viktor Pavlovic, Karlo Siric
@ASSESSME.DESCRIPTION: Problem Solving 11
@ASSESSME.ANALYZE: YES 
'''
import random as r
from colorama import Back, Fore, Style
import copy
import time
import playsound

#################################################################
#################################################################
#          This is a puzzle game called Genius Square.          #        
#################################################################
#################################################################




#################################################################
#     These are all the GLOBAL VARIABLES used in the program.   #   
#################################################################



EMPTY_SPOT = '-'
BLOCKER_SPOT = 'o'
# L_SHAPE = [[[0, 0, 1], [1, 1, 1]], [[1, 0], [1, 0], [1, 1]], [[1, 1, 1], [1, 0, 0]], [[1, 1], [0, 1], [0, 1]], [[1,1,1], [0,0,1]], [[1,1], [1,0], [1,0]], [[1,1,1], [1,0,0]], [[0,1], [0,1], [1,1]]]
# L SHAPE!

## WE CRAETED THIS TO CHECK FOR ALL THE ROTATIONS OF ALL THE SHAPES!

L_SHAPE_BASE = [[1, 0], [1, 0], [1, 1]] # BASE SHAPE
# L_SHAPE_ROT1 = [[[0, 1], [0, 1], [1, 1]]] # left rotation
# L_SHAPE_ROT2 = [[[1, 1, 1], [1, 0, 0]]] 
# L_SHAPE_ROT3 = [[[1, 1], [0, 1], [0, 1]]] # right rotation          
# L_SHAPE_ROT4 = [[[1, 1, 1], [0, 0, 1]]]
# L_SHAPE_ROT5 = [[[1, 1], [1, 0], [1, 0]]]
# L_SHAPE_ROT6 = [[[1, 1, 1], [1, 0, 0]]]
# T SHAPE 

T_SHAPE_BASE = [[1, 1, 1], [0, 1, 0], [0, 1, 0]]
# T_SHAPE_ROT1 = [[[0, 1], [1, 1], [0, 1]]]
# T_SHAPE_ROT2 = [[[0, 1, 0], [1, 1, 1]]]                       ###
# T_SHAPE_ROT3 = [[[1, 0], [1, 1], [1, 0]]]                      #
# # T SMALL SHAPE                                                #

T_SMALL_SHAPE_BASE = [[1, 1, 1], [0, 1, 0]]       ###
# T_SMALL_SHAPE_ROT1 = [[[0 ,1], [1, 1], [0, 1]]]                 # 
# T_SMALL_SHAPE_ROT2 = [[[0, 1, 0], [1, 1, 1]]]                   #
# T_SMALL_SHAPE_ROT3 = [[[1, 0], [1, 1], [1, 0]]]
# C SHAPE

C_SHAPE_BASE = [[1, 1], [1, 0], [1, 1]]            ##
# C_SHAPE_ROT1 = [[[1, 1], [0, 1], [1, 1]]]           #
# C_SHAPE_ROT2 = [[[1, 0, 1], [1, 1, 1]]]             ##
# C_SHAPE_ROT3 = [[[1, 1], [1, 0], [1, 1]]]
# Z SHAPE
Z_SHAPE_BASE = [[1, 1, 0], [0, 1, 1]]   

# L SMALL SHAPE
L_SMALL_SHAPE_BASE = [[1, 0], [1, 1]]

# F SHAPE
F_SHAPE_BASE = [[1, 1], [1, 0], [1, 1], [1, 0]]             
                                                    
#Symbols

SYMBOLS_LIST = ["T", "t", "L", "l", "C", "z", "f", BLOCKER_SPOT]

SYMBOL_NUMBERS = [1,2,3,4,5,6,7]
SYMBOL_NUMBERS_STRING = ["1","2","3","4","5","6","7"]

#Dice
DIE1 = [(0, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 2)]
DIE2 = [(0, 1), (1, 1), (2, 1), (0, 2), (1, 0), (1, 2)]
DIE3 = [(2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3)]
DIE4 = [(4, 0), (5, 1), (5, 1), (1, 5), (0, 4), (0, 4)]
DIE5 = [(0, 4), (1, 4), (2, 5), (2, 4), (3, 5), (5, 5)]
DIE6 = [(4, 3), (5, 3), (4, 4), (5, 4), (3, 4), (4, 5)]
DIE7 = [(5, 0), (5, 0), (5, 0), (0, 5), (0, 5), (0, 5)]
DICE = [DIE1, DIE2, DIE3, DIE4, DIE5, DIE6, DIE7]


######################################################
#  These are our main classes used in the program.   # 
######################################################

class Shape:
    __slots__ = ["table", "position"]

    def __init__(self, table:list) -> None:
        self.table = table
        self.position = None

    def set_position(self, position) -> tuple:
        self.position = position

    def get_table(self) -> list:
        return self.table

    def __str__(self) -> str:
        return f"{self.table} {self.position}"
   
class Puzzle:
    __slots__ = ["__board","blocker_locations"]
    def __init__(self, blocker_locations:tuple) -> None:
        self.__board = [[EMPTY_SPOT for _ in range(6)] for _ in range(6)]
        self.blocker_locations = blocker_locations
        for blocker in blocker_locations:
            self.__board[blocker[0]][blocker[1]] = BLOCKER_SPOT
    
    
###################################################################
#   This is the main draw function that draws the shapes on the   #
###################################################################    
    
    def draw(self, position:tuple, shape:Shape, symbol:str) -> None:
        shape.set_position(position)
        for row in range(len(shape.table)):
            for column in range(len(shape.table[row])):
                if shape.table[row][column] == 1:

                    """if symbol == "T":
                        color = Back.MAGENTA
                    elif symbol == "t":
                        color = Back.LIGHTMAGENTA_EX
                    elif symbol == "L":
                        color = Back.CYAN
                    elif symbol == "l":
                        color = Back.LIGHTRED_EX
                    elif symbol == "C":
                        color = Back.LIGHTGREEN_EX
                    elif symbol == "z":
                        color = Back.GREEN
                    elif symbol == "f":
                        color = Back.YELLOW
                    else:
                        color = Back.RESET

                    self.__board[row+position[0]][column+position[1]] = f"{color}{Fore.WHITE}{symbol}{Back.RESET}"""
                    self.__board[row+position[0]][column+position[1]] = symbol

    def get_board(self):
        return self.__board
    
    def __str__(self) -> str:
        board = "    0 1 2 3 4 5\n    -----------\n"
        rows = [row for row in self.__board]
        rows_str = []
        for i in range(len(rows)):
            row = ""
            for item in rows[i]:
                row += f"{item} "
            rows_str.append(row)
        for index in range(len(rows_str)):
            board += f"{index} | {rows_str[index]}\n"
        return board


############################################################
#   This function prints out the options for the shapes.   #
############################################################

used_shapes = []

def print_options():
    print("These are the shapes you can choose from:\n")
    if "1" not in used_shapes:
        print("1 = TTT \n     T\n     T\n")
    if "2" not in used_shapes:
        print("2 = ttt \n     t\n     t\n")
    if "3" not in used_shapes:
        print("3 = L\n    L\n    LL\n")
    if "4" not in used_shapes:
        print("4 = l\n    ll\n")
    if "5" not in used_shapes:
        print("5 = CC\n    C\n    CC\n")
    if "6" not in used_shapes:
        print("6 = zz\n     zz\n")
    if "7" not in used_shapes:
        print("7 = ff\n    f\n    ff\n    f\n\n")


    # print("1 = TTT \t\t 2 = ttt \t\t 3 = L\
    #       \n     T \t\t\t      t \t\t     L\
    #       \n     T \t\t\t        \t\t     LL\n\n")
    # print("4 = l \t\t 5 = CC  \t\t 6 = zz\
    #       \n    ll \t\t      C \t\t      zz\
    #       \n       \t\t     CC \t\t       \n\n")

    # print("7 = ff\n    f\n    ff\n    f\n\n")

############################################################
#    This function asks the user to choose a shape.        #
#   It also checks if the shape is already placed.         #
#   If it is, it asks the user to choose another shape.    #
############################################################    

def ask_shape():
    while True:
        userInputShape = input("Choose which shape to place (O for options): ").lower()

        if userInputShape == "o":
            print_options()
        elif userInputShape in SYMBOL_NUMBERS_STRING and userInputShape not in used_shapes:
            used_shapes.append(userInputShape)
            return int(userInputShape)
        else:
            print("Invalid input or shape already placed.Please choose another shape!")
            
        
        
        # elif userInputShape == "1":
        #     return 1
        # elif userInputShape == "2":
        #     return 2
        # elif userInputShape == "3":
        #     return 3
        # elif userInputShape == "4":
        #     return 4
        # elif userInputShape == "5":
        #     return 5
        # elif userInputShape == "6":
        #     return 6
        # elif userInputShape == "7":
        #     return 7


############################################################
#    This function asks the user to choose a position.     #
############################################################

def ask_position():
    while True:
        try:
            userInputPositionY = int(input("Choose in which column to place the shape: "))
            userInputPositionX = int(input("Choose in which row to place the shape: "))
        except ValueError:
            continue

        if userInputPositionX >= 0 and userInputPositionX <= 5 and userInputPositionY >= 0 and userInputPositionY <= 5:
            return (userInputPositionX, userInputPositionY)

############################################################
#    This function creates the shapes.                     #
############################################################

def make_shape(s_type:int):
    if s_type == 1:
        return Shape(T_SHAPE_BASE), "T"
    elif s_type == 2:
        return Shape(T_SMALL_SHAPE_BASE), "t"
    elif s_type == 3:
        return Shape(L_SHAPE_BASE), "L"
    elif s_type == 4:
        return Shape(L_SMALL_SHAPE_BASE), "l"
    elif s_type == 5:
        return Shape(C_SHAPE_BASE), "C"
    elif s_type == 6:
        return Shape(Z_SHAPE_BASE), "z"
    elif s_type == 7:
        return Shape(F_SHAPE_BASE), "f"


############################################################
#    This function checks if the shape is already placed.  #
############################################################

def shaper():
    while True:
        s_type = ask_shape()
        if s_type not in SYMBOL_NUMBERS:
            print("That shape is already placed!")
            print("Please choose another shape!")
            continue
        else:
            SYMBOL_NUMBERS.remove(s_type)
            shape, s_letter = make_shape(s_type)
            return shape, s_letter

############################################################
#    This function creates the blockers.                   #
############################################################


def blockers(amount:int):
    blocker_locations = []

    for index in range(amount):
        if index > len(DICE):
            return "Invalid Input {}".format(amount)
        else:
            blocker_locations.append(r.choice(DICE[index]))

    return blocker_locations

############ ROTATIONS  #############
#####################################
#####################################


def rotate_shape_left(shape:Shape):
    return list(zip(*reversed(shape)))

def rotate_shape_right(shape:Shape):
    return list(reversed(list(zip(*shape))))

def reverse_shape(shape:Shape):
    return list(reversed(shape))

def rotate_shape(shape:Shape, s_letter):
    puzzle = Puzzle(((0, 0), (5, 0), (0, 5), (5, 5)))

    while True:
        userInputRotateBool = input("Do you want to rotate it? (y/n) ").lower()
        
        if userInputRotateBool == "y":
            while True:
                userInputRotate = input("Left(L) or Right(R) or Reversed(E) or Confirm(C): ").lower()
                if userInputRotate == "l":
                    puzzle.draw((2, 2), shape, "-")
                    shape.table = rotate_shape_left(shape.table)
                    puzzle.draw((2, 2), shape, s_letter)
                    print(puzzle)
                elif userInputRotate == "r":
                    puzzle.draw((2, 2), shape, "-")
                    shape.table = rotate_shape_right(shape.table)
                    puzzle.draw((2, 2), shape, s_letter)
                    print(puzzle)
                elif userInputRotate == "e":
                    puzzle.draw((2, 2), shape, "-")
                    shape.table = reverse_shape(shape.table)
                    puzzle.draw((2, 2), shape, s_letter)
                    print(puzzle)
                elif userInputRotate == "c":
                    break
            break
        elif userInputRotateBool == "n":
            break

#############################################
#   This function creates a tuple of tuples #
#   that contains the coordinates of all    #
#   the symbols on the board except         #
#   the empty spots.                        #
#############################################


def get_coords(symbols: list, puzzle: Puzzle):
    coords = []
    board = puzzle.get_board()

    for symbol in symbols:
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == symbol:
                    coords.append((row, column))
    
    return tuple(coords)

################################################
#   This function checks if the shape collides #
#   with the blockers.                         #
################################################



def check_collision(shape: Shape, blockers: tuple):
    for row in range(len(shape.table)):
            for column in range(len(shape.table[row])):
                if shape.table[row][column] == 1:
                    if (row+shape.position[0], column+shape.position[1]) in blockers:
                        return True
    return False

################################################
#   This function draws the shape on the board #
#   if there is no collision.                  #
################################################


def shape_draw(shape: Shape, puzzle: Puzzle, s_letter):
    while True:
        userInputPosition = ask_position()
        shape.position = userInputPosition
        if check_collision(shape, get_coords(SYMBOLS_LIST, puzzle)):
            print("Can't place shape there, place is already occupied!")
        elif shape.position[0] < 0 or shape.position[1] < 0 or shape.position[0] + len(shape.table) > 6 or shape.position[1] + len(shape.table[0]) > 6:
            print("Can't place shape there, it is out of bounds!")
        else:
            puzzle.draw(shape.position, shape, s_letter)
            break

#################################################
#   This function asks the user if he wants to  #
#   quit or continue playing.                   #
#################################################


def prompt_quit():
    while True:
        userInputQuit = str(input("Do you want to quit or would you like to continue playing? (Q/C) ").lower())
        if userInputQuit == "q":
            print("Thank you for playing!")
            return True
        elif userInputQuit == "c":
            print("Okay let's continue then!\n")
            return False
        else:
            print("Invalid input!")
            print("Please enter Q or C!")

#################################################
#   This function shows the difficulty level    #
#   and the rules of the game.                  #
#################################################



def rules():
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "Welcome to the Genius Square game!\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "The rules are simple:\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "You will be given a shape and you will have to place it on the board.\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "You will have to place all the shapes on the board without overlapping them or placing them on the blockers.\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "You can rotate the shapes by choosing the left or right rotation or reversing them.\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "If you do not complete the game within 3 minutes then your final game score will be deducted by 500 points.\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "If you complete the game within 3 minutes then your final game score will be increased by 500 points.\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "Your score will be shown after you either complete the game or choose the easy way out.\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Style.BRIGHT + Fore.RED + "\033[1m" + "Good luck and have fun!\n" + "\033[0m\n" + Style.RESET_ALL)
    time.sleep(1)

##################################################
#   This function asked the user to choose the   #
#           difficulty level.                    #   
#   It also prints out the rules of the game.    #
#   It returns the amount of blockers.           #
#   This function is not used in the program.    #
#   ---FOR TESTING PURPOSES ONLY---              #                  
##################################################
    
    
    #--------------------------------------------#
    # while True:
    #     userInputDifficulty = input("Choose your difficulty level (E/M/H): ").lower()
    #     if userInputDifficulty == "e":
    #         print("You have chosen Easy difficulty level!\n")
    #         print("Good luck!\n")
    #         return 3 
    #     elif userInputDifficulty == "m":
    #         print("You have chosen Medium difficulty level!\n")
    #         print("Good luck!\n")
    #         return 5
    #     elif userInputDifficulty == "h":
    #         print("You have chosen Hard difficulty level!\n")
    #         print("Good luck!\n")
    #         return 7
    #     else:
    #         print("Invalid input!")
    #         print("Please enter E, M or H!")
    #--------------------------------------------#

#################################################
#   This function calculates the score.         #
#################################################


def calculate_score(shape: Shape, score):

    shape_score = len(shape.table) * len(shape.table[0])
    return score + shape_score

#################################################
#   This is the main function.                  #
#################################################


    
def main():
    # rules()
    blocker_locations = blockers(5)
    puzzle = Puzzle(blocker_locations)
    print(puzzle)
    score = 0
    start = time.perf_counter()
    while True:
        shape, s_letter = shaper()
        rotate_shape(shape, s_letter)
        print(puzzle)
        shape_draw(shape, puzzle, s_letter)
        print(puzzle)
        score += calculate_score(shape, score)
        if prompt_quit():
            break
    end = time.perf_counter()
    total_time = end - start
    print(f"Your time is {total_time:2f} seconds!")
    if total_time > 180 and score > 0:
        score -= 500
    else:
        score += 500
    
    print(f"Your score is {score}!")
    
if __name__ == "__main__":
    main()