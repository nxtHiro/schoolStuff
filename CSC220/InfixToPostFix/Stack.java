/* ***************************************************
 * Marco Flores
 * 25th October, 2018.
 * Stack.java
 *
 * A Stack data structure, with a linked list as the back end.
 *************************************************** */
 
public class Stack<Type>
{
  // List to hold data for the Stack of type Type
     private List<Type> list = null;

  // Standard constructor
     public <Type>Stack()
     {
          list = new List();
     }

  // Copy constructor
     public <Type>Stack(Stack s)
     {
          list = new List(s.list);
     }

  // Pushes data to top of Stack
     public void Push(Type data)
     {
          list.InsertBefore(data);
     }

  // Pops data from top of Stack and returns it
     public Type Pop()
     {
          list.First();
          Type retVal = list.GetValue();
          list.Remove();
          return retVal;
     }

  // Returns the data at the top of Stack
     public Type Peek()
     {
          list.First();
          return list.GetValue();
     }

  // Returns the size of the Stack
     public int Size()
     {
          return list.GetSize();
     }

  // Returns whether or not the Stack is empty
     public boolean IsEmpty()
     {
          return list.IsEmpty();
     }

  // Returns whether or not the Stack is full
     public boolean IsFull()
     {
          return list.IsFull();
     }

  // Returns whether or not a Stack is equal to another
     public boolean Equals(Stack s)
     {
          return this.list.Equals(s.list);
     }

  // Concatenates one Stack to another then returns the Stack
     public Stack<Type> Add(Stack s)
     {
          List<Type> l = this.list.Add(s.list);
          Stack<Type> retStack = new Stack<Type>();
          for (int i = l.GetSize() - 1; i >= 0; i--)
          {
               l.SetPos(i);
               retStack.Push(l.GetValue());
          }
          return retStack;
     }

  // toString function for printing
     public String toString()
     {
          return this.list.toString();
     }

}
