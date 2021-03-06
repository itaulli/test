#include <iostream>

int main()
{
    unsigned k;
    double sum = 0.f, old_sum = -1.f;

    for (k = 1; old_sum != sum; ++k)
    {
        old_sum = sum;
        sum += static_cast<double>(1)/k;
	if (k % 1000000 == 0)
	{
		std::cout << "k is " << k << ", sum is " << sum << '\n';	
	}
    }

    std::cout << "k is " << k << ", sum is " << sum << '\n';
    return 0;
}
