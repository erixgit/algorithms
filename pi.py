import math

def calc_pi():
    # Your Code Here
    
    k = 0
    p = 0
    s = 0
    
    while (True):
        a = 2*math.sqrt(2)/9801
        b = math.factorial(4*k)*(1103 + 26390*k)
        c = math.factorial(k)**4*396**(4*k)
        s = a*b/c
        p += s
        if s < 10**-15:
            break
        else:
            k += 1
    
    return 1/p
