def factors(x,y):
        if x >= y:
                if x % y == 0:
                    print(y)
                    y = y+1
                    factors(x,y)
                else:
                       y=y+1
                       factors(x,y)
factors(997)