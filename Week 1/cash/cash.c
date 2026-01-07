#include <cs50.h>
#include <stdio.h>

int change(int n)
{
    int coins = 0;

    coins += n / 25;
    n %= 25;

    coins += n / 10;
    n %= 10;

    coins += n / 5;
    n %= 5;

    coins += n;

    printf("%i\n", coins);

}

int main()
{
    int cash;
    do
    {
        cash = get_int("Change Owned : ");
        change(cash);
    }while(cash < 0);
}
