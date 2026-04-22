def survival(T):
    """
    Determine if the organism will survive or not
    
    Argument:
        T: integer
    Return:
        result: bool
    """
    # organism will survive only on integer coordinates :- (0,0),(0,1),....(5,5).=36points.
    #organism survive when there exists atleast one point :- f(x,y) <= T

    for i in range(6):
        for j in range(6):
            temp = 30 + i**2 + j**2 -3*i - 4*j
            if temp <= T:
                return True
    return False

print(survival(30))