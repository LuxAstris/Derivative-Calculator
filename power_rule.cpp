#include <iostream>
#include <cmath>

using namespace std;

float x;

float coeff;

float n;

float C;

float constant_rule;

float power_rule;

int specific_function;

float constant()
{
    cout << "Welcome to the constant multiple rule.\n";

    cout << "Enter in the value of x, the coefficient of x";

    cin >> x >> coeff;

    constant_rule = coeff;

    cout << " The derivative of your function evaluated at the given value x is " <<constant_rule;

    return constant_rule;
}

float power()
{
    cout << "Welcome to the power rule.\n";

    cout << "Enter in the value of x, the coefficient of x, and the exponent of x";

    cin >> x >> coeff >> n ;

    power_rule = coeff * n * pow(x, n-1);

    cout << " The derivative of your function evaluated at the given value x is " << power_rule;

    return power_rule;
}

int main()
{
    cout << "Which derivative rule would you like to use? : \n" << "1 Constant Multiple Rule \n 2 Power Rule";

    cin >> specific_function;

    if(specific_function == 1){
      constant();
    }

    else{
        power();
    }

}
