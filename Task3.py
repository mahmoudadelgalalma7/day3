import math

#Variables
x = int(input("From: "))
y = int(input("To: "))
numbers = list(range(1, 5000))

# Function
def check(x,y):
    for x in numbers:
        root = math.sqrt(x)
        if x <= y:
            if int(root + .5) ** 2 == x:
                print(x)
        else:
            break
check(x,y)



