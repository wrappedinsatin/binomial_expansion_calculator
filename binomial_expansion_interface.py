from polynomial_expressions_inputs import inputs
from polynomial_expression_calculator import expression, expression_parts

def main():
    n, a, b, rounder = inputs()
    coefs = expression(n, a, b, rounder)
    variables = expression_parts(coefs)

    string = ""
    for variable in expression_parts(coefs):
        string += variable + ' + '
    string = string.rstrip(' + ')

    print(f"n value: {n}")
    print(f"a value: {a}")
    print(f"b value: {b}")
    print(f"Rounded to {rounder} digit(s)\n")
    print("Your polynomial expression is " + string)

if __name__ == '__main__':
    main()