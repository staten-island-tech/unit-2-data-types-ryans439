westbound:bool
eastbound:bool

def traffic(x, y):
    print(x)
    print(y)
    if x==True and y==True:
        print("False")
    elif x==True and y==False:
        print("True")
    elif x==False and y==True:
        print("True")
    elif x==False and y==False:
        print("True")
traffic(True, False)