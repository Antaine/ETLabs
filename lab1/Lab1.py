#Lab 1 - Antaine O'Conghaile
#Collatz Conjecture

#Take Nuber in
n = int(input("Enter a Int: "))

while n != 1:
    #Print current value of n
    print(n)
    #Check if n is even
    if n%2 == 0:
        n //= 2
    #Check if n = odd
    else:
        n = (3*n) + 1

#Final value is 1 - Collatz Conjecture True
if(n == 1):print("Collatz is true! n =",n)
#Final value is not 1 - Collatz Conjecture False
else:print("Collatz is not true n =",n)