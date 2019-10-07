class Ackermann
{
     public static void main(String[] args)
     {
          for (int i = 0; i < 5; i++)
          {
               for (int j = 0; j < 5; j++)
               {
               System.out.println("i: " + i + " j: " + j + " : " + acker(i, j));
               }
          }
     }
     public static int acker(int m, int n)
     {
     if (m == 0)
          return n + 1;
     if (m > 0 && n == 0)
          return acker(m - 1, 1);
     return acker(m - 1, acker(m, n - 1));
     }
}
