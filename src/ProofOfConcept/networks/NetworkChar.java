package networks;

public class NetworkChar extends NetworkBase
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
	private char [] fire;
	private double [] matrix;
	private double [] error;
	private double [] accMatrixDelta;
	private double [] thresholds;
	private double [] matrixDelta;
	private double [] accThresholdDelta;
	private double [] thresholdDelta;

  public NetworkChar (int inputCnt, int hiddenCnt,int outputCnt, double learnRate, double momentum)
	{
		this.learnRate = learnRate;
		this.momentum = momentum;

		this.inputCnt = inputCnt;
		this.hiddenCnt = hiddenCnt;
		this.outputCnt = outputCnt;

		neuronCnt = inputCnt+hiddenCnt+outputCnt;
		weightCnt = (inputCnt*hiddenCnt) + (hiddenCnt*outputCnt);

		fire = new char [neuronCnt];
		matrix = new double[weightCnt];
		matrixDelta = new double[weightCnt];
		thresholds = new double [neuronCnt];
		errorDelta = new double [neuronCnt];
		error = new double [neuronCnt];
		accThresholdDelta = new double [neuronCnt];
		accMatrixDelta = new double [weightCnt];
		thresholdDelta = new double [neuronCnt];

		reset();
	}

  public char compute (char [] input)
  {
    int i,j;
		final int hiddenInd = inputCnt;
		final int outInd = inputCnt+hiddenCnt;

		for (i = 0; i<inputCnt;i++)
		{
			fire[i] = input[i];
		}
		int inx = 0;
		for (i = hiddenInd;i<outInd;i++)
		{
			double sum = thresholds[i];
			for (j = 0; j < inputCnt;j++)
			{
				sum+= fire[j] * matrix[inx++];
			}
			fire[i] = threshold(sum);
		}
		char result [] = new char [outputCnt];
		for (i = outInd; i<neuronCnt;i++)
		{
			double sum = thresholds[i];
			for (j = hiddenInd; j < outInd; j++)
			{
				sum+=fire[j]*matrix[inx++];
			}
			fire[i] = threshold(sum);
			result[i-outInd]=fire[i];
		}
		return result;
  }

  public void calcError(char ideal [])
	{
		int i,j;
		final int hiddenInd = inputCnt;
		final int outputInd = inputCnt + hiddenCnt;

		for (i = inputCnt; i < neuronCnt; i++)
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
			for (j = hiddenInd; j <outputInd;j++)
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

  public double threshold (double sum)
	{
		return 1/(1+Math.exp(-1.0*sum));
	}
}
