// Project Gourd 2 intGrid
// by Marco Flores

import java.util.*;

class intGrid
{
	public static void main(String[] args)
	{
	//	initializes Scanner object
		Scanner s = new Scanner(System.in);

	//	initializes an integer ArrayList
		ArrayList<Integer> grid = new ArrayList<Integer>();
	
	//	initializes a variable to be used to store the highest sum
		int highestSum = 0;

	//	initializes a variable to be used to store the current calculated sum to be compared to the highest sum
		int currSum = 0;

	//	puts Scanner input data into an ArrayList
		while(s.hasNextInt())
    		{
   		grid.add(s.nextInt());
   		}
	
	//	initializes a 20x20 array
		int[][] gridArray = new int[20][20];
	
	//	initializes a counter variable for incrementing through ArrayList grid
		int arrayListCounter = 0;

	//	populates the 20x20 array gridArray with data from the ArrayList grid
		for (int i = 0; i < 20; i++)
		{
			for (int j = 0; j < 20; j++)
			{
				gridArray[i][j] = grid.get(arrayListCounter).intValue();
				arrayListCounter++;		
			}
		
		}
		
	//	calculates the highest sum
		for (int i = 0; i < 20; i++)
		{
			for (int j = 0; j < 17; j++)
			{
				currSum = (gridArray[i][j] + gridArray[i][j+1] + gridArray[i][j+2] + gridArray[i][j+3]);					
				if (highestSum < currSum)
				{
					highestSum = currSum;
				}
			}
		}

	//	prints the highest sum
		System.out.println(highestSum);
    	}
}
