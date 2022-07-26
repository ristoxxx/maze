from pyamaze import maze,agent
# m=maze(20,20)
# m.CreateMaze()
# a=agent(m,filled=True,footprints=True)
# m.tracePath({a:m.path})
m=maze()
m.CreateMaze(2,2,loadMaze="maze2.csv")
m.run()
