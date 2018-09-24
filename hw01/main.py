for a in range(1,10):
    for c in range(1,a):
        print (end="       ")
    for b in range(a,10):
            print("{}*{}={:<2d}" .format(a,b,a*b),end=" ")
    print (" ")

