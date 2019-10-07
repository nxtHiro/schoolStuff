// Marco Flores
// Basically need to redo

#include <stdio.h>
#include <unistd.h>
#include <limits.h>
#include <sys/wait.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

     if(argc != 2){
          printf("Please pass exactly one directory.\n");
          return -1;
     }

     char cwd[PATH_MAX];

     if(getcwd(cwd, sizeof(cwd)) != NULL){
          printf("Current working directory: %s\n", cwd);
     }
     else{
          printf("getcwd() error");
          return -1;
     }
     int chdirRet = chdir(argv[1]);
     printf("Executing ls %s --all -l --human-readable\n", argv[1]);


     if (chdirRet == 0){

          char *lsArgs[5];
          lsArgs[0] = "/bin/ls";
          lsArgs[1] = "--all";
          lsArgs[2] = "-l";
          lsArgs[3] = "--human-readable";
          lsArgs[4] = NULL;

          int pid = fork();
          int *status;

          if(pid == 0){
               execv(lsArgs[0],lsArgs);
               exit(0);
          }
          wait(status);
          printf("%d", pid);
          printf("Exit status: 0\n");
     }
     else{
          printf("Can't chdir to %s\nExit status: 1\n", argv[1]);
     }
}
