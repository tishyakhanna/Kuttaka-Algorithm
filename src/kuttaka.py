"""
Kuttaka Algorithm
@author Tishya Khanna
"""

#the Euclidean method to compute gcd
def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

#performs the division algorithm and stores the quotients and remainders in arrays
def division(x,y):
    quotients = []
    remainder = 0
    while(remainder!=1):
        quotients.append(x // y)
        remainder = x%y
        x,y=y,x%y
    print("The list of quotients is as follows: " + str(quotients))
    return quotients


#to check if the equation is a valid LDE
def check_if_valid_LDE(a,b,c):
    return (c % gcd(a,b)==0)

#kuttaka algorithm solver
def kuttaka_algorithm(A,B,C):
    A, B, C = abs(A), abs(B), abs(C)
    x, y = 0, C
    quot=division(A,B)
    print("The various iterations of x and y are: ")
    for i in range(0, len(quot)):
        x, y = y, quot[-(i + 1)] * y + x
        print(x,y)

    if len(quot) % 2 != 0:
        x, y = B - x, A - y

    #taking into account various cases
    # if a is negative
    if a < 0:
        x, y = -x, y
    # if b is negative
    if b < 0:
        x, y = x, -y
    # if c is negative
    if c < 0:
        x, y = B - x, A - y

    q = min(x // B, y // A)
    x, y = x - q * b, y - q * a

    return (x, y)



print("For the Linear Diophantine Equation in the form ax + c = by")
print("Enter the value of a: ")
a = int(input())
print("Enter the value of b: ")
b = int(input())
print("Enter the value of c: ")
c = int(input())

GCD = gcd(a,b)

if (check_if_valid_LDE(a,b,c)):
    a, b, c = a/GCD, b/GCD, c/GCD
    X,Y = kuttaka_algorithm(a,b,c)
    print("A particular solution is: ")
    print(X,Y)
    print("%d * %d + %d = %d = %d = %d * %d" % (a, X, c, a * X + c, b * Y, b, Y))
else:
    print("No solution since gcd(a,b) does not evenly divide c to give an integer.")
