import java.util.*;

class Echo
{
  public static void main(String[] args)
  {
    Scanner s = new Scanner(System.in);
    ArrayList<Integer> grades = new ArrayList<Integer>();
    int[] gradesList = new int[grades.size()];
    while(s.hasNextInt())
    {
    grades.add(s.nextInt());
    }
    gradesList = grades.toArray(gradesList);

    System.out.println("Finished entering grades");

    for (int i = 0; i < gradesList.length; i++)
    {
      System.out.print(gradesList[i] + ",\t");
    }
  }
}
