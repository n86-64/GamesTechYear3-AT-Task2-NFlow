using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using UnityEngine.SceneManagement;

public class AppFileBrowser : MonoBehaviour {

	// Use this for initialization
	public void OpenFileBrowser()
    {
        SimpleFileBrowser.FileBrowser.SetFilters(false, new string[]{ ".jpg", ".JPG"});
        SimpleFileBrowser.FileBrowser.ShowLoadDialog(LoadImage, OnCancel, false, Application.dataPath, "Load an Image");
    }
	
	void LoadImage(string imageName)
    {
        File.Copy(imageName, Application.dataPath + "\\image.jpg", true);
        SceneManager.LoadScene("GenerationSummery");
    }

    void OnCancel()
    {}
}
