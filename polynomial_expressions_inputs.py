def inputs():
    print("What is the degree of your polynomial?")
    n = int(input(">"))
    #coef = coefficient for variable x
    print("What is the coefficient for your variable x?")
    a = int(input(">"))
    print("What is the number next to your variable (type in 0 if none)")
    b = int(input(">"))
    print("To what degree do you want to round your coefficients?")
    rounder = int(input(">"))
    return n, a, b, rounder