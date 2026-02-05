
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
