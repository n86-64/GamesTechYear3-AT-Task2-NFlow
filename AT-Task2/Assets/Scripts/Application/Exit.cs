﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Exit : MonoBehaviour
{
    public void quitApplication()
    {
        Application.Quit();
        Debug.Log("Exiting Mate.");
    }

}
