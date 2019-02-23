using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GeneratePrediction : MonoBehaviour {

    public GameGenerator generatorTemplate;
    Predictor predictiorEngine;
    public List<string> sceneCategories;
    public List<string> characterCategories;

    // Use this for initialization
    void Awake ()
    {
        predictiorEngine = FindObjectOfType<Predictor>();
        predictiorEngine.predict("image.jpg");
        CreatePredictorObject();
	}
	
	// Update is called once per frame
	void CreatePredictorObject()
    {
        float bestPresiction = 0.0f;
        GameGenerator generator = Instantiate(generatorTemplate);
        DontDestroyOnLoad(generator);
        int searchIndex = 0;
        int bestResult = 0;

        // Generate Scene prediction.
        for(int i = 0; i < predictiorEngine.predictions.Count; i++)
        {
            if (sceneCategories[searchIndex] == predictiorEngine.labels[i])
            {
                if( predictiorEngine.predictions[i] > bestPresiction)
                {
                    bestResult = i;
                    bestPresiction = predictiorEngine.predictions[i];
                }

                searchIndex++;
            }

            if(searchIndex >= sceneCategories.Count) { break; }
        }
        generator.generatedScene = predictiorEngine.labels[bestResult];

        bestResult = 0;
        bestPresiction = 0.0f;
        searchIndex = 0;

        // Generate Character prediction.
        for (int i = 0; i < predictiorEngine.predictions.Count; i++)
        {
            if (characterCategories[searchIndex] == predictiorEngine.labels[i])
            {
                if (predictiorEngine.predictions[i] > bestPresiction)
                {
                    bestResult = i;
                    bestPresiction = predictiorEngine.predictions[i];
                }

                searchIndex++;
            }

            if (searchIndex >= characterCategories.Count) { break; }
        }

        generator.generatedCharacter = predictiorEngine.labels[bestResult];
    }
}
