using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneChanger : MonoBehaviour
{
    public List<string> labels;
    public List<string> sceneNames;

    public void quitApplication()
    {
        Application.Quit();
        Debug.Log("Exiting Mate.");
    }

    public void startGame()
    {
        SceneManager.LoadScene("GeneratorScene");
    }

    public void startLevel()
    {
        GameGenerator generator = FindObjectOfType<GameGenerator>();
        string sceneName = "Game Scene";

        // Here the map should be chosen acording to the generated scene.
        if (generator.generatedScene != "null")
        {
            int index = labels.FindIndex(x => x == generator.generatedScene);
            sceneName = sceneNames[index];
        }

        SceneManager.LoadScene(sceneName);
    }

    public void backToMenu()
    {
        SceneManager.LoadScene("Main Menu");
    }
}
