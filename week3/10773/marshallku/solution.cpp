#include <iostream>
#include <stack>

int main()
{
    int max, value;

    scanf("%d", &max);

    std::stack<int> stack;

    for (int i = 0; i < max; ++i)
    {
        scanf("%d", &value);

        if (value == 0)
        {
            stack.pop();
        }
        else
        {
            stack.push(value);
        }
    }

    int result = 0;

    while (!stack.empty())
    {
        result += stack.top();
        stack.pop();
    }

    printf("%d\n", result);

    return 0;
}