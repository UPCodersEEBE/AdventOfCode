#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char const *const fileName = "input.dat";
    FILE *file = fopen(fileName, "r");
    char line[256];

    int32_t depth = 0;
    int32_t horizontal_pos = 0;
    while (!feof(file))
    {
        fgets(line, sizeof(line), file);

        switch (line[0])
        {
        case 'u':
            depth -= atoi(line + 3);
            break;
        case 'd':
            depth += atoi(line + 5);
            break;
        case 'f':
            horizontal_pos += atoi(line + 8);
            break;
        default:
            printf("ERROR, invalid token%c", line[0]);
            break;
        }
    }

    fclose(file);
    printf("Result = %lld\n", (int64_t)(horizontal_pos * depth));
    return 0;
}