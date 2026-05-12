
from sympy import binomial

def expression(n, a, b, rounder):
    coefs = []
    for r in range(n+1):
        coefs.append(binomial(n, r) * a**(n-r) * b**r)
    for coef in coefs:
        round(coef, rounder)
    return coefs

def expression_parts(coefs: list):
    variables = []
    for index, coef in enumerate(coefs):
        variable = str(coef) + 'x' + str(len(coefs)-index-1)
        variables.append(variable)
    return variables
