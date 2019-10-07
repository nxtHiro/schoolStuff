class Fact{
     public static void main(String[] args){
          long n = 1000;
          System.out.println(n + "! = " + myfact(n));
     }
     public static long myfact(long n){
          if (n == 1)
               return 1;
          else
               return n *myfact(n-1);
     }
}
