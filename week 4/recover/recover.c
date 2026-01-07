#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    unsigned char buffer[512];
    FILE *output = NULL;
    int jpg_count = 0;
    char filename[8];

    while (fread(buffer, 1, 512, input) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output != NULL)
            {
                fclose(output);
            }

            sprintf(filename, "%03i.jpg", jpg_count);
            output = fopen(filename, "w");
            jpg_count++;
        }

        if (output != NULL)
        {
            fwrite(buffer, 1, 512, output);
        }
    }

    if (output != NULL)
    {
        fclose(output);
    }

    fclose(input);
    return 0;
}
