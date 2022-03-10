def g_console(array):
    """Given an array it nicely prints and formats it on the console."""
    for i in array:
        for j in i:
            if len(j)==2:
                print(j, end="")
            else:
                print(j+" ", end="")
        print("")
