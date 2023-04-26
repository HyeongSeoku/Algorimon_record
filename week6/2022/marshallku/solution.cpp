#include <cstdio>
#include <algorithm>
#include <cmath>

const double TOLERANCE = 1e-6;

int main()
{
    double x, y, c;
    scanf("%lf %lf %lf", &x, &y, &c);

    double min = 0;
    double max = std::min(x, y);

    while (TOLERANCE < max - min)
    {
        double mid = (max + min) / 2;
        double p = std::sqrt(x * x - mid * mid);
        double q = std::sqrt(y * y - mid * mid);

        if (c <= (p * q) / (p + q))
            min = mid;
        else
            max = mid;
    }

    printf("%.3lf\n", min);
    return 0;
}