#Lab 2 - Antaine O Conghaile - G00347577
# Adapted from https://tour.golang.org/flowcontrol/8
def sqrt(x):
    z = 1.0
    #Keep getting better estimate for the square root
    #of x, until you are within two decimal places.
    while abs(z*z - x)>= 0.01:
        #Get a better approximation for the square root.
        z -= (z*z - x) / (2*z)
    return z

    #Calculate Suare root & print it
z = sqrt(float(input()))
#print z
print(z)
print(z*z)
