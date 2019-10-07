class TreeTest
{
     public static void main(String[] args)
     {
          TreeNode root = new TreeNode();
          root.setData(60);

          TreeNode temp = new TreeNode();
          temp.setData(67);

          TreeNode temp2 = new TreeNode();
          root.setData(58);

          root.setLeft(temp);
          root.setRight(temp2);
     }
}
