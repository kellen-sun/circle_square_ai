import random
def generate_rectangle():
    '''Generates a random circle in a 32 by 32 grid marked by 1'''
    # generates the 32 by 32 grid
    grid = [[0 for i in range(32)] for j in range(32)]
    #randomly generates the coordinates for the top left and bottom right corners of the rectangle
    x1 = random.randint(10,22)
    y1 = random.randint(10,22)
    x2 = random.randint(5,9)
    y2 = random.randint(5,9)
    for i in range(32):
        for j in range(32):
            if i<=x1+x2 and i>=x1-x2:
                if j<=y1+y2 and j>=y1-y2:
                    grid[i][j]=1
    return grid

def generate_circle():
    """Generates a random circle in a 32x32 grid. (marked with -1)"""
    array=[[0]*32 for i in range(32)]
    x=random.randint(10,22)
    y=random.randint(10,22)
    r=random.uniform(7.38, 9.456)
    for i in range(len(array)):
        for j in range(len(array)):
            if (i-x)**2+(j-x)**2<=r**2:
                array[i][j]=-1
    return array

def g_console(array):
    """Given an array it nicely prints and formats it on the console."""
    string = ''
    for i in array:
        for j in i:
            if len(str(j))==2:
                string = string+str(j)+' '
                #print(j, end="")
            else:
                string = string+str(j)+" "
                #print(str(j)+" ", end="")
        string =string+'\n'
    string = string+'\n'
        #print("")
    return string

f = open("training_data.txt", "w")
for i in range(300):
    rectangle = generate_rectangle()
    circle = generate_circle()
    f.write(g_console(rectangle))
    f.write(g_console(circle))
f.close()
f = open("test_data.txt", "w")
for i in range(20):
    rectangle = generate_rectangle()
    circle = generate_circle()
    f.write(g_console(rectangle))
    f.write(g_console(circle))
f.close()


model=[[0]*32 for i in range(32)]
with open('training_data.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
    line=list(map(int, lines[i].split()))
    #print(line)
    for j in range(len(line)):
        model[(i%33)-1][j]+=line[j]
f=open("model.txt", "w")
f.write(g_console(model))
f.close()
