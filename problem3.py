#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

biggestFactor = 0

for x in range(1, 13195): #cant loop through 600851475143
    if x / 2 or x / 3 != 0:
        y = 13195 % x
        if y == 0:
            primeFactor = x
            if primeFactor > biggestFactor:
                biggestFactor = primeFactor
print(biggestFactor)
