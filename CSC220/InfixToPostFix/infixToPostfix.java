import java.util.*;

class infixToPostfix
{
     // handles printing and calling operations
     public static void main(String[] args)
     {
          Scanner s = new Scanner(System.in);

          ArrayList<String> expr = new ArrayList<String>();

          while (s.hasNext())
          {
               expr.add(s.next());
          }
          String postfixExpression = new String();
          Double eval = 0.0;
          for(int i = 0; i < expr.size(); i++)
          {
               System.out.println(expr.get(i));
               postfixExpression = inFToPoF(expr.get(i));
               System.out.println(postfixExpression);
               eval = evalPostfix(postfixExpression);
               System.out.println(eval + "\n");

          }
     }

     // determines operator priority
     public static int priority(char c)
     {
          if (c == '+' || c == '-')
               return 1;
          else if (c == '*' || c == '/')
               return 2;
          else if (c == '^')
               return 3;
          else
               return -1;
     }

     // converts Infix to Postfix
     public static String inFToPoF(String expression)
     {
          Queue<Character> result = new Queue<>();

          Stack<Character> opStack = new Stack<>();
          char tmp = ' ';
          for (int i = 0; i < expression.length(); ++i)
          {
               char c = expression.charAt(i);
               if(Character.isDigit(c))
               {
                    result.Enqueue(c);
               }
               else if(c == '(')
               {
                    opStack.Push(c);
               }
               else if (c == ')')
               {
                   while (!opStack.IsEmpty() && opStack.Peek() != '(')
                       result.Enqueue(opStack.Pop());

                   opStack.Pop();
               }
               // an operator is encountered
               else
               {
                   while (!opStack.IsEmpty() && priority(c) <= priority(opStack.Peek()))
                   {
                       result.Enqueue(opStack.Pop());
                   }
                   opStack.Push(c);
               }
               System.out.println(result);
          }

          while (!opStack.IsEmpty())
              result.Enqueue(opStack.Pop());

          return result.toString();

     }

     // evaluates the Postfix expression using a Stack
     public static double evalPostfix(String expression)
     {
          double a = 0.0;
          double b = 0.0;
          double solution = 0.0;
          Stack<Double> evalStack = new Stack<>();

          for (int i = 0; i < expression.length(); ++i)
          {
               char c = expression.charAt(i);


               if(c == '+')
               {
                    a = evalStack.Pop();
                    b = evalStack.Pop();
                    evalStack.Push(a + b);
               }
               else if(c == '-')
               {
                    a = evalStack.Pop();
                    b = evalStack.Pop();
                    evalStack.Push(b - a);
               }
               else if(c == '*')
               {
                    a = evalStack.Pop();
                    b = evalStack.Pop();
                    evalStack.Push(a * b);
               }
               else if(c == '/')
               {
                    a = evalStack.Pop();
                    b = evalStack.Pop();
                    evalStack.Push(b / a);
               }
               else if(c == '^')
               {
                    a = evalStack.Pop();
                    b = evalStack.Pop();
                    evalStack.Push(Math.pow(b, a));
               }
               else
               {
                    evalStack.Push((double)Character.digit(c, 10));
               }
               //System.out.println(evalStack + "\n");
          }
          solution = evalStack.Pop();
          return solution;
     }

}
