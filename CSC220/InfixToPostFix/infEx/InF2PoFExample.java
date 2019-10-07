import java.util.*;
import java.io.*;

/**
 * An arithmetic expression in postfix form.
 *
 * @author Jim Glenn
 * @version 0.2 2012-04-27 updated for Java 7 and consolidated some cases
 * @version 0.1 11/22/2004
 */

class Postfix
{
    /**
     * The string representing this postfix expression.
     */
    private String exp;

    /**
     * Creates a postfix expression from the given prefix expression.
     * This version does not handle errors and does not allow
     * integer literals.
     *
     * @param infix a legal infix expression
     */

    public Postfix(String infix)
    {
        // postfix output starts out empty
        exp = "";

        // create stack of pending operators
        Stack<String> pendingOps = new Stack<String>();

        // set up scanner to break up input expression
        Scanner scan = new Scanner(infix);

        while (scan.hasNext())
            {
                String token = scan.next();

                if (!isOperator(token))
                    {
                        // literals and variables go straight to output
                        exp = exp + token + " ";
                    }
                else if (token.equals("("))
                    {
                        // opening parentheses are always pushed
                        pendingOps.push(token);
                    }
                else if (token.equals(")"))
                    {
                        // pop off stack until get to matching open paren
                        while (!pendingOps.peek().equals("("))
                            {
                                exp = exp + pendingOps.pop() + " ";
                            }

                        // pop off opening parenthesis
                        pendingOps.pop();
                    }
                else
                    {
                        // pop >= precedence operators off stack
                        // and add to output (note that we consider open paren
                        // to have low precedence here so it is not popped
                        // until the matching close paren is found)
                        // (also note that precedes handles the differences
                        // between left- and right-associative operators
                        // [left pop >= precedence; right pop only > prec])

                        while (pendingOps.size() > 0
                               && precedes(pendingOps.peek(), token))
                            {
                                if (!pendingOps.peek().equals("("))
                                    {
                                        exp = exp + pendingOps.pop() + " ";
                                    }
                                else
                                    {
                                        // opening parenthesis is discarded
                                        pendingOps.pop();
                                    }
                            }

                        // push operator on stack (except if its a close paren)
                        if (!token.equals(")"))
                            {
                                pendingOps.push(token);
                            }
                    }

            }

        // pop any remaining operators off the stack and add them to the output
        // (at this point if there is an open paren left on the stack that
        // means the infix formula was invalid)
        while (pendingOps.size() > 0)
            {
                exp = exp + pendingOps.pop() + " ";
            }
    }

    /**
     * Precedence levels for arithmetic operators and parentheses.
     * Levels are spaced out to make it easier to add operators with
     * in between precedences.
     */
    private static final int ADDITIVE = 0;
    private static final int MULTIPLICATIVE = 10;
    private static final int PARENTHESES = -10;
    private static final int EXPONENTIATION = 20;

    /**
     * Constants for associativity.  Left associate operators group
     * left-to-right -- - is left-associative, so 3-2-1 is equivalent
     * to (3-2)-1 and not 3-(2-1); ^ (exponentiation) is
     * right-associative, so 2^3^2 is 512, not 64.
     */
    private static final int RIGHT_ASSOCIATIVE = 0;
    private static final int LEFT_ASSOCIATIVE = 1;

    /**
     * Returns the precedence of the given operator.
     *
     * @param op an operator or parenthesis
     * @return the precedence of the given operator.
     */
    private static int getAssociativity(String op)
    {
        switch (op)
            {
            case "^":
                return RIGHT_ASSOCIATIVE;

            case "+":
            case "-":
            case "*":
            case "/":
                return LEFT_ASSOCIATIVE;

            default:
                throw new IllegalArgumentException();
            }
    }

    /**
     * Returns whether the left operator should precede the right
     * operator.  The left should precede the right if it has
     * higher precedence or equals precedence and the operators are
     * left-associative.
     *
     * @param left a string giving the left operator
     * @param right a string giving the right operator
     */
    private static boolean precedes(String left, String right)
    {
        return (getPrecedence(left) > getPrecedence(right)
                || (getPrecedence(left) == getPrecedence(right)
                    && getAssociativity(left) == LEFT_ASSOCIATIVE));
    }

    /**
     * Returns the precedence of the given operator.
     *
     * @param op an operator or parenthesis
     * @return the precedence of the given operator.
     */
    private static int getPrecedence(String op)
    {
        switch (op)
            {
            case "+":
            case "-":
                return ADDITIVE;

            case "*":
            case "/":
                return MULTIPLICATIVE;

            case "^":
                return EXPONENTIATION;

            case "(":
            case ")":
                return PARENTHESES;

            default:
                throw new IllegalArgumentException();
            }
    }

    /**
     * Determines if the given string is an identifier.
     *
     * @param id a string
     * @return true iff the given string is an identifier
     */

    private static boolean isIdentifier(String id)
    {
        return Character.isJavaIdentifierStart(id.charAt(0));
    }

    /**
     * Determines if the given string is an integer literal.
     *
     * @param num a string
     * @return true iff that string is an integer literal
     */

    private static boolean isLiteral(String num)
    {
        return (num.charAt(0) >= '0' && num.charAt(0) <= '9');
    }

    /**
     * Determines if the given string is an operator.
     *
     * @param op a string
     * @return true iff that string is an operator
     */
    public static boolean isOperator(String op)
    {
        return (op.length() == 1 && "()*-/+^".indexOf(op.charAt(0)) != -1);
    }

    /**
     * Returns a string representation of this expression.
     *
     * @return a string representation of this expression.
     */
    public String toString()
    {
        return exp;
    }

    public static void main(String[] args)
    {
        
         System.out.println(new Postfix("1 + 2 * 6"));
         System.out.println(new Postfix("( 1 + 2 ) * 6"));
         System.out.println(new Postfix("1 * 2 + 6"));
         System.out.println(new Postfix("1 + 2 * 6 / 3 + 1"));
         System.out.println(new Postfix("20 - 3 * 6 + 4"));
         System.out.println(new Postfix("2 ^ 3 ^ 2"));
         System.out.println(new Postfix("( 2 ^ 3 ) ^ 2"));
         System.out.println(new Postfix("6 * 2 ^ 3 ^ 2"));
         System.out.println(new Postfix("1 + ( 6 + 2 ) * 2"));


        if (args.length != 1)
            {
                System.err.println("USAGE: java Postfix infix-expression");
                System.exit(1);
            }

        System.out.println(new Postfix(args[0]));
    }
}
