using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Scroll : MonoBehaviour {

    public GameObject startPos;
    public GameObject endPos;

    // Use this for initialization
    void Start ()
    {
		
	}
	
	// Update is called once per frame
	void Update ()
    {
        gameObject.GetComponent<RectTransform>().anchoredPosition += new Vector2(2, 0);

        if(Mathf.Abs(gameObject.GetComponent<RectTransform>().anchoredPosition.x - endPos.GetComponent<RectTransform>().anchoredPosition.x) < 2.0)
        {
            gameObject.GetComponent<RectTransform>().anchoredPosition = startPos.GetComponent<RectTransform>().anchoredPosition;
        }
	}
}
