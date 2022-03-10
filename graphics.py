def g_console(array):
    """Given an array it nicely prints and formats it on the console."""
    for i in array:
        for j in i:
            if len(str(j))==2:
                print(j, end="")
            else:
                print(str(j)+" ", end="")
        print("")
