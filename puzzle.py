import sudoku

def invalid_puzzle(puzzle) -> bool:
    '''
        checks if input is correct with respects to the puzzle
    '''
    #checks if row, col, and subgrid have a repeated number
    col_veri = sudoku.check_columns(puzzle)
    row_veri = sudoku.check_rows(puzzle)
    sub_veri = sudoku.check_rows(sudoku.check_subgrids(puzzle))
    if len(col_veri) > 0 or len(row_veri) > 0 or len(sub_veri) > 0: #if none of the veri has a repeated number in their domain return False
        return True
    else:
        return False

def space(puzzle) -> list:
    '''
        turns zeros into spaces
    '''
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                puzzle[i][j] = ' '

    return puzzle
    
def checkForSpace(row, column, puzzle) -> bool:
    '''
        Checks if the given inputs are valid and can't change indexes that aren't spaces
    '''
    print(puzzle[row])
    if puzzle[row][column] == ' ':
        return True
    else:
        return False

def finished(puzzle) -> bool:
    '''
        checks if puzzle is filled out
    '''
    counter = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == ' ':
                counter += 1
    if counter > 0: #checks if there are any spaces left in the puzzle
        return False
    else:
        return True

def main():

    total_numbers = 0 #gets how much numbers are inputed
    invalid_count = 0 #gets how many incorrect numbers are inputed

    while(1):
        board = input('Please enter your sudoku puzzle file: ')
        puzzle = space(sudoku.load_puzzle(board))
        if invalid_puzzle(puzzle):
            print('Please provide a valid sudoku puzzle file')
        else:
            break
    
    while(1): #loops the puzzle to enable input until  user quits

        print("Current Grid")
        print(sudoku.puzzle_to_string(puzzle))
        
        if finished(puzzle): #check if no spaces are left
            print('Game has ended.')
            print('Puzzle is complete.')
            print(f'You entered {total_numbers} numbers in total')
            print(f'You entered {invalid_count} invalid numbers')
            break

        while(1): #validates if input is correct
            puz = input('Enter as "<row>,<col>,<number>" where <..> is an integer from 1-9. (quit to exit): ')
            if puz == 'quit':
                break  

            mark = puz.split(',') #splits input into a list of 3 ints
            for i in range(len(mark)-1):
                mark[i] = int(mark[i])
                
            if checkForSpace(mark[0]-1, mark[1]-1, puzzle): #checks if input is correct
                puzzle[mark[0]-1][mark[1]-1] = mark[2]
                total_numbers += 1
                if invalid_puzzle(puzzle):
                    puzzle[mark[0]-1][mark[1]-1] = ' '
                    invalid_count += 1
                else:
                    break
                    
            else:
                total_numbers += 1
                invalid_count += 1
                print("Value entered was invalid, try again")
        
        if puz == 'quit': #checks if user wants to quit
            print('Game has ended.')
            print('Puzzle is NOT completed.')
            print(f'You entered {total_numbers} numbers in total')
            print(f'You entered {invalid_count} invalid numbers')
            break
        



if __name__ == "__main__":
    main()





