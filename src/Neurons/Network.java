package Neurons;

public class Network
{
	private double globalError;
	private int inputCnt;
	private int hiddenCnt;
	private int outputCnt;
	private int neuronCnt;
	private int weightCnt;
	private double learnRate;
	private double momentum;
	private double errorDelta;
	private double [] fire;
	private double [] matrix;
	private double [] error;
	private double [] accMatrixDelta;
	private double [] thresholds;
	private double [] matrixDelta;
	private double [] accThresholdDelta;
	private double [] thresholdDelta;

	//Constructor
	public Network (int inputCnt, int hiddenCnt,int outputCnt, double learnRate, double momentum)
	{
		this.learnRate = learnRate;
		this.momentum = momentum;

		this.inputCnt = inputCnt;
		this.hiddenCnt = hiddenCnt;
		this.outputCnt = outputCnt;

		neuronCnt = inputCnt+hiddenCnt+outputCnt;
		weightCnt = (inputCnt*hiddenCnt) + (hiddenCnt*outputCnt);

		fire = new double [neuronCnt];
		matrix = new double[weightCnt];
		matrixDelta = new double[weightCnt];
		thresholds = new double [neuronCnt];
		errorDelta = new double [neuronCnt];
		error = new double [neuronCnt];
		accThresholdDelta = new double [neuronCnt];
		accMatrixDelta = new double [neuronCnt];
		thresholdDelta = new double [neuronCnt];

		reset();
	}
	public double[] compute (double [] input[])
	{
		final int hiddenIndex = inputCnt;
		final int outIndex = inputCnt+hiddenCnt;

		for (int i = 0; i<inputCnt;i++)
		{
			fire[i] = input[i];
		}
		int inx = 0;
		for (int i = hiddenIndex;i<inputCnt;i++)
		{
			double sum = thresholds[i];
			for (int j = 0; j < inputCnt;j++)
			{
				sum+= fire[j] * matrix[inx++];
			}
			fire[i] = threshold(sum);
		}
		double result [] = new double [outputCnt];
		for (int i = outIndex; i<neuronCnt;i++)
		{
			double sum = thresholds[i];
			for (j = hiddenIndex; j < outIndex; j++)
			{
				sum+=fire[i]*matrix[inx++]
			}
			fire[i] = threshold(sum);
			result[i-outIndex]=fire[i];
		}
		return result;
	}
	public double threshold (double sum)
	{
		return 1/(1+Math.exp(-1.0*sum));
	}
	public void calcError(double ideal [])
	{

	}
	public double getError (int len)
	{
		double err = Math.sqrt(globalError/len*outputCnt);
		globalError=0;
		return err;
	}
	public void learn ()
	{

	}
	public void reset ()
	{

	}
}
