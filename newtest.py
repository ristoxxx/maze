from colorama import Fore

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
                path = path + 1
            else:
                print(Fore.RED, f'{maze[i][j]}', end=" ")
        print('\n')
    print(Fore.WHITE)
    print("Path length: ",path)

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
    
    
    #read file and count lines
    filename = "maze22.txt"
    f = open(filename, "r")
    l = len(f.readlines())
    #print('Total lines:', l)
    #Initialize a list for maze
    uusi = []
    for i in range(l):
    # In each iteration, add an empty list to the main list
        uusi.append([])
    #print(uusi)
    
    f = open(filename, "r")
    a=0
    ulos=[]
    sisaan = []
    for x in f:
        a = a+1
        b=0
        for y in x:
            b = b+1
            if y=="#":
                y = "w"
                uusi[a-1].append(y)
                
            elif y == "\n":
                y =  "\n"
            
            elif y == "E":
                i=0
                if i < 1:
                    y =  "c"
                    ulos.append(a-1)
                    ulos.append(b-1)
                    uusi[a-1].append(y)
                    
                else:
                    y = "w"
                    uusi[a-1].append(y)

            elif y == "^":
                y =  "c"
                sisaan.append(a-1)
                sisaan.append(b-1)
                uusi[a-1].append(y)
            
            else:
                y = "c"
                uusi[a-1].append(y)
                
            
        #uusi = uusi + "\n"
    maze = uusi    
    #print(maze[13][37])
    #print(ulos)
    #print(sisaan)
    f.close()
    
    


    #start, finish = get_starting_finishing_points()
    start = sisaan
    finish = ulos
    maze[start[0]][start[1]] = 'p'

    rat_path = [start]
    escape()
    print(maze_solver())
    print(Fore.WHITE)
    
     #uusi=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    #vanha=[[]] * 20
    #uusi= vanha
    
    # maze = [
    #     ['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
    #      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    #     ['w', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c',
    #      'c', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
    #     ['w', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
    #      'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
    #     ['w', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
    #      'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
    #     ['w', 'w', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'w', 'w',
    #      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'w', 'c', 'w'],
    #     ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'c', 'c', 'w', 'c', 'w', 'w',
    #      'w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
    #     ['w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c',
    #      'w', 'w', 'w', 'w', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
    #     ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'c', 'w', 'c',
    #      'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'w'],
    #     ['w', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
    #      'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'w'],
    #     ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
    #      'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w'],
    # ]
    
    #def get_starting_finishing_points():
    #_start = [i for i in range(len(maze[0])) if maze[0][i] == 'c']
    #_end = [i for i in range(len(maze[0])) if maze[len(maze)-1][i] == 'c']
    #print([0, _start[0]], [len(maze) - 1, _end[0]])
    #return [0, _start[0]], [len(maze) - 1, _end[0]]
    #return [9,18],[13,37]
    #return[4,11],[9,24]