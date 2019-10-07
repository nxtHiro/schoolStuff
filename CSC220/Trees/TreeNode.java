class TreeNode
{
     private int data;
     private TreeNode left;
     private TreeNode right;

     public TreeNode()
     {
     this.data = 0;
     this.left = null;
     this.right = null;
     }


     public int getData()
     {
     return this.data;
     }


     public TreeNode getLeft()
     {
     return this.left;
     }

     public TreeNode getRight()
     {
     return this.right;
     }

     public TreeNode setLeft(TreeNode left)
     {
     this.left = left;
     }

     public TreeNode setRight(TreeNode right`)
     {
     this.right = right;
     }

     public String toString()
     {
          return "" + this.data;
     }
}
