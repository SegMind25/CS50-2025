#include <cs50.h>
#include <stdio.h>

void printhash(int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int space = 0; space < n - i - 1; space++)
        {
            printf(" ");
        }

        for(int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}

int main()
{
    int numpyramids;
    do{
        numpyramids = get_int("Enter The Height Of Pyramids : ");
        printhash(numpyramids);
    }while(numpyramids < 1);
}
