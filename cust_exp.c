#include <stdio.h>



long long powr(long long base, int exp)
{
	int i;
	long long result = 1;
	for (i=0; i<exp; i++)
	{
		result = (result * base);
	}
	return result;
}

int main()
{
	//message = 4, n = 2*3=6
	long long enc = powr(7, 5)%6;

	printf("%lld..\n",enc);

	long long dec = powr(enc,11)%6;

	printf("%lld\n",dec);
	return 0;
}
