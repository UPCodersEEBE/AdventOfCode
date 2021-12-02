#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char const *const fileName = "input.dat";
    FILE *file = fopen(fileName, "r");
    char line[256];

    int64_t depth = 0;
    int32_t horiontal_pos = 0;
    int64_t aim = 0;
    while (!feof(file))
    {
        fgets(line, sizeof(line), file);

        switch (line[0])
        {
        case 'u':
            aim -= atoi(line + 3);
            break;
        case 'd':
            aim += atoi(line + 5);
            break;
        case 'f':
            horiontal_pos += atoi(line + 8);
            depth += aim * atoi(line + 8);
            break;
        default:
            printf("ERROR, invalid token%c", line[0]);
            break;
        }
    }

    fclose(file);
    printf("Result = %lld\n", (int64_t)(horiontal_pos * depth));
    return 0;
}