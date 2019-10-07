
Skip to content

    All gists
    GitHub

    New gist
    @floresm2199

0

    0

@BillPepsiOfPepsiCo BillPepsiOfPepsiCo/List.java
Last active 4 days ago •
Code
Revisions 3
Sick thick list
List.java
package ug.list;
/* ***************************************************
 * <your name>
 * <the date>
 *
 * List Class - handles any form of data
 *************************************************** */

import java.util.function.Consumer;

public class List<Type> {
	// We don't actually have to set a max size with linked lists
	// But it is a good idea.
	// Just picture an infinite loop adding to the list! :O
	public static final int MAX_SIZE = 50;

	private Node<Type> head;
	private Node<Type> tail;
	private Node<Type> currentNode;
	private int size;
	private int position;

	// constructor
	// remember that an empty list has a "size" of -1 and its "position" is at -1
	public List() {
		this.head = null;
		this.tail = null;
		this.currentNode = null;
		this.position = -1;
	}

	// copy constructor
	// clones the list l and sets the last element as the current
	public List(List<Type> l) {
		Node<Type> n = l.head;

		this.head = this.tail = this.currentNode = null;
		this.size = 0;
		this.position = 0;

		while (n != null) {
			this.InsertAfter(n.getData());
			n = n.getLink();
		}
	}

	// navigates to the beginning of the list
	public void First() {
		//System.out.println("Reset position to head");
		this.currentNode = head;
		this.position = 0;
	}

	// navigates to the end of the list
	// the end of the list is at the last valid item in the list
	public void Last() {
		this.position = size - 1;
		this.currentNode = this.tail;
	}

	// navigates to the specified element (0-index)
	// this should not be possible for an empty list
	// this should not be possible for invalid positions
	public void SetPos(int pos) {
		if (size == 0) {
			this.position = -1;
		} else if (pos >= 0 && pos < size) {
			int i = 0;
			Node<Type> opNode = this.head;

			while (i++ < pos && opNode != null) {
				opNode = opNode.getLink();
			}

			this.currentNode = opNode;
			this.position = i;
		} else {
			SetPos(size - 1);
		}

	}

	private void posPlusPlus() {
		this.SetPos(this.position + 1);
	}

	private void posMinusMinus() {
		this.SetPos(this.position - 1);
	}

	// navigates to the previous element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Prev() {
		if (currentNode == null) {
			First();
		}
		if (this.position == 0) return;

		Node<Type> n = this.currentNode;
		First();

		while (this.currentNode != null) {
			if (this.currentNode.getLink() == n) {
				break;
			}
			Next();
		}
	}


	// navigates to the next element
	// this should not be possible for an empty list
	// there should be no wrap-around
	public void Next() {
		if (this.currentNode != null) {
			if (this.currentNode.getLink() != null) {
				this.currentNode = this.currentNode.getLink();
				position++;
			} else {
				//System.out.println(String.format("Node %s containing %s was next'd, but its link is null (currentNode will become null)", this.currentNode, this.currentNode.getData()));
				this.currentNode = null;
			}
		} else {
			//System.out.println("Current node is null, can't be next\'d");
		}
	}

	// returns the location of the current element (or -1)
	public int GetPos() {
		return this.position;
	}

	// returns the value of the current element (or -1)
	public Type GetValue() {
		if (this.currentNode == null) {
			return null;
		} else {
			return this.currentNode.getData();
		}
	}

	// returns the size of the list
	// size does not imply capacity
	public int GetSize() {
		return this.size;
	}

	// inserts an item before the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertBefore(Type data) {

		if (this.size < MAX_SIZE) {
			Node<Type> n = new Node<>();
			n.setData(data);

			if (head == null) {
				//System.out.println(String.format("Node added as head: %s containing %s", n, n.getData()));
				head = n;
				First();
			} else if (tail == null) {
				////System.out.println(String.format("Node added as tail: %s containing %s", n, n.getData()));
				Node<Type> oldHead = this.head;
				oldHead.setLink(null);
				this.tail = oldHead;
				n.setLink(this.tail);
				this.head = n;
				this.currentNode = head;
			} else if (this.currentNode == head) {
				////System.out.println(String.format("Node appended to beginning of list: %s containing %s", n, n.getData()));
				n.setLink(head);
				this.head = n;
				First();
			} else {
				////System.out.println(String.format("Node inserted into middle of list: %s containing %s", n, n.getData()));
				/*Node<Type> currNode = this.currentNode;
				n.setLink(currNode);
				Prev();
				this.currentNode.setLink(n);
				this.currentNode = n;
				position++;*/

				Prev();
				this.InsertAfter(data);
				position++;
			}

			size++;
		}
	}

	// inserts an item after the current element
	// the new element becomes the current
	// this should not be possible for a full list
	public void InsertAfter(Type data) {
		if (this.size < MAX_SIZE) {
			Node<Type> n = new Node<>();
			n.setData(data);

			if (this.head == null) {
				////System.out.println(String.format("Node added as head: %s containing %s", n, n.getData()));
				this.head = n;
				First();
			} else if (this.tail == null) {
				////System.out.println(String.format("Node added as tail: %s containing %s", n, n.getData()));
				this.tail = n;
				this.head.setLink(tail);
				Last();
			} else if (this.currentNode == this.tail) {
				////System.out.println(String.format("Node appended to end of list: %s containing %s", n, n.getData()));
				this.tail.setLink(n);
				n.setLink(null);
				this.tail = n;
				this.currentNode = tail;
				Last();
			} else {
				////System.out.println(String.format("Node inserted into middle of list: %s containing %s", n, n.getData()));

				Node<Type> currNode = this.currentNode;
				Next();
				Node<Type> nextNode = this.currentNode;

				currNode.setLink(n);
				n.setLink(nextNode);
				this.currentNode = n;
				position++;
			}

			this.size++;
		}
	}

	// removes the current element
	// this should not be possible for an empty list
	public void Remove() {
		if (this.size == 0) return;

		if (this.currentNode == null) {
			System.out.println("Remove called on null node (you probably Next\'d on the tail, call prev() to go back)");
			return;
		}

		//System.out.println(String.format("Remove called on node %s containing %s", this.currentNode, this.currentNode.getData()));

		if (this.currentNode == head) {
			//Next();
			Node<Type> nextNode = this.currentNode.getLink();
			if (nextNode != null && nextNode == this.tail) {
				this.head = this.tail;
				this.tail = null;
				this.head.setLink(null);
				this.size--;
				First();
			} else if (nextNode == null) {
				this.head = null;
				this.size--;
				this.position = -1;
			} else {
				this.head = this.head.getLink();
				this.size--;
				First();
			}
		} else if (this.currentNode == this.tail) {
			Prev();
			if (this.currentNode != null && this.currentNode == head) {
				this.tail = null;
				this.head.setLink(null);
				this.size--;
				First();
			} else {
				this.tail = this.currentNode;
				this.tail.setLink(null);
				this.size--;
				Last();
			}
		} else {
			final Node<Type> nodeBeforeCurrentNode, nodeAfterCurrentNode;
			Prev();
			nodeBeforeCurrentNode = this.currentNode;
			Next();
			Next();
			nodeAfterCurrentNode = this.currentNode;

			nodeBeforeCurrentNode.setLink(nodeAfterCurrentNode);
			this.currentNode = nodeAfterCurrentNode;
			this.size--;
		}

		if (this.size == 0) this.position = -1;
	}

	// replaces the value of the current element with the specified value
	// this should not be possible for an empty list
	public void Replace(Type data) {
		assert this.currentNode != null;
		this.currentNode.setData(data);
	}

	// returns if the list is empty
	public boolean IsEmpty() {
		return this.size == 0;
	}

	// returns if the list is full
	public boolean IsFull() {
		return this.size == MAX_SIZE;
	}

	// returns if two lists are equal (by value)
	public boolean Equals(List<Type> l) {
		if (this.size != l.size) return false;

		Node<Type> opNode = this.head, opNode2 = l.head;

		while (opNode != null) {
			if (opNode.getData() != opNode2.getData()) {
				return false;
			}

			opNode = opNode.getLink();
			opNode2 = opNode2.getLink();
		}

		return true;
	}

	// returns the concatenation of two lists
	// l should not be modified
	// l should be concatenated to the end of *this
	// the returned list should not exceed MAX_SIZE elements
	// the last element of the new list is the current
	public List<Type> Add(List<Type> l) {
		List<Type> concatList = new List<>(this);
		if (this.tail == null) return concatList;

		concatList.tail.setLink(l.head);
		concatList.tail = l.tail;
		concatList.size += l.size;
		concatList.Last();

		return concatList;
	}

	// returns a string representation of the entire list (e.g., 1 2 3 4 5)
	// the string "NULL" should be returned for an empty list
	public String toString() {
		if (this.size == 0) return "NULL";

		Node<Type> opNode = this.head;
		StringBuilder sb = new StringBuilder();

		while (opNode != null) {
			sb.append(opNode.getData().toString());
			sb.append(" ");
			opNode = opNode.getLink();
		}

		return sb.toString();
	}

	public void traverseList(Consumer<Node<Type>> consumer) {
		Node<Type> opNode = this.head;

		while (opNode != null) {
			consumer.accept(opNode);
			opNode = opNode.getLink();
		}
	}

	public int indexOf(Type data) {
		Node<Type> opNode = this.head;
		int i = 0;

		while (opNode != null) {
			if (opNode.getData().equals(data)) {
				return i;
			}

			opNode = opNode.getLink();
			i++;
		}

		return -1;
	}

	public boolean hasNext() {
		if (this.currentNode == null) {
			return false;
		}

		return this.currentNode.getLink() != null;
	}
}
@floresm2199

Attach files by dragging & dropping,

, or pasting from the clipboard.
Styling with Markdown is supported

    © 2018 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

Press h to open a hovercard with more details.
