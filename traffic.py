westbound:bool
eastbound:bool

def traffic(x, y):
    print(x)
    print(y)
    if westbound==True and eastbound==True:
        print("False")
    elif westbound==True and eastbound==False:
        print("True")
    elif westbound==False and eastbound==True:
        print("True")
    elif westbound==False and eastbound==False:
        print("True")
traffic()