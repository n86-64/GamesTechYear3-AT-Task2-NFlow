using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlatformerCharacter : MonoBehaviour {

    private Camera playerCam;
    private Animator characterAnimator;
    private Rigidbody characterBody;

    public GameObject viewTarget;
    public float runSpeed = 10.0f;

	// Use this for initialization
	void Start ()
    {
        playerCam = gameObject.GetComponentInChildren<Camera>();
        playerCam.transform.LookAt(viewTarget.transform);
        playerCam.tag = "MainCamera";
        characterAnimator = gameObject.GetComponent<Animator>();
        characterBody = gameObject.GetComponent<Rigidbody>();
	}
	
	// Update is called once per frame
	void Update ()
    {
        Jump();
        Forward();
	}


    // Move forward
    void Forward()
    {
        float axisVal = Input.GetAxis("Vertical");
        characterAnimator.SetFloat("Speed", axisVal);
        characterBody.velocity = gameObject.transform.forward * runSpeed * axisVal;
    }

    void Jump()
    {
        characterAnimator.SetBool("Jump", Input.GetKeyDown(KeyCode.Space));
    }
}
