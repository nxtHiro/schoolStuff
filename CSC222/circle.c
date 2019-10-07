#include <stdio.h>

const float pi = 3.1415;

int main(void){

  float area;
  float cir;
  float rad;

  printf("Enter radius: \n");
  scanf("%f", &rad);

  area = pi * rad * rad;
  cir = 2 * rad * pi;

  printf("The area is %f. The circumference is %f.\n", area, cir);

  return 0;
}
