using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GeneratePrediction : MonoBehaviour {

	// Use this for initialization
	void Start ()
    {
        Predictor predictiorEngine = FindObjectOfType<Predictor>();
        predictiorEngine.predict("image.jpg");
	}
	
	// Update is called once per frame
	void Update ()
    {
		
	}
}
