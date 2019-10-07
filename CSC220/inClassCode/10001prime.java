import java.util.*;
class prime
{
  public static void main(String[] args)
  {
    ArrayList<Integer> primes = new ArrayList<Integer>();
    int num = 1;
    boolean isPrime = true;
    int temp;
    while(primes.size() <= 10001){
      isPrime = true;
      for(int i=2;i<=num/2;i++)
      {
        temp=num%i;
      	if(temp==0)
      	{
      	  isPrime=false;
        }
      }
      if (isPrime)
      {
        primes.add(num);
      }
      num++;

    }
    System.out.println(primes.get(primes.size()-1));
  }
}
