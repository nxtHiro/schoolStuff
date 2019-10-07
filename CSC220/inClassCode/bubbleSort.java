import java.util.*;
class Sorts
{
     public static void main(String[] args)
     {
          int[] arr = new int[25];
          fillArray(arr);

          printArray(arr);
     }


     public static void bubbleSort(int[] arr)
     {
          int temp = 0;
          for(int i = 0; i < arr.length-1; i++)
          {
               for(int j = 1; j < arr.length - i + 1; i++){
                    if(arr[j] < arr[j-1])
                    {
                         temp = arr[j];
                         arr[i+1] = arr[i];
                         arr[i] = temp;
                    }
               }
          }
     }

     public static void fillArray(int[] arr)
     {
          Random rand = new Random();
          for(int i = 0; i < arr.length; i++)
               arr[i] = rand.nextInt();
     }

     public static void printArray(int[] arr)
     {
          for (int value : arr)
               System.out.print(value + ", ");
     }
}
