#include <iostream>
#include <cmath>

using namespace std;

float x, coeff, n, C, constant_rule, power_rule, product_rule, U, U_prime, G, G_prime;

int specific_function, a, b;

float constant()
{
    cout << "Welcome to the constant multiple rule.\n" << endl;

    cout << "Enter in the coefficient of x \n"<< endl;

    cin >> coeff;

    cout<< "Enter in the value of the constant (C) in the f(x) \n"<< endl;

    cin >> C;

    constant_rule = coeff;

    cout << " The derivative of your function evaluated at the given value x is " <<constant_rule <<"\n" << endl;

    return constant_rule;
}

float power()
{
    cout << "Welcome to the power rule.\n" << endl;

    cout << "Enter in the coefficient of x \n" << endl;

    cin >> coeff;

    cout << "Enter in the exponent of x \n" << endl;

    cin >> n;

    cout<< "Enter in the value of the constant (C) in the f(x) \n"<< endl;

    cin >> C;

    power_rule = coeff * n * pow(x, n-1);

    cout << " The derivative of your function evaluated at the given value x is " << power_rule<< "\n" << endl;

    return power_rule;
}

float product()
{
    cout << "Welcome to the product rule.\n Enter the function type for U \n 1 constant multiple \n 2 exponential" << endl;

    cin >> a;

    if(a == 1){

        U_prime = constant();

        U = coeff * x + C;
    }
    else{

        U_prime = power();

        U = coeff * pow(x,n) + C;
    }

    cout << "Welcome to the product rule.\n Enter the function type for G \n 1 constant multiple \n 2 exponential" << endl;

    cin >> b;

    if(b == 1){

        G_prime = constant();

        G = coeff * x + C;
    }
    else{

        G_prime = power();

        G = coeff * pow(x,n) + C;

    }

    product_rule = U * G_prime + U_prime * G;

    cout << "The answer to the derivative evaluated at x for your function derived from the product rule is " << product_rule << endl;

    return product_rule;

}


int main()
{

    cout << "Welcome to the derivative calculator. \n Enter in the value of x for which the derivative will be evaluated\n" << endl;

    cin >> x;

    cout << "Which derivative rule would you like to use? : \n" << "1 Constant Multiple Rule \n 2 Power Rule \n 3 Product Rule" << endl;

    cin >> specific_function;

    if(specific_function == 1){
      constant();
    }

    else{
            if(specific_function == 2){
                power();
            }
            else{
                if(specific_function == 3){
                    product();
                }
                else{
                    cout << "Please enter a valid input"<<endl;
                }
            }

    }

}
