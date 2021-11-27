#include <stdio.h>


int Hello()
{
    for(int i=0; i< 1000000; i++)
    {
        printf("hello \n");
    }
    return 0;
}

int NotHello()
{
    for(int i=0; i<1000000;i++ )
    {
        printf("Not hello~\n");
    }
}