// TechShell
//  by Marco Flores and Lewis Johnson


#include <stdio.h>
#include <unistd.h>
#include <limits.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>
#include <errno.h>

//for compatability dont actually need this and leads to buffer overflow
struct ShellCommand{
     char *args[256];
};

// declarations of functions used
int cd(char *dir);
void pwd();
char* commandPrompt();
struct ShellCommand parseCommandLine(char* input);
int executeCommand(struct ShellCommand command);
int contains(char** args, char* str);
void FileOut(struct ShellCommand args, int index);
void FileIn(struct ShellCommand args, int index);

int main(){

     char* input;
     struct ShellCommand command;

     // repeatedly prompt the user for input
     for (;;){

          // get user input
          input = commandPrompt();
          // parse the command line
          command = parseCommandLine(input);

          // execute the command
          executeCommand(command);
     }

     exit(0);
}

// change directory
int cd(char *dir){
	const char* tmp = dir;
     int chdirRet = chdir(tmp);
	if(chdirRet!=0){
		printf("Error %d (%s) \n",errno,strerror(errno));
	}
	return chdirRet;
}

// print working directory
void pwd(){
     char cwd[PATH_MAX];
     if(getcwd(cwd, sizeof(cwd)) != NULL){
	    printf("%s\n", cwd);
     }
}

// prompt user for input
char* commandPrompt(){
     char *input;
     input = malloc(256);
     printf("$ ");
	fgets(input, 256, stdin);
	if(strcmp((input+strlen(input)-1), "\n") == 0){
     	input[strlen(input) - 1] = '\0';
	}
     char *tmp;
     tmp = realloc(input, strlen(input));
     input = tmp;
     return input;

}

// parse user input
struct ShellCommand parseCommandLine(char* input){
	char tokenDelim[2] = " ";
     char *token;
     int tokenCounter = 0;
     struct ShellCommand command[256];
     token = strtok(input, " ");
     while( token != NULL ) {
          command -> args[tokenCounter] = token;
          token = strtok(NULL, " ");
          tokenCounter++;
     }

     command -> args[tokenCounter] = NULL;
     return *command;
}

// checks for a particular character then returns its position, if not present returns -1
int contains(char** args, char* str){
	char* arg = args[0];
	int pos = 0;

	while(arg != NULL){
		if(strcmp(arg, str) == 0)
			return pos;
		arg = args[++pos];
	}

	return -1;
}

//take in command
//parse command into sub commands and order subcommands to be executed
//run commands via a for loop and pipe the out put when needed
// return error status
int executeCommand(struct ShellCommand command){
	//variables
	int *status;
	int pid;

	struct ShellCommand commands[10];
	int index = 0;


	//variables dynamically assigned
     if(strcmp(command.args[0], "exit") == 0){
          exit(0);
     }
     else if(strcmp(command.args[0], "pwd") == 0){
          pwd();
          return 0;
     }
     else if(strcmp(command.args[0], "cd") == 0){
          cd(command.args[1]);
          return 0;
	}
	
	pid = fork(); 					//forks process
	status = malloc(sizeof(int));		//this makes waitpid happy
	//child process code
	if(pid == 0){
		
		int indexOfGreat = contains(command.args, ">");
		int indexOfLess = contains(command.args, "<");
		
		if(indexOfGreat != -1){
			command.args[indexOfGreat] = NULL;
			FileOut(command, indexOfGreat);
		}
		if(indexOfLess != -1){
			command.args[indexOfLess] = NULL;
			FileIn(command, indexOfLess);
		}
		execvp(command.args[0],command.args);
		int code = errno;
		exit(code);

	 //parent process code
	}
	else{
		//wait for child to complete and pass the error onto main
		waitpid(pid,status,0);
		int code = WEXITSTATUS(*status);
		if(code !=0){
			printf("Error %d (%s) \n",code,strerror(code));
		}

		return code;

	}
}

// generates output file
void FileOut(struct ShellCommand args, int index){
	
	int fp = open(args.args[index+1],O_WRONLY|O_CREAT|O_TRUNC,S_IRUSR|S_IRGRP|S_IWGRP|S_IWUSR);
	dup2(fp,1);
	if(dup2(fp,1)==-1){
		perror("the file failed (out)");
	}
	close(fp);
	args.args[index] = NULL;
}

// handles input file
void FileIn(struct ShellCommand args, int index){
	int fp = open(args.args[index+1],O_RDONLY);
	dup2(fp,0);
	if(dup2(fp,STDIN_FILENO) == -1){
		perror("the file failed (in)");
	}

	close(fp);
	args.args[index] = NULL;
}
