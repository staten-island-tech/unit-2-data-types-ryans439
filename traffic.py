westbound:bool
eastbound:bool
x=("Is there westbound traffic?")
y=("Is there eastbound traffic?")
def traffic():
    if westbound==True and eastbound==True:
        print("False")
    elif westbound==True and eastbound==False:
        print("True")
    elif westbound==False and eastbound==True:
        print("True")
    elif westbound==False and eastbound==False:
        print("True")
traffic(x)