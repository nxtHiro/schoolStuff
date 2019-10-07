class Recursion
{
     static String F(int n)
     {
          if (n/10 != 0)
               return n%10 + "" + F(n/10);
          else
               return Integer.toString(n%10);

     }
     public static void main(String[] args)
     {
          System.out.println(F(10));
     }
}
