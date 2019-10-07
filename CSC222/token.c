// String tokenizer
//   by Marco Flores
//     16 January 2019

#include <stdio.h>
#include <string.h>

int main(void){

     char userIn[256];
     int exitCalled = 1;
     char tokenDelim[2] = " ";
     char *token;
     int tokenCounter = 0;

     // runs program until exit condition is met
     while(exitCalled != 0){

          // input and formatting for input
          printf("$ ");
          fgets(userIn, 256, stdin);

          // checks for exit condition
          exitCalled = strcmp(userIn, "exit\n");
          if (exitCalled == 0)
               continue;

          // parses tokens and formatting
          printf("Line read: %s", userIn);
          printf("Token(s):");

          token = strtok(userIn, tokenDelim);
          while( token != NULL ) {
               printf( "\n %s", token );
               token = strtok(NULL, tokenDelim);
               tokenCounter++;
          }
          printf("%d token(s) read\n\n", tokenCounter);
          tokenCounter = 0;
     }

     return 0;
}
