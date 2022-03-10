import random

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
    for i in array:
        for j in i:
            if len(str(j))==2:
                print(j, end="")
            else:
                print(str(j)+" ", end="")
        print("")
    return array
generate_circle()
