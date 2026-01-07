
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string key_str = argv[1];
    for (int i = 0, len = strlen(key_str); i < len; i++)
    {
        if (!isdigit(key_str[i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(key_str);

    string plaintext = get_string("plaintext: ");


    printf("ciphertext: ");
    for (int i = 0, len = strlen(plaintext); i < len; i++)
    {
        char c = plaintext[i];

        if (isalpha(c))
        {
            if (isupper(c))
            {
                char encrypted = ((c - 'A' + key) % 26) + 'A';
                printf("%c", encrypted);
            }
            else
            {
                char encrypted = ((c - 'a' + key) % 26) + 'a';
                printf("%c", encrypted);
            }
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");

    return 0;
}
