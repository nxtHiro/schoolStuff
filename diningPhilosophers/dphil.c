/* Dining Philosophers problem
   By: Marco Flores and Lewis Johnson
   Compiler command: gcc -o dphil dphil.c -lpthread
*/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct{
     int numOfThreads;             // total number of threads
     int tid;					// id of the thread
     int timesEaten;               // times eaten
	int timesToEat;			// number of times to eat
} threadData;

int *chopstickStatus = 0;
pthread_mutex_t *mutex = 0;

void *doThings( void * data );

int main( int argc, char* argv[] ){


     if(argc != 3){
          printf("Usage: ./dphil 10 7\n");
          return -1;
     }
     if(atoi(argv[2]) < 2 || atoi(argv[1]) < 0){
          printf("Please set greater than one philosopher and at least zero meals.\n");
          return -1;
     }

     int threadNum = atoi(argv[2]);                             // number of threads to spawn
     
     int timesToEat = atoi(argv[1]);                            // number of times for each philosopher to eat
     
     chopstickStatus = malloc(sizeof(int) * threadNum);         // availability status of each chopstick
     for (int i = 0; i < threadNum; i++){
          chopstickStatus[i] = 1;
     }
     
     mutex = malloc(sizeof(pthread_mutex_t) * (threadNum));     // mutex locks for each chopstick

     pthread_t dphils[threadNum];                               // tids for the philosophers

     pthread_attr_t attr[threadNum];                            // attributes for the threads
     
     int numOfMeals[threadNum];                                 // number of meals eaten by each philosopher
     for (int i = 0; i < threadNum; i++){
          numOfMeals[i] = 0;
     }

     threadData tds[threadNum];                                 // array of threadData of size threadNum 
                                                                // to push data to threads

     // init an array of attributes for the threads
     for ( int i = 0; i < threadNum; i++ ){
	     pthread_attr_init(&(attr[i]));
	}

     // init an array of mutex locks "chopsticks"
     for ( int i = 0; i < threadNum; i++ ){
          pthread_mutex_init(&mutex[i], NULL);
     }

     // populating the thread data stuct for the threads' data
     for ( int i = 0; i < threadNum; i++ ){
          threadData td;
          td.numOfThreads = threadNum;
          td.tid = i;
          td.timesEaten = numOfMeals[i];
          td.timesToEat = timesToEat;
          tds[i] = td;                    // populates an array of type threadData to store all the data
     }

     // create threads
     for ( int i = 0; i < threadNum; i++ ){
          pthread_create(&(dphils[i]), &(attr[i]), doThings, &(tds[i]));
     }

     // joins threads
     for ( int i = 0; i < threadNum; i++ ){
          pthread_join(dphils[i], NULL);
     }

     return 0;     

}

void *doThings( void *sdata ){

     threadData *data = sdata; // typecast void* to threadData

     int rightIndex = data->tid;                            // index of the thread's right chopstick mutex
     int leftIndex = (data->tid + 1) % data->numOfThreads;  // index of the thread's left chopstick mutex
     
     // loops until the philosopher eats enough times
	while ( data->timesEaten < data->timesToEat ){
          
          // locks the right chopstick
          pthread_mutex_lock(&mutex[rightIndex]);

          // check if right chopstick is available
          if ( chopstickStatus[rightIndex] == 1 ){
               
               // set right chopstick availability to unavailable
               chopstickStatus[rightIndex] = 0;

               // unlock right chopstick
               pthread_mutex_unlock(&mutex[rightIndex]);

               // locks the left chopstick
               pthread_mutex_lock(&mutex[leftIndex]);

               // check if left chopstick is available
               if ( chopstickStatus[leftIndex == 1] ){

                    // set left chopstick availability to unavailable
                    chopstickStatus[leftIndex] = 0;

                    // unlock left chopstick
                    pthread_mutex_unlock( &mutex[leftIndex] );

                    // lock both chopsticks
                    pthread_mutex_lock(&mutex[rightIndex]);
                    pthread_mutex_lock(&mutex[leftIndex]);
                    // ************************ Critical Section ************************************** //
                    
                    data->timesEaten++;
                    printf("Philosopher %d is eating...\n", data->tid);

                    // ******************************************************************************** //
                    
                    // set chopsticks availability to available
                    chopstickStatus[rightIndex] = 1;
                    chopstickStatus[leftIndex] = 1;

                    // unlock both chopsticks
                    pthread_mutex_unlock(&mutex[rightIndex]);
                    pthread_mutex_unlock(&mutex[leftIndex]);
                    
                                  // sleep to reduce number of needless loops 
                    usleep(5000); // (i.e. bang head against door while its locked until its unlockd)
 

               }
               else{
                    // if left chopstick is unavailable think
                    printf("Philosopher %d is thinking...\n", data->tid);

                    // unlock the left chopstick
                    pthread_mutex_unlock(&mutex[leftIndex]);

                    // lock right chopstick
                    pthread_mutex_lock(&mutex[rightIndex]);

                    // set right chopstick to available
                    chopstickStatus[rightIndex] = 1;

                    // unlock right chopstick
                    pthread_mutex_unlock(&mutex[rightIndex]);

                                  // sleep to reduce number of needless loops 
                    usleep(5000); // (i.e. bang head against door while its locked until its unlockd)
               }
          }
          else{
               // if right chopstick is unavailable think
               printf("Philosopher %d is thinking...\n", data->tid);

               // unlock right chopstick
               pthread_mutex_unlock(&mutex[rightIndex]);
               
                               // sleep to reduce number of needless loops 
               usleep(5000); // (i.e. bang head against door while its locked until its unlockd)
          }
     }

     pthread_exit(0);
}