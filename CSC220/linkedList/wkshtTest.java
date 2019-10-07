class main
{
     public static void main(String[] args)
     {
          Node head = new Node();
          head.setData(5);
          System.out.println(head);

          Node tail = new Node();
          head.setLink(new Node());
          head.getLink().setData(10);
          tail = head.getLink();

          for (int i = 15; i <= 40;i += 5)
          {
               tail.setLink(new Node());
               tail.getLink().setData(i);
               tail = tail.getLink();
               System.out.println(tail);
          }
System.out.println("fdsojkhgsljhdf");
          Node twelve = new Node();
          twelve.setData(12);
          Node prev = new Node();
          Node current = head;
          while (current != null && current.getData() < twelve.getData())
          {
               prev = current;
               current = current.getLink();
          }
          twelve.setLink(prev.getLink());
          prev.setLink(twelve);

          Node delNodeOG = new Node();
          delNodeOG.setLink(head);
          Node delNode = delNodeOG;
          while (delNode.getLink() != null)
          {
               if (delNode.getLink().getData() == 5)
               {
                    Node next = delNode.getLink();
                    delNode.setLink(next.getLink());
               }
               else
               {
                    delNode = delNode.getLink();
               }
          }
          head = delNodeOG.getLink();

          System.out.println("fdsojkhgsljhdf");

          Node trav = head;
          while(trav != null)
          {
               System.out.println(trav);
               trav = trav.getLink();
          }


          Node sqTerms = head;
          while (sqTerms != null)
          {
               sqTerms.setData((int)Math.pow(sqTerms.getData(), 2));
               sqTerms = sqTerms.getLink();
          }

          System.out.println("fdsojkhgsljhdf");

          trav = head;
          while(trav != null)
          {
               System.out.println(trav);
               trav = trav.getLink();
          }
          head.setLink(null);
     }
}
