#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
char buffer[64];
if (argc < 2)
{
printf("ERROR - Vy dolzhny predostavit kak minimum odin argument\n");
return 1;
}
strcpy(buffer, argv[1]);
return 0;
}
