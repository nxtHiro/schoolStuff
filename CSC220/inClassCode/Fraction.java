class Fraction
{
  // fields stored privately
  private int num;
  private int den;

  // functions are public
  public Fraction()
  {
    num = 0;
    den = 1;
  }
  public int getNum()
  {
    return num;
  }

  public int getDen()
  {
    return den;
  }

  public void setNum(int n)
  {
    this.num = n;
  }

  public void setDen(int d)
  {
    this.den = d;
  }
  public double intoDec()
  {
    return (double)getNum()/getDen();
  }
  public String toString()
  {
  return "" + num + "/" + den + " and the decimal is " + intoDec();
}
}

class FractionTest
{
  public static void main(String[] args)
  {
  Fraction f = new Fraction();
  System.out.println(f);
  }
}
