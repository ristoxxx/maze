from pyamaze import maze,agent,COLOR
from sys import argv

#list_of_args = argv

#filename = (list_of_args[1])
filename = "maze4.csv"

def RCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=[v[-1]]+v[:-1]
    direction=dict(zip(k,v_rotated))

def RCCW():
    global direction
    k=list(direction.keys())
    v=list(direction.values())
    v_rotated=v[1:]+[v[0]]
    direction=dict(zip(k,v_rotated))

def moveForward(cell):
    if direction['forward']=='E':
        return (cell[0],cell[1]+1),'E'
    if direction['forward']=='W':
        return (cell[0],cell[1]-1),'W'
    if direction['forward']=='N':
        return (cell[0]-1,cell[1]),'N'
    if direction['forward']=='S':
        return (cell[0]+1,cell[1]),'S'

def wallFollower(m):
    global direction
    direction={'forward':'N','left':'W','back':'S','right':'E'}
    currCell=(m.rows,m.cols)
    path=''
    while True:
        if len(path)>200:
            break
        
        if currCell==(1,1):
            break
        if m.maze_map[currCell][direction['left']]==0:
            if m.maze_map[currCell][direction['forward']]==0:
                RCW()
            else:
                currCell,d=moveForward(currCell)
                path+=d
        else:
            RCCW()
            currCell,d=moveForward(currCell)
            path+=d
    path2=path
    while 'EW' in path2 or 'WE' in path2 or 'NS' in path2 or 'SN' in path2:
        path2=path2.replace('EW','')
        path2=path2.replace('WE','')
        path2=path2.replace('NS','')
        path2=path2.replace('SN','')
    return path,path2
        


if __name__=='__main__':
    myMaze=maze()
    #myMaze.CreateMaze(2,8,loadMaze=filename)
    myMaze.CreateMaze(2,8)
    # a=agent(myMaze,shape='arrow',footprints=True)
    b=agent(myMaze,shape='arrow',color=COLOR.yellow,footprints=True)
    path,path2=wallFollower(myMaze)
    # myMaze.tracePath({a:path})
    myMaze.tracePath({b:path2})
    
    if len(path)>20:
            print("20 steps is not enouhg")
    if len(path)>150:
            print("150 steps is not enouhg")
    if len(path)>200:
            print("200 steps is not enouhg")
            
    print("Final steps count: ",len(path))
    print("Final route: ",path)
    
    myMaze.run()