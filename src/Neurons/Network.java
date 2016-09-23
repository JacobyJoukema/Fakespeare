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
	private double [] errorDelta;
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
	public double[] compute (double [] input)
	{
		int i,j;
		final int hiddenIndex = inputCnt;
		final int outIndex = inputCnt+hiddenCnt;

		for (i = 0; i<inputCnt;i++)
		{
			fire[i] = input[i];
		}
		int inx = 0;
		for (i = hiddenIndex;i<inputCnt;i++)
		{
			double sum = thresholds[i];
			for (j = 0; j < inputCnt;j++)
			{
				sum+= fire[j] * matrix[inx++];
			}
			fire[i] = threshold(sum);
		}
		double result [] = new double [outputCnt];
		for (i = outIndex; i<neuronCnt;i++)
		{
			double sum = thresholds[i];
			for (j = hiddenIndex; j < outIndex; j++)
			{
				sum+=fire[i]*matrix[inx++];
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
		int i,j;
		final int hiddenInd = inputCnt;
		final int outputInd = inputCnt + hiddenCnt;

		for (i = outputInd; i < neuronCnt; i++)
		{
			error[i] = 0;
		}

		for (i = outputInd; i < neuronCnt; i++)
		{
			error[i] = ideal[i-outputInd] - fire[i];
			globalError += error [i] * error[i];
			errorDelta[i] = error[i] * fire[i] * (1 -fire[i]);
		}

		int winx = inputCnt*hiddenCnt;

		for (i = outputInd; i <neuronCnt; i++)
		{
			for (j = hiddenInd; j <outputCnt;j++)
			{
				accMatrixDelta[winx]+= errorDelta[i]*fire[j];
				error[j] += matrix[winx]*errorDelta[i];
				winx++;
			}
			accThresholdDelta[i] += errorDelta[i];
		}
		for (i = hiddenInd; i < outputInd; i++)
		{
			errorDelta[i] = error[i] * fire[i] * (1- fire[i]);
		}

		winx = 0;
		for (i = hiddenInd; i <outputInd;i++)
		{
			for (j = 0; j <hiddenInd; j++)
			{
				accMatrixDelta[winx] += errorDelta[i] * fire[j];
				error[j] += matrix[winx] *errorDelta[i];
				winx++;
			}
			accThresholdDelta[i] += errorDelta[i];
		}
	}
	public double getError (int len)
	{
		double err = Math.sqrt(globalError/len*outputCnt);
		globalError=0;
		return err;
	}
	public void learn ()
	{
		int i;

		for (i=0; i <matrix.length; i++)
		{
			matrixDelta[i] = learnRate *accThresholdDelta[i] + (momentum*thresholdDelta[i]);
			matrix[i] += matrixDelta;
			accThresholdDelta[i] = 0;
		}
		for (i = inputCnt; i < neuronCnt; i++)
		{
			thresholdDelta[i] = learnRate *accThresholdDelta[i] + (momentum*thresholdDelta[i]);
			thresholds[i] += thresholdDelta[i];
			accThresholdDelta[i] = 0;
		}
	}
	public void reset ()
	{
		int i;
		for (i = 0; i <neuronCnt;i++)
		{
			thresholds[i] = .5 - (Math.random());
			thresholdDelta[i] = 0;
			accThresholdDelta[i] = 0;
		}
		for (i = 0; i <matrix.length;i++)
		{
			matrix[i] = .5 - (Math.random());
			matrixDelta[i] = 0;
			accMatrixDelta[i] = 0;
		}
	}
}
