using System.Collections;
using System.IO;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Webcam : MonoBehaviour {

    public Dropdown dropdownMenu;

    WebCamTexture webcamHandle;
    RawImage imageComp;
    WebCamDevice[] devices;

    int selectedCamera = -1;

	// Use this for initialization
	void Start ()
    {
        imageComp = gameObject.GetComponent<RawImage>();
        webcamHandle = new WebCamTexture();
        devices = WebCamTexture.devices;
        List<Dropdown.OptionData> items = new List<Dropdown.OptionData>();

        for (int i = 0; i < devices.Length; i++)
        {
            Dropdown.OptionData newOption = new Dropdown.OptionData();
            newOption.image = null;
            newOption.text = devices[i].name;
            items.Add(newOption);
        }
        selectedCamera = 0;

        if (devices.Length > 0)
        {
            webcamHandle.deviceName = devices[selectedCamera].name;
            imageComp.texture = webcamHandle;
            webcamHandle.Play();
        }

        dropdownMenu.AddOptions(items);
        dropdownMenu.RefreshShownValue();
    }
	
	// Update is called once per frame
	void Update ()
    {
        CheckDropdown();
	}

    void CheckDropdown()
    {
        if(dropdownMenu.value != selectedCamera)
        {
            selectedCamera = dropdownMenu.value;
            webcamHandle.Stop();
            webcamHandle.deviceName = devices[selectedCamera].name;
            webcamHandle.Play();
        }
    }

    // Takes a snapshot and saves to disk.
    public void TakeSnapshot()
    {
        // Here we will allow a snapshot to be taken.
        Texture2D texture = new Texture2D(webcamHandle.width, webcamHandle.height);
        texture.SetPixels(webcamHandle.GetPixels());
        byte[] data = texture.EncodeToJPG();
        File.WriteAllBytes(Application.dataPath + "\\image.jpg", data);
        SceneManager.LoadScene("GenerationSummery");
        webcamHandle.Stop();
    }
}
