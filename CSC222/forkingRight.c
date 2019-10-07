// Forking assignment
//   by: Marco Flores
//      5 February 2019

#include <stdio.h>
#include <unistd.h>
#include <limits.h>
#include <sys/wait.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

     if(argc != 2){
          printf("Usage: ./forkingRight <dir>\n");
          exit(1);
     }

     char cwd[PATH_MAX]; // current working directory

     int chdirRet; // chdir() return value

     int *status; // child process status
     status = malloc(sizeof(int)); // allocates memory to status pointer

     int pid = fork(); // generates child process

     if(pid == 0){
          if(getcwd(cwd, sizeof(cwd)) != NULL){
               printf("Current working directory: %s\n", cwd); // prints current working directory after obtaining it
          }
          else{
               printf("getcwd() error");
               exit(1);
          }

          chdirRet = chdir(argv[1]); // attempts to change directory

          printf("Executing ls %s --all -l --human-readable\n", argv[1]);

          if(chdirRet == 0){ // if chdir() is successful
               char *lsArgs[5]; // execv() char array for ls
               lsArgs[0] = "/bin/ls"; // assigning each argument
               lsArgs[1] = "--all";
               lsArgs[2] = "-l";
               lsArgs[3] = "--human-readable";
               lsArgs[4] = NULL; // must be null terminated

               execv(lsArgs[0], lsArgs); // executes "ls --all -l --human-readable" on the current working directory
          }
          else{
               printf("Can't chdir to %s\n", argv[1]); // chdir error handling
               exit(1);
          }

          exit(0); // everything is successful
     }

     waitpid(pid, status, 0); // parent process waits for child process to finish

     printf("Exit status: %d\n", WEXITSTATUS(*status)); // prints child process exit status

}
