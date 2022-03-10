import random
def rectangle():
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
    print(grid)

rectangle()
