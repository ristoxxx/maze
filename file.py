#filereader
from xml.etree.ElementTree import tostring


f = open("maze11.txt", "r")
#print(f.readline())
#print(f.readline())
a=0
uusi=""
for x in f:
    a = a+1
    b=0
    for y in x:
        b = b+1
        if y=="#":
            y = 0,0,0,0
        else:
            y = 1,1,1,1
        uusi=(a,b,y)
        print(uusi)
    
print(uusi)
f.close()