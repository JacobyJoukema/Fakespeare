package Main;

import Neurons.Network;

public class Main 
{
	public static void main (String [] args)
	{
		Network neural = new Network ()
		double input [] = {0.0,1.0};
		double output [] = neural.compute(input);
		for (double out: output)
		{
			System.out.println(out);
		}
	}
}
