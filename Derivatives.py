
print("Welcome to the derivative calculator.")

specific_function = int(input('''Please specify the Derivative rule you need for the function:
                                1 Constant multiply Rule
                                2 Power Rule
                                3 Product Rule
                                4 Quotient Rule
                                5 Chain Rule'''))



def power():
    x = float(input("Enter in the x value for the function f(x)."))

    n = float(input("Enter in the value of the exponent in f(x)"))

    coefficient = float(input('Enter the coefficient of x in x ^ n'))

    power_rule = coefficient * n*x**(n-1)

    print("the derivative of f(x) is ")

    print(power_rule)

    return power_rule


def constant_multiple():
    x = float(input("Enter in the x value for the function f(x)."))

    coefficient1 = float(input("Enter the coefficient of x"))

    F1 = coefficient1 * x

    constant_rule = F1 = coefficient1

    print(constant_rule)

    return constant_rule


def product():
    x = float(input('Enter in the value of x upon which the function will be evaluated.'))

    A = int(input('''what is U for the Product Rule
                       Enter 1 for Power Rule function
                       Enter 2 for constant multiplier function'''))

    if A == 1:

        n = float(input("Enter in the value of the exponent in f(x)"))

        C = float(input("Enter in the value for the constant in f(x)"))

        coefficient1 = float(input("Enter the coefficient of x ^ n"))

        U = coefficient1 * x ** n + C

        U_prime = power

    else:

        coefficient1 = float(input("Enter the coefficient of x"))

        C = float(input("Enter in the value for the constant in f(x)"))

        U = coefficient1 * x + C

        U_prime = constant_multiple()

    B = int(input('''What type of function is G for the product rule
                                   Enter 1 for Power Rule function
                                   Enter 2 for constant multiplier function'''))

    if B == 1:

        n = float(input("Enter in the value of the exponent in g(x)"))

        C = float(input("Enter in the value for the constant in g(x)"))

        coefficient2 = float(input("Enter the coefficient of x ^ n"))

        G = coefficient2 * x ** n + C

        G_prime = n * coefficient2 * x ** (n - 1)

    else:

        coefficient2 = float(input("Enter the coefficient of x"))

        G = coefficient2 * x + C

        G_prime = coefficient2

    product_rule = U * G_prime + U_prime * G

    print(product_rule)

    return product_rule

def quotient():
    x = float(input('Enter in the value of x upon which the function will be evaluated.'))

    A = int(input('''what is U for the Product Rule
                       Enter 1 for Power Rule function
                       Enter 2 for constant multiplier function'''))

    if A == 1:

        n = float(input("Enter in the value of the exponent in f(x)"))

        C = float(input("Enter in the value for the constant in f(x)"))

        coefficient1 = float(input("Enter the coefficient of x ^ n"))

        U = coefficient1 * x ** n + C

        U_prime = n * coefficient1 * x ** (n - 1)


    else:

        coefficient1 = float(input("Enter the coefficient of x"))

        C = float(input("Enter in the value for the constant in f(x)"))

        U = coefficient1 * x + C

        U_prime = coefficient1

    B = int(input('''What type of function is G for the product rule
                                   Enter 1 for Power Rule function
                                   Enter 2 for constant multiplier function'''))

    if B == 1:

        n = float(input("Enter in the value of the exponent in g(x)"))

        C = float(input("Enter in the value for the constant in g(x)"))

        coefficient2 = float(input("Enter the coefficient of x ^ n"))

        G = coefficient2 * x ** n + C

        G_prime = n * coefficient2 * x ** (n - 1)

    else:

        coefficient2 = float(input("Enter the coefficient of x"))

        C = float(input("Enter in the value for the constant in f(x)"))

        G = coefficient2 * x + C

        G_prime = coefficient2

    quotient_rule = (U * G_prime - U_prime * G) / G ** 2

    print(quotient_rule)

    return quotient_rule


def chain():

    B = int(input('''What Rule will differentiate g(x)
                        Enter 1 for the constant multiple rule
                        Enter 2 for the power rule
                        Enter 3 for the product rule
                        Enter 4 for the quotient rule'''))

    if B == 1:

        constant_multiple()

        H_prime = constant_multiple()

    elif B == 2:

        power()

        H_prime = power()

    elif B == 3:

        product()

        H_prime = product()

    elif B == 4:

        quotient()

        H_prime = quotient
    else:

        print('Sorry, you entered an invalid input please try again.')

        chain()

    A = int(input('''What Rule will differentiate f(g(x))
                    Enter 1 for the constant multiple rule
                    Enter 2 for the power rule
                    Enter 3 for the product rule
                    Enter 4 for the quotient rule'''))

    if A == 1:

        constant_multiple()

        F_prime = contant_multiple() * H_prime

    elif A == 2:

        power()

        F_prime = power() * H_prime

    elif A == 3:

        product()

        F_prime = product() * H_prime

    elif A == 4:

        quotient()

        F_prime = quotient() * H_prime

    else:

        print('Sorry, you entered an invalid input please try again.')

        chain()

    chain_rule = F_prime * H_prime

    print(chain_rule)

    return chain_rule

if specific_function == 1:

    constant_multiple()

elif specific_function == 2:

    power()

elif specific_function == 3:

    print('Welcome to the Product Rule calculator. the Product rule is given by (dx/dy) U*G = U * d/dx G + d/dx U * G')

    product()

elif specific_function == 4:

    print('Welcome to the Quotient Rule calculator. The Quotient rule is given by the dx/dy U/G = (U * d/dx G - d/dx U * G)/ G**2 .')

    quotient()

elif specific_function == 5:

    print('Welcome to the Chain Rule calculator. The Chain Rule is given by dx/dy f(g(x))= d/dx f(g(x)) * d/dx g(x).')

    chain()


else:
    print('Sorry you entered an invalid input. Please try again')

