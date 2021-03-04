import random as rd
import time as time

def cubicSequence():
    a = rd.randint(1,25)
    b = rd.randint(1,25)
    c = rd.randint(1,25)
    d = rd.randint(1,25)

    n = 1

    while n!=5:
        sequence1 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
        sequence2 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
        sequence3 = a*n**3 + b*n**2 + c*n + d
        n = n + 1
        
        sequence4 = a*n**3 + b*n**2 + c*n + d
        n = n + 1

    if n == 5:
        print ("Sequence:", sequence1, sequence2, sequence3, sequence4)

        time.sleep(5)

        print ("A:", a, "B:", b, "C:", c, "D:", d)


def quadSequence():
    a = 20
    b = 9
    c = 22

    n = 1

    while n!=7:
        sequence1 = a*n**2 + b*n + c
        n = n + 1
        
        sequence2 = a*n**2 + b*n + c
        n = n + 1
        
        sequence3 = a*n**2 + b*n + c
        n = n + 1
        
        sequence4 = a*n**2 + b*n + c
        n = n + 1

        sequence5 = a*n**2 + b*n + c
        n = n + 1

        sequence6 = a*n**2 + b*n + c
        n = n + 1


    if n == 7:
        print ("Sequence:", sequence1, sequence2, sequence3, sequence4, sequence5, sequence6)

        time.sleep(5)

        print ("A:", a, "B:", b, "C:", c)


def geometric():

    n = 1

    r = rd.randint(2, 7)

    a = r

    n = n + 1
    
    sequence1 = a*r**(n-1)
    n = n + 1

    sequence2 = a*r**(n-1)
    n = n + 1

    sequence3 = a*r**(n-1)
    n = n + 1

    sequence4 = a*r**(n-1)
    n = n + 1

    if n == 6:
        print ("Sequence:", a, sequence1, sequence2, sequence3, sequence4)

        time.sleep(5)

        print ("R:", r)

    
while True:
    sequence = input("A: Quadratic, B: Cubic, C: Geometric")

    if sequence == "A".lower():
        quadSequence()
        time.sleep(5)
        
    elif sequence == "B".lower():
        cubicSequence()
        time.sleep(5)

    elif sequence =="C".lower():
        geometric()
        time.sleep(1)
    
    else:
        print ("Enter a valid input")
