using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnCharacter : MonoBehaviour {

    public List<string> label;
    public List<GameObject> characterPrefabs;

    // Use this for initialization
    void Start ()
    {
        GameGenerator generator = FindObjectOfType<GameGenerator>();
        int characterToSpawn = 0;

        characterToSpawn = label.FindIndex(x => x == generator.generatedCharacter);
        Instantiate(characterPrefabs[characterToSpawn], gameObject.transform.position, Quaternion.Euler(Vector3.zero));
    }
	
	// Update is called once per frame
	void Update ()
    {
		
	}

    public void RespawnCharacter()
    {

    }
}
