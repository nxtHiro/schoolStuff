#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

int main(int argc, char **argv){

     if(argc < 2){
          printf("Usage ./final <bash_script> args %d\n", argc);
          exit(1);
     }


     int *status;
     status = malloc(sizeof(int));

     int pid = fork();
     if(pid == 0){
          printf("Child PID: %d\n\nBash file execution output: \n", getpid());
          execvp(argv[1], argv);
     }
     wait(NULL);
     printf("\n");
     
     return 0;
}


