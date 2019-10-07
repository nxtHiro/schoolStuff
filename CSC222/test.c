#include <stdlib.h>
#include <stdio.h>

int main(){
     const char *name = "HOME";
     char *value;


     value = getenv(name);
     printf("%s", value);
}
