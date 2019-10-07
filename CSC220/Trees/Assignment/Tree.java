/* ***************************************************************************
 * <your name>
 * <the date>
 * <the file name>
 *
 * <a simple, short program/class description>
 * **************************************************************************/

import java.util.*;

class Tree
{
     private Node root;
     private int size;
     public static final int MAX_SIZE = 30;

     // Constructor. An empty tree has a size of 0.
     public Tree()
     {
             root = null;
             size = 0;
     }

     // Copy constructor. Clones Tree t (i.e. its nodes, and its size)
     public Tree(Tree t)
     {
          this.root = mycopy(t.root);
          this.size = t.Size();
     }

     // Private copy function that recursively copies Node a (along with
     // all its links, and returns that copy.
     private Node mycopy(Node a)
     {
          if (a == null)
               return null;
          Node newNode = new Node(a.getData());
          newNode.setLeft(mycopy(a.getLeft()));
          newNode.setRight(mycopy(a.getRight()));
          return newNode;
     }

     // function that takes the key and calls the deleteKey function.
     // Should only work if the tree is not empty.
     public void Delete(int key)
     {
          if (!IsEmpty())
               DeleteKey(this.root, key);
     }

     // private recursive function that takes a node, and the key to delete from
     // the subtrees attached to that node. It returns a copy of the tree
     // with the required node having been removed from the appropriate subtrees.
     private Node DeleteKey(Node a, int key)
     {
          if (a == null)
               return a;
          if (key < a.getData())
               a.setLeft(DeleteKey(a.getLeft(), key));
          else if (key > a.getData())
               a.setRight(DeleteKey(a.getRight(), key));
          else
          {
               if (a.getLeft() == null && a.getRight() == null)
               {
                    size--;
                    return null;
               }
               else if (a.getLeft() == null)
               {
                    size--;
                    return a.getRight();
               }
               else if (a.getRight() == null)
               {
                    size--;
                    return a.getLeft();
               }
               else
               {
                    int minVal = Successor(a.getRight()).getData();
                    a.setData(minVal);
                    a.setRight(DeleteKey(a.getRight(), minVal));
               }
          }
          return a;
     }

     // Private function to find the successor to a node. The successor
     // of a node in a binary tree is the node immediately larger than
     // the required node.
     private Node Successor(Node a)
     {
          if (a.getLeft() != null)
               return Successor(a.getLeft());
          return a;
     }



     // Function to insert data into the tree in its appropriate location
     // by using the Add() recursive function. This should not be
     // possible for a tree that is already full. If the tree is empty,
     // then it does the insertion itself.
     public void Insert(int data)
     {
          if (!IsFull())
          {
               if (IsEmpty())
                    root = new Node(data);
               else
                    this.root = Add(data, root);
               size++;
          }
     }

     // Private recursive function that takes a Node attached to its own
     // subtrees, and attaches the data to the tree in the proper location.
     private Node Add(int data, Node a)
     {
          if (!IsFull())
          {
               if (a == null)
               {
                    a =  new Node(data);
                   return a;
               }

               if (data < a.getData())
               {
                   a.setLeft(Add(data, a.getLeft()));
               }
               else if (data > a.getData())
               {
                   a.setRight(Add(data, a.getRight()));
               }
               else
               {
                   return a;
               }
          }
          return a;
      }

     // function to return the size of the tree (i.e. the number of nodes
     // in the tree).
     public int Size()
     {
             return this.size;
     }

     // Function to tell whether the tree is empty or not.
     public boolean IsEmpty()
     {
             if (this.size == 0)
                     return true;
             return false;
     }

     // Function to tell whether the tree is full or not.
     public boolean IsFull()
     {
             if (this.size < MAX_SIZE)
                     return false;
             return true;
     }

     // Function to return the InOrder traversal of the tree. It takes a
     // string as its argument, updates the string with the node
     // information, and then returns the updated string that should
     // contain the inorder traversal of the tree.getData
     private String InOrder(Node a, String s)
     {
          String temp = s;
          if (a != null)
          {
               temp = InOrder(a.getLeft(), temp);
               temp += a.getData() + " ";
               temp = InOrder(a.getRight(), temp);
          }
         return temp;
     }

     // Function to return the PreOrder traversal of the tree. It takes a
     // string as its argument, updates the string with the node
     // information, and then returns the updated string that should
     // contain the preorder traversal of the tree.
     private String PreOrder(Node a, String s)
     {
          String temp = s;
          if (a != null)
          {
               temp += a.getData() + " ";
               temp = InOrder(a.getLeft(), temp);
               temp = InOrder(a.getRight(), temp);
          }
         return temp;
     }

     // Function to return the PostOrder traversal of the tree. It takes a
     // string as its argument, updates the string with the node
     // information, and then returns the updated string that should
     // contain the postorder traversal of the tree.
     private String PostOrder(Node a, String s)
     {
          String temp = s;
          if (a != null)
          {
               temp = InOrder(a.getLeft(), temp);
               temp = InOrder(a.getRight(), temp);
               temp += a.getData() + " ";
          }
         return temp;
     }

     // A function that returns the maximum value in the tree. That value
     // is -1 for an empty tree.
     public int getMax()
     {
          Node temp = this.root;
          if (temp == null)
               return -1;
          while (temp.getRight() != null)
          {
             temp = temp.getRight();
          }
          return temp.getData();
     }

     // A function that returns the minimum value in the tree. That value
     // is -1 for an empty tree.
     public int getMin()
     {
          Node temp = this.root;
          if (temp == null)
               return -1;
          while (temp.getLeft() != null)
          {
             temp = temp.getLeft();
          }
          return temp.getData();
     }

     // A toString function that returns "NULL" if the tree is empty.
     // Otherwise, it returns the InOrder traversal of the tree.
     public String toString()
     {
          String s = "";
          if (IsEmpty())
               return "NULL";
          else
          {
               s = InOrder(this.root, s);
          }
          return s;
     }

     // A Print function that prints out the InOrder, PreOrder, and
     // PostOrder traversals of the tree (each one preceeded by the word
     // identifying what kind of traversal it is). It also calls the
     // private Print() function which prints out the tree sideways.
     public void Print()
     {
          String s = "";
          System.out.println("InOrder: " + InOrder(this.root, s));
          System.out.println("PreOrder: " + PreOrder(this.root, s));
          System.out.println("PostOrder: " + PostOrder(this.root, s));

          Print(root, 0);

     }

     // A Print function that takes a node and an int to recursively print
     // out the tree sideways. The int "lev" determines how far away from
     // the root that particular node will be printed. (Refer to notes for
     // details of this function).
     private void Print(Node n, int lev)
     {
          if (n != null)
          {
               Print(n.getRight(), lev + 1);

               for (int i = 0; i < lev; i++)
                    System.out.print("\t");
               System.out.println(n);

               Print(n.getLeft(), lev + 1);
          }
     }


     // A function that returns if two trees are equal by value.
     public boolean Equals(Tree t)
     {
             String curr = new String();
             String that = new String();

             if (this.Size() != t.Size())
                    return false;
             if (!(this.InOrder(this.root, curr).equals(InOrder(t.root, that))))
                    return false;
             if (!(this.PreOrder(this.root, curr).equals(PreOrder(t.root, that))))
                    return false;
             if (!(this.PostOrder(this.root, curr).equals(PostOrder(t.root, that))))
                    return false;
             return true;

     }
}
