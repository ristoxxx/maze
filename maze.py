from colorama import Fore
import sys

#route visualisation/print + count moves
def maze_solver():
    path = 0
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end=" ")
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end=" ")
            elif maze[i][j] == 'p':
                print(Fore.BLUE, f'{maze[i][j]}', end=" ")
                path = path + 1                             #count moves
            else:
                print(Fore.RED, f'{maze[i][j]}', end=" ")
        print('\n')
    print(Fore.WHITE)
    print("Path length: ",path)

#route finder
def escape():
    current_cell = rat_path[len(rat_path) - 1]

    if current_cell == finish:
        return
    
    if maze[current_cell[0] - 1][current_cell[1]] == 'c':
        maze[current_cell[0] - 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] - 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] - 1] == 'c':
        maze[current_cell[0]][current_cell[1] - 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] - 1])
        escape()
        
    if maze[current_cell[0] + 1][current_cell[1]] == 'c':
        maze[current_cell[0] + 1][current_cell[1]] = 'p'
        rat_path.append([current_cell[0] + 1, current_cell[1]])
        escape()

    if maze[current_cell[0]][current_cell[1] + 1] == 'c':
        maze[current_cell[0]][current_cell[1] + 1] = 'p'
        rat_path.append([current_cell[0], current_cell[1] + 1])
        escape()

    # If we get here, this means that we made a wrong decision, so we need to
    # backtrack
    current_cell = rat_path[len(rat_path) - 1]
    if current_cell != finish:
        cell_to_remove = rat_path[len(rat_path) - 1]
        rat_path.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = 'c'

if __name__ == '__main__':
    
    #read argumet from command
    list_of_args = sys.argv
    filename = (list_of_args[1])
    #filename = "maze22.txt" #for testing
    #Get_filename
    
    #opional filename imput
    #print("Enter maze filename: ") 
    #filename = input()
    
    # if (filename[-4:]) != ".txt":
    #     print("filetype must be .txt")
    #     print("Enter maze filename: ")
    #     filename = input()
        
    try:
        #read file and count lines
        with open(filename) as f:
            l = len(f.readlines())
        #Initialize a list for maze
        maze = []
        for i in range(l):
        # In each iteration, add an empty list to the main list
            maze.append([])

        # Open file to read characters to make maze
        with open(filename) as f:
            a=0
            ulos=[]             # Entrypoint of maze
            sisaan = []         # Exit point of maze
        
            for x in f:         #read maze file line by line
                a = a+1
                b=0
                for y in x:             #read line character by character and convert characters
                    b = b+1
                    if y=="#":          #mark all hastag as wall
                        y = "w"
                        maze[a-1].append(y)
                        
                    elif y == "\n":
                        y =  "\n"
                    
                    elif y == "E":      #find entrypoint
                        y =  "c"
                        ulos.append(a-1)
                        ulos.append(b-1)
                        maze[a-1].append(y)

                    elif y == "^":      #find exit point
                        y =  "c"
                        sisaan.append(a-1)
                        sisaan.append(b-1)
                        maze[a-1].append(y)
                    
                    else:               #mark all else as corridor
                        y = "c"
                        maze[a-1].append(y)
    except FileNotFoundError: 
        msg = ("Sorry, the file "+ filename + "does not exist.")
        print(msg)
        
    f.close()                           #close file
        
    start = sisaan
    finish = ulos
    maze[start[0]][start[1]] = 'p'

    rat_path = [start]      #set "rat" to starting point
    escape()                #find way to exit
    print(maze_solver())    #print maze and way to exit
    print(Fore.WHITE)
