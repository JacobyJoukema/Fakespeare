package Train;

import Networks.NetworkBase;

public class Trainer
{
  public static void trainDouble ()
  {
    double xorIn [] [] = {
      {0,0},
      {1,0},
      {0,1},
      {1,1}
    };
    double [][] xorIdeal = {
      {0},{1},{1},{0}
    };

  System.out.println("Start");

  NetworkBase net = new NetworkBase (2,3,1,0.7,0.9);

  for (int i=0; i <= 10000; i++)
  {
    for (int j = 0; j < xorIn.length;j++)
    {
      net.compute(xorIn[j]);
      net.calcError(xorIdeal[j]);
      net.learn();
    }
    System.out.println("Trial " + i + " Error " + net.getError(xorIn.length));
  }
  System.out.println ("Recall:");
  for (int i = 0; i < xorIn.length;i++)
  {
    for (int j = 0; j < xorIn[0].length;j++)
    {
      System.out.println (xorIn[i][j] + ":");
    }
    double out [] = net.compute(xorIn[i]);
    System.out.println ("=" + out[0]);
  }
  }
}
