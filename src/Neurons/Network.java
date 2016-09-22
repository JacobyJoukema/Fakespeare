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
		thresholds = new double [neuronCnt]
	}
	public double[] compute (double [] input[])
	{
		
	}
	public void calcError(double ideal [])
	{
		
	}
	public double getError (int len)
	{
		return 0;
	}
	public void learn ()
	{
		
	}
	public void reset ()
	{
		
	}
}
