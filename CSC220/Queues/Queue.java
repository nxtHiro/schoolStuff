/* ***************************************************
 * Marco Flores
 * 25th October, 2018.
 * Queue.java
 *
 * A Queue data structure, with a linked list as the back end.
 *************************************************** */

public class Queue<Type>
{
  // List to hold data for the Queue of type Type
     private List<Type> list = null;

  // Standard constructor
     public <Type>Queue()
     {
          list = new List();
     }

  // Copy constructor
     public <Type>Queue(Queue q)
     {
          list = new List(q.list);
     }

  // Enqueues data to end of Queue
     public void Enqueue(Type data)
     {
          list.InsertAfter(data);
     }

  // Dequeues data from front of Stack and returns it
     public Type Dequeue()
     {
          list.First();
          Type retVal = list.GetValue();
          list.Remove();
          list.Last();
          return retVal;
     }

  // Returns the data at the front of Queue
     public Type Peek()
     {
          list.First();
          Type retVal = list.GetValue();
          list.Last();
          return retVal;
     }

  // Returns the size of the Queue
     public int Size()
     {
          return list.GetSize();
     }

  // Returns whether or not the Queue is empty
     public boolean IsEmpty()
     {
          return list.IsEmpty();
     }

  // Returns whether or not the Queue is full
     public boolean IsFull()
     {
          return list.IsFull();
     }

  // Returns whether or not a Queue is equal to another
     public boolean Equals(Queue q)
     {
          return this.list.Equals(q.list);
     }

  // Concatenates one Queue to another then returns the Queue
     public Queue<Type> Add(Queue q)
     {
          List<Type> l = this.list.Add(q.list);
          Queue<Type> retQueue = new Queue<Type>();
          for (int i = 0; i < l.GetSize(); i++)
          {
               l.SetPos(i);
               retQueue.Enqueue(l.GetValue());
          }
          return retQueue;
     }

  // toString function for printing
     public String toString()
     {
          return this.list.toString();
     }

}
