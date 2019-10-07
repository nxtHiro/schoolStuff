#include <stdio.h>
#include <unistd.h>
#include <limits.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int nani(char *fname){
     int ret = access( fname, F_OK );
     return ret;
}

int fileWrite(char *data, char *fileName){
     FILE *fp;

     fp = fopen(fileName, "w");
     fputs(data, fp);
     fclose(fp);
     return 0;
}

int main(){
     printf("%d", nani("README"));
     int ret = fileWrite("hi", "hi.txt");
     return 0;
}
