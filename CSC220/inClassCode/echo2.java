import java.util.*;

class Echo
{
  public static void main(String[] args)
  {
    Scanner s = new Scanner(System.in);
    ArrayList<Integer> grades = new ArrayList<Integer>();
    while(s.hasNextInt())
    {
    grades.add(s.nextInt());
    }
    System.out.println("Finished entering grades");

    for (int grade : grades)
    {
      System.out.print(grade + ",\t");
    }
  }
}
