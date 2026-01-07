#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    string text = get_string("Text: ");

    int letters = 0;
    int words = 0;
    int sentences = 0;

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        char c = text[i];
        if (isalpha(c))
        {
            letters++;
        }
        else if (c == ' ')
        {
            words++;
        }
        else if (c == '.' || c == '!' || c == '?')
        {
            sentences++;
        }
    }
    words++;

    if (words == 0)
    {
        printf("Before Grade 1\n");
        return 0;
    }

    float L = (float)letters / words * 100;
    float S = (float)sentences / words * 100;

    float index = 0.0588 * L - 0.296 * S - 15.8;

    int grade = (int) round(index);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}
