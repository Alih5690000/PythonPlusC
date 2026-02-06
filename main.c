#include <string.h>
#include <stdlib.h>

//gcc -shared -o lib.so -fPIC main.c

int add(int a,int b){
    return a+b;
}

typedef struct{
    int x,y;
} Point;

void Point_move(Point* o, int dx, int dy){
    o->x+=dx;
    o->y+=dy;
}

int stoi(const char* str,int* res){
    size_t len=strlen(str);
    *res=0;
    for (int i=0;i<len;i++){
        if (str[i]<'0' || str[i]>'9')
            return -1;
        *res*=10;
        *res+=str[i]-'0';
    }
    return 0;
}

typedef struct{
    int size;
    int* data;
} ArrayInt;

void ArrayInt_init(ArrayInt* o,int size){
    o->size=size;
    o->data=malloc(sizeof(int)*size);
}

int* ArrayInt_data(ArrayInt* o){
    return o->data;
}

int sumof(int* a,int size){
    int sum=0;
    for (int i=0;i<size;i++){
        sum+=a[i];
    }
    return sum;
}
