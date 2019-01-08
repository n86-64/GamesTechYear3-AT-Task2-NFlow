using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class SceneChanger : MonoBehaviour
{
    public void quitApplication()
    {
        Application.Quit();
        Debug.Log("Exiting Mate.");
    }


    public void startGame()
    {
        SceneManager.LoadScene("GeneratorScene");
    }

    public void backToMenu()
    {
        SceneManager.LoadScene("Main Menu");
    }
}
