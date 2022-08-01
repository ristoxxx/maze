#filereader
from xml.etree.ElementTree import tostring


f = open("maze22.txt", "r")
a=0
uusi=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
ulos=[]
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
            y =  "c"
            ulos.append(a)
            ulos.append(b)
            uusi[a-1].append(y)
        
        else:
            y = "c"
            uusi[a-1].append(y)
            
        
    #uusi = uusi + "\n"
maze = uusi    
print(maze[13][37])
print(ulos)
f.close()
# maze = [
#         ['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
#          'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
#         ['w', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c',
#          'c', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
#         ['w', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
#          'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
#         ['w', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
#          'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
#         ['w', 'w', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'w', 'w',
#          'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'w', 'c', 'w'],
#         ['w', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c',
#          'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'w'],
#         ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'c', 'c', 'w', 'c', 'w', 'w',
#          'w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
#         ['w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c',
#          'w', 'w', 'w', 'w', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
#         ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'c', 'w', 'c',
#          'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'w'],
#         ['w', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c',
#          'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'w'],
#         ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
#          'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']
#     ]
# print(maze)

