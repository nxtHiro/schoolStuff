/*
2 int arrays [10, 99]
10 elements each
use loop to print out each scores and sum

make array random
*/

import java.util.*;
class scores
{
  public static void main(String[] args)
  {
    int[] test1 = new int[10];
    int[] test2 = new int[10];

    for(int i=0;i<test1.length;i++)
    {
      test1[i] = (int)(Math.random()*((99-10)+1))+10;
      System.out.print(test1[i] + " ");
    }
    System.out.println();

    for(int i=0;i<test2.length;i++)
    {
      test2[i] = (int)(Math.random()*((99-10)+1))+10;
      System.out.print(test2[i] + " ");
    }
    System.out.println();

    for (int i = 0; i < 10; i++)
    {
        System.out.println("Student " + i + "'s scores are: " + test1[i] + " and " + test2[i] + ". The sum of the scores are " + (test1[i] + test2[i]) + ".");
    }
  }
}
