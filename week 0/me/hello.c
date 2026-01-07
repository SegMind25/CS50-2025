#include <cs50.h>
#include <stdio.h>


int main()
{
    string name = get_string("Hello, What's Your Name ? : ");
    printf("Hello, %s\n", name);
}
