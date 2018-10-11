#include <iostream>
#include <cmath>

using namespace std;

float x;

float coeff;

float n;

float power_rule;



float power()
{
    cout << "Welcome to the power rule.\n";

    cout << "Enter in the value of x, the coefficient of x, and the exponent of x";

    cin >> x >> coeff >> n ;

    power_rule = coeff * n * pow(x, n-1);

    cout << power_rule;

    return power_rule;
}

int main()
{
    power();

}
