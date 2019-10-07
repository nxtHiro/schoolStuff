/* ***************************************************
 * Marco Flores
 * 12th October, 2018.
 * List.java
 *
 * A List data structure, with a linked list as the back end.
 *************************************************** */

// the Node class
class Node
{
	private int data;
	private Node link;

	// constructor
	public Node()
	{
		this.data = 0;
		this.link = null;
	}

	// accessor and mutator for the data component
	public int getData()
	{
		return this.data;
	}

	public void setData(int data)
	{
		this.data = data;
	}

	// accessor and mutator for the link component
	public Node getLink()
	{
		return this.link;
	}

	public void setLink(Node link)
	{
		this.link = link;
	}
}

// the List class
public class List
{
	public static final int MAX_SIZE = 50;

	private Node head;
	private Node tail;
	private Node curr;
	private int num_items;

	// constructor
	// remember that an empty list has a "size" of -1 and its "position" is at -1
	public List()
	{
	    head = tail = curr = null;
	    num_items = 0;
	}

	// copy constructor
	// clones the list l and sets the last element as the current
	public List(List l)
	{
	    head = tail = curr = null;
	    num_items = 0;

	    Node temp = l.head;
	    while (temp != null)
	    {
		InsertAfter(temp.getData());
		temp = temp.getLink();
	    }
	}

	// navigates to the beginning of the list
	public void First()
	{
	    curr = head;
	}

	// navigates to the end of the list
	// the end of the list is at the last valid item in the list
	public void Last()
	{
	    curr = tail;
	}

	// navigates to the specified element (0-index)
	// this should not be possible for an empty list
	// this should not be possible for invalid positions
	public void SetPos(int pos)
	{
	    if (!IsEmpty() && pos >= 0 && pos < num_items)
	    {
		curr = head;
		for (int i = 0; i < pos; i++)
		    curr = curr.getLink();
	    }
	}

	// navigates to the previous element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Prev()
	{
	    if (!IsEmpty() && curr != head)
	    {
		Node temp = head;
		while (temp.getLink() != curr)
		    temp = temp.getLink();

		this.curr = temp;
	    }
	}

	// navigates to the next element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Next()
	{
	    if (!IsEmpty() && curr != tail)
		curr = curr.getLink();
	}

	// returns the location of the current element (or -1)
	public int GetPos()
	{
	    if (IsEmpty())
		return -1;
	    else
	    {
		int pos = 0;
		Node temp = head;
		while (temp != curr)
		{
		    temp = temp.getLink();
		    pos++;
		}
		return pos;
	    }
	}

	// returns the value of the current element (or -1)
	public int GetValue()
	{
	    if (IsEmpty())
		return -1;
	    return curr.getData();
	}

	// returns the size of the list
	// size does not imply capacity
	public int GetSize()
	{
	    return num_items;
	}

	// inserts an item before the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertBefore(int data)
	{
	    if (!IsFull())
	    {
		if (IsEmpty())
		    InsertAfter(data);
		else if (curr == head)
		{
		    curr = new Node();
		    curr.setData(data);
		    curr.setLink(head);
		    head = curr;
		    num_items++;
		}
		else
		{
		    Prev();
		    InsertAfter(data);
		}
	    }
	}

	// inserts an item after the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertAfter(int data)
	{
	    if (!IsFull())
	    {
		if (IsEmpty())
		{
		    head = tail = curr = new Node();
		    head.setData(data);
		}
		else if (curr == tail)
		{
		    tail.setLink(new Node());
		    tail = tail.getLink();
		    tail.setData(data);
		    curr = tail;
		}
		else
		{
		    Node temp = new Node();
		    temp.setData(data);
		    temp.setLink(curr.getLink());
		    curr.setLink(temp);
		    curr = temp;
		}
		num_items++;
	    }
	}

	// removes the current element (collapsing the list)
	// this should not be possible for an empty list
	public void Remove()
	{
	    if (!IsEmpty())
	    {
		if (curr ==  head)
		{
		    head = curr = curr.getLink();
		}
		else if(curr == tail)
		{
		    Prev();
		    curr.setLink(null);
		    tail = curr;
		}
		else
		{
		    Prev();
		    curr.setLink(curr.getLink().getLink());
		    Next();
		}
		num_items--;

	    }
	}

	// replaces the value of the current element with the specified value
	// this should not be possible for an empty list
	public void Replace(int data)
	{
	    if (!IsEmpty())
		curr.setData(data);
	}

	// returns if the list is empty
	public boolean IsEmpty()
	{
	    return (head == null);
	}

	// returns if the list is full
	public boolean IsFull()
	{
	    return (num_items == MAX_SIZE);
	}

	// returns if two lists are equal (by value)
	public boolean Equals(List l)
	{
	    if (this.num_items != l.num_items)
		return false;

	    for (Node a = this.head, b = l.head; a != null || b != null; a = a.getLink(), b = b.getLink())
		if (a.getData() != b.getData())
		    return false;

	    return true;
	}

	// returns the concatenation of two lists
	// l should not be modified
	// l should be concatenated to the end of *this
	// the returned list should not exceed MAX_SIZE elements
	// the last element of the new list is the current
	public List Add(List l)
	{
	    List sum = new List(this);
	    Node temp = l.head;
	    while (temp != null)
	    {
		sum.InsertAfter(temp.getData());
		temp = temp.getLink();
	    }

	    return sum;
	}

	// returns a string representation of the entire list (e.g., 1 2 3 4 5)
	// the string "NULL" should be returned for an empty list
	public String toString()
	{
	    if (IsEmpty())
		return "NULL";
	    String s = "";
	    Node temp = head;
	    while (temp != null)
	    {
		s += (temp.getData() + " ");
		temp = temp.getLink();
	    }
	    return s;
	}
}
