using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ScrollTwo : MonoBehaviour
{
    public List<string> label;
    public List<Sprite> Texture;

    public bool characterTexture = false;
    
    public GameObject startPos;
    public GameObject endPos;

    public Text textField;

    // Use this for initialization
    void Start()
    {
        GameGenerator generator = FindObjectOfType<GameGenerator>();
        int index = -1;

        if (characterTexture)
        {
            index = label.FindIndex(x => x == generator.generatedCharacter);
            if (index != -1)
            {
                textField.text = "An " + generator.generatedCharacter + " character";
            }
        }
        else
        {
            index = label.FindIndex(x => x == generator.generatedScene);
            if(index != -1)
            {
                textField.text = "Set at a " + generator.generatedScene;
            }
        }

        if (index >= 0) { GetComponent<Image>().sprite = Texture[index]; }
    }

    // Update is called once per frame
    void Update()
    {
        gameObject.GetComponent<RectTransform>().anchoredPosition += new Vector2(2, 0);

        if (Mathf.Abs(gameObject.GetComponent<RectTransform>().anchoredPosition.x - endPos.GetComponent<RectTransform>().anchoredPosition.x) < 2.0)
        {
            gameObject.GetComponent<RectTransform>().anchoredPosition = startPos.GetComponent<RectTransform>().anchoredPosition;
        }
    }
}
