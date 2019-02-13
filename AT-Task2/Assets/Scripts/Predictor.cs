using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;
using System.IO;

public class Predictor : MonoBehaviour
{
    // Predictions from the neural-network. 
    public List<string> labels = new List<string>();
    public List<float> predictions = new List<float>();

	// Use this for initialization
	void Start ()
    {
        loadLabels("labels.txt");
	}

    // Load the labels file into memory.
    public void loadLabels(string fileName)
    {
        labels.Clear();
        predictions.Clear();

        StreamReader fileReader = new StreamReader(Application.dataPath + "\\" + fileName);

        if (fileReader != null)
        {
            while (!fileReader.EndOfStream)
            {
                labels.Add(fileReader.ReadLine());
                predictions.Add(0.0f);
            }
        }

        fileReader.Close();
    }

    // Performs a prediction. Stores the result in an array for later use.
    public void predict(string fileName)
    {
        string prediction = getPredictions(fileName);
        char strCharacter = '\0';
        string valueString = "";
        int labelIndex = 0;

        for(int i = 0; i < prediction.Length; i++)
        {
            strCharacter = prediction[i];
            if(strCharacter != '[' || strCharacter != ']')
            {
                if (strCharacter != ',')
                {
                    valueString += strCharacter;
                }
                else
                {
                    predictions[labelIndex] = float.Parse(valueString);
                    labelIndex++;
                }
            }
        }
    }

    // Returns a prediction value for a label.
    float getPredictionValue(string label)
    {
        return predictions[labels.IndexOf(label)];
    }

    // Gets the predictions from the array utalising the neural-network.
    string getPredictions(string imageFile)
    {
        // The pyhon process with supervising parameters.
        Process neuralNetwork = null;
        ProcessStartInfo pyHandle = new ProcessStartInfo();
        pyHandle.CreateNoWindow = false;
        pyHandle.UseShellExecute = false;
        pyHandle.FileName = "python.exe";
        pyHandle.WindowStyle = ProcessWindowStyle.Normal;
        pyHandle.Arguments = Application.dataPath + "/Externals/cnn-prediction.py " + Application.dataPath + "//cnn-game.hd5 " + Application.dataPath + "//" + imageFile;
        pyHandle.RedirectStandardOutput = true;

        // Loads the network
        neuralNetwork = Process.Start(pyHandle);
        StreamReader reader = neuralNetwork.StandardOutput;

        // Get the output.
        return reader.ReadToEnd();
    }

    
}
