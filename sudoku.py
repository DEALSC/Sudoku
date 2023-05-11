'''
COMP 1405 - Fall 2020
Assignment #3
Name: Loc Binh 
'''

#------------------------------------------------------------------#
# provided function - do NOT remove or change
def load_puzzle(filename):
    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open(filename, "r") as f:
        for line in f:
            puzzle.append( [int(val) for val in line.split(",")] )
    return puzzle


#------------------------------------------------------------------#
#------------------------------------------------------------------#


# your functions go here!
def puzzle_layout():
    '''
        This is to help with the puzzle_to_string function, this function builds the borders for a 9x9 matrix
    '''
    layout1 = [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ',' ']*3
    layout2 = ['-','-','-','-','-','-','+','-','-','-','-','-','-','-','+','-','-','-','-','-','-'] 
    final_layout = layout1 + layout2 + layout1 + layout2 + layout1
    return final_layout

def puzzle_to_string(puzzle):
    '''
        turns puzzle into string and renders it
    '''
    hold = '' #will contain the listed list all in one string

    for i in range(9):
        for j in range(9):
            hold += str(puzzle[i][j])

    layout = puzzle_layout() #board for matrix

    counter = 0 #counter to loadup the layout
    spaceCount = 0 #to format the puzzle
    
    for i in range(len(layout)): #formatting the puzzle

        if counter == len(hold):
            break

        if i%21 == 0:
            spaceCount = 0
        
        if layout[i] == '|':
            spaceCount = 1
        
        if layout[i] == '-':
            spaceCount = 0
        
        if layout[i] == ' ':
            if spaceCount == 1:
                spaceCount = 0
                continue
            
            if hold[counter] == '0':
                spaceCount = spaceCount + 1
                counter = counter + 1
                continue
            
            layout[i] = hold[counter]
            counter = counter + 1
            spaceCount = spaceCount + 1
        

            

    hold2 = '' #will display the puzzle as a proper string

    for i in range(len(layout)):
        if i%21 == 0: #mapped out 21 indexes in 1 row to form 'the proper output'
            hold2 += '\n'
        hold2 += layout[i]

    return hold2

def check_rows(puzzle):
    '''
        check rows for repeated numbers 
    '''
    
    intList = [] #used to return which rows are invalid

    for i in range(len(puzzle)): #iterates 9 times to check every row
        doubleCheck = [] #for checking if row has same number more than once
        for j in range(len(puzzle[i])): #iterates 81 times to check every number
            if puzzle[i][j] != ' ' and puzzle[i][j] in doubleCheck:
                intList.append(i+1)
                break 
            doubleCheck.append(str(puzzle[i][j]))
            
    return intList


def check_columns(puzzle):
    '''
        check columns for repeated numbers
    '''

    intList = [] #used to return which columns are invalid

    for i in range(len(puzzle)): #iterates 9 times to check every columns
 
        doubleCheck = [] #for checking if columns has same number more than once
        for j in range(len(puzzle[i])): #iterates 81 times to check every number    
            if puzzle[j][i] != ' ' and puzzle[j][i] in doubleCheck:
                intList.append(i+1)
                break 
            doubleCheck.append(str(puzzle[j][i]))
                    
    return intList


def check_subgrids(puzzle):

    intList = [] #used for storing list of listed subgrids

    x_axis = 0 
    y_axis = 0
    
    for i in range(len(puzzle)): #iterates 9 times; one for each subgrid

        if i > 0: #if subgrid row number is [0-2 add 0], if [3-5 add 3] and if [6-8 add 6] to x_axis. If subgrid number %3 == 0, reset x_axis to 0 
            x_axis += 3
            if i % 3 == 0:
                x_axis = 0
    
        intList.append([]) #creates a new list everytime we move onto the next subgrid       

        if i%3 == 0 and i != 0: #if subgrid column number is [0-2 add 0], if [3-5 add 3] and if [6-8 add 6] to y_axis
            y_axis += 3 

        for j in range(3): #iterates 27 times for every row in every subgrid
            for k in range(3): #itertaes 81 times for every number in every subgrid
                intList[i].append(puzzle[j + y_axis][k + x_axis]) #appends subgrid indexes into the current list

    return intList #returns the listed list of subgrids

#------------------------------------------------------------------#
#------------------------------------------------------------------#


#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed to test your functions
def main():
    puzzle = load_puzzle('test.txt')
    print(puzzle_to_string(puzzle))
    print(f'\nChecking for invalid rows {check_rows(puzzle)}')
    print(f'\nChecking for invalid columns {check_columns(puzzle)}')
    print(f'\nChecking for invalid subgrids {check_rows(check_subgrids(puzzle))}')



#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()