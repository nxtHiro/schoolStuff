// Project Gourd 1 rockJars
// by Marco Flores

import java.util.*;
import java.text.DecimalFormat;

class rockJar
{

	public static void main(String[] args)
	{
	//	Scans for input from stdin
		Scanner s = new Scanner(System.in);
	
	//	Sets up ArrayList for the input
    	ArrayList<Integer> rocks = new ArrayList<Integer>();
	
	//	Populates ArrayList
   		while(s.hasNextInt())
    		{
   	 		rocks.add(s.nextInt());
    		}
	
	//	initializes variable to be used to count number of times a given first digit occurs
		int firstDigit = 0;

	//	initializes int array to keep record of occurrances of 0-9 in the given data sets
		int[] counter = new int[10];
	
	//	initializes total number counter variable
		int totalRocks = 0;

	//	double array for storing percent statisic for each first digit	
		double[] percents = new double[10];
		String[] percentsDisp = new String[10];
		
	//	double for calculating the total percentage of the statistics. Should always equal 100%
		double percentsTotal = 0.00;
		String perTotalDisp = "";
	 	
	//	counts the occurrances of each first digit 0-9 as well as increments the total
		for (int count : rocks)
    		{
      			firstDigit = Integer.parseInt(Integer.toString(count).substring(0, 1));
			counter[firstDigit]++;
			totalRocks++;
		}

	//	calculates the percentage statistic of each first digit occurrance
		for (int i = 0; i < counter.length; i++)
		{
			percents[i] = (double)counter[i] / totalRocks * 100;
			percentsDisp[i] = new DecimalFormat("0.00").format(percents[i]);
			percentsTotal += percents[i];
		}
		
	//	sets up formatting and display
		perTotalDisp = new DecimalFormat("0.00").format(percentsTotal);
		System.out.println("------------------------------");
		System.out.println("Leading Digit\tCount\t     %");
		System.out.println("------------------------------");
		for (int i = 0; i< counter.length; i++){
			System.out.format("%d\t\t", i);
			System.out.format("%d\t", counter[i]);
			System.out.format("%5s%%\n", percentsDisp[i]);	
		}
		System.out.println("------------------------------");
		System.out.format("TOTAL\t\t%d", totalRocks);
		System.out.format("%8s%%\n", perTotalDisp);
		System.out.println("==============================");
	}
}

