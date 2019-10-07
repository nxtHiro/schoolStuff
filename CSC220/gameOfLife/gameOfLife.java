import java.io.*;
class gameOfLife
{
	public static void main(String[] args)
	{
		int gen = (args.length == 0) ? 10 : Integer.parseInt(args[0]);
		int sleeptime = (args.length != 2) ? 1000 : Integer.parseInt(args[1]);
		boolean [][] mybrd = readFile();
		for(int i = 0; i< gen ; i++)
		{
			printBoard(i, mybrd);
			mySleep(sleeptime);
			mybrd = nextGen(mybrd);
		}
	}
	public static boolean [][] readFile()
	{
		boolean [][] board = null;
		int i = 0;
		try
		{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String line;

			while ((line = br.readLine()) != null)
			{
				if (i == 0)
					board = new boolean [line.length()][line.length()];
				fillBoard(board, i, line);
				i++;
       			}
       		 br.close();
    		}
    		catch(Exception e){}
   		return board;
	}
	public static boolean[][] nextGen(boolean[][] arr)
	{
		boolean[][] newbrd = new boolean [arr.length][arr.length];

		for(int i = 1; i < arr.length -1; i++)
		{
			for(int j = 1; j < arr[i].length - 1; j++)
			{
				int neighbours = countNeighbours(arr, i, j);
				if(arr[i][j])
					newbrd[i][j] = (neighbours == 2) || (neighbours  == 3);
				else
					newbrd[i][j] = (neighbours == 3);

			}
		}
		return newbrd;
	}
	
	public static int countNeighbours(boolean[][] brd, int a, int b)
	{
		int n = 0;
		for(int i = -1; i <= 1; i++)
		{
			for(int j = -1; j <= 1; j++)
			{
				if (!(i == 0 && j ==0) && brd[a+i][b+j])
					n++;
			}
		}
		return n; 
	}

	public static void printBoard(int i, boolean [][] arr)
	{	
		System.out.print("\033[H\033[2J");
		System.out.flush();
		System.out.println("Generation " + i);
		for(int r = 0; r < arr.length; r++)
		{
			for (int c = 0; c < arr[r].length; c++)
			{
				System.out.print(arr[r][c] ? "*" : " ");
				//System.out.print(arr[r][c] + ", ");
			}
			System.out.println();
		}
	}
	public static void fillBoard(boolean[][] arr, int a, String s)
	{
		for(int i = 0; i < s.length(); i++)
		{
			arr[a][i] = (s.charAt(i) == '*');
		}
	}


	static void mySleep(int time) {
        	try {
            		Thread.sleep(time);
        	}
		 catch (InterruptedException e) {
       		}
   	}
}

