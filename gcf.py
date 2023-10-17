number1 = int(input("What is Number 1?: "))
number2 = int(input("What is Number 2?: "))

def gcf(x, y):
    while y:
        x, y = y, x % y
    return x
print(f"The Greatest Common Factor of {number1} and {number2} is " +str(gcf(number1, number2)))