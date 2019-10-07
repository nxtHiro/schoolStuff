#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <string.h> 
#include <time.h>

int main(int argc, char **argv){

     if(argc != 2){
          printf("Usage ./two <script>\n e.g., ./two one.sh\n");
          exit(1);
     }

     srand(time(NULL));

     int pid = fork();
     if(pid == 0){

          char *execArgs[argc+1000];
          execArgs[0] = strdup("bash");
          execArgs[1] = strdup(argv[1]);

          int loopTimes = rand() % 10 + 1;
          char buffer[100];
          int randVal;

          for(int i = 0; i < loopTimes ; i++){
          
               randVal = rand() % 10 + 1;
               snprintf(buffer,100,"%d", randVal);
               execArgs[i+2] = strdup(buffer);
          
          }    

          fflush(stdout);
          printf("In child %d: ", getpid());
          
          fflush(stdout); // why twice I do not know, DON'T TOUCH IT
          execvp("bash", execArgs);

          exit(0);
     }

     wait(NULL);
     return 0;
}