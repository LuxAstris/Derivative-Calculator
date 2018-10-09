def chain():

    print('Welcome the the Chain Rule sub complex. The Chain Rule is given by dx/dy f(g(x))= d/dx f(g(x)) * d/dx g(x).')

    B = int(input('''What Rule will differentiate g(x)
                        Enter 1 for the constant multiple rule
                        Enter 2 for the power rule
                        Enter 3 for the product rule
                        Enter 4 for the quotient rule'''))

    if A == 1:

        constant_multiple()

        H_prime = constant_multiple()

    elif A == 2:

        power()

        H_prime = power()

    elif A == 3:

        product()

        H_prime = product()

    elif A == 4:

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