using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Diagnostics;
using System.IO;

public class Predictor : MonoBehaviour
{
    private string pyOut = null;

	// Use this for initialization
	void Start ()
    {
        getPredictions("test.jpg");
	}
	
	// Update is called once per frame
	void Update ()
    {
		
	}

    // Gets the predictions from the array.
    public void getPredictions(string imageFile)
    {
        // The pyhon process with supervising parameters.
        Process neuralNetwork = null;
        ProcessStartInfo pyHandle = new ProcessStartInfo();
        pyHandle.CreateNoWindow = false;
        pyHandle.UseShellExecute = false;
        pyHandle.FileName = "python.exe";
        pyHandle.WindowStyle = ProcessWindowStyle.Normal;
        pyHandle.Arguments = "D:\\Nflow\\cnn2\\cnn-prediction.py D:\\Nflow\\cnn2\\cnn-game.hd5 D:\\Nflow\\cnn2\\test.jpg";
        pyHandle.RedirectStandardOutput = true;

        // Perform the traning.
        neuralNetwork = Process.Start(pyHandle);

        StreamReader reader = neuralNetwork.StandardOutput;

        // Get the output.
        UnityEngine.Debug.Log(reader.ReadToEnd());
    }
}
