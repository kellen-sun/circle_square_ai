import random
def generate_rectangle():
    '''Generates a random circle in a 32 by 32 grid marked by 1'''
    # generates the 32 by 32 grid
    grid = [[0 for i in range(32)] for j in range(32)]
    #randomly generates the coordinates for the top left and bottom right corners of the rectangle
    x1 = random.randint(0,31)
    y1 = random.randint(0,31)
    x2 = random.randint(0,31)
    y2 = random.randint(0,31)

    for i in range(32):
        if i>=min(x1,x2) and i<=max(x1,x2):
            for j in range(32):
                if j>=min(y1,y2) and j<=max(y1,y2):
                    grid[i][j] = 1
    return grid

def generate_circle():
    """Generates a random circle in a 32x32 grid. (marked with -1)"""
    array=[[0]*32 for i in range(32)]
    x=random.randint(10,22)
    y=random.randint(10,22)
    r=random.randint(6,10)
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
                string = string+str(j)
                #print(j, end="")
            else:
                string = string+str(j)+" "
                #print(str(j)+" ", end="")
        string =string+'\n'
        #print("")
    return string

f = open("training_data.txt", "w")
for i in range(10):
    rectangle = generate_rectangle()
    circle = generate_circle()
    #f.write(g_console(generate_rectangle()))
    f.write(g_console(circle))
f.close()
