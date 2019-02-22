using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DeletionScript : MonoBehaviour
{

    public void deleteGameGenerator()
    {
        GameGenerator generator = FindObjectOfType<GameGenerator>();
        if (generator)
        {
            Destroy(generator.gameObject);
        }
    }
}
