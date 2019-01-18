using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlatformerCharacter : MonoBehaviour {

    private Camera playerCam;
    private Animator characterAnimator;
    private Rigidbody characterBody;
    private int health;
    private bool dead;


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
        if(health <= 0 && dead)
        {
            Dead();
        }

        if (characterAnimator.GetCurrentAnimatorStateInfo(0).IsName("Dead"))
        {
            characterAnimator.SetBool("Dead", false);
        }

        Jump();
        Forward();
        Rotation();
        
        dead = Input.GetKeyDown(KeyCode.K); 
	}


    // Move forward
    void Forward()
    {
        float axisVal = Input.GetAxis("Vertical");
        characterAnimator.SetFloat("Speed", axisVal);
        characterBody.velocity = transform.forward * runSpeed * axisVal;
    }

    void Jump()
    {
        characterAnimator.SetBool("Jump", Input.GetKeyDown(KeyCode.Space));
    }

    void Rotation()
    {
        float val = Input.GetAxis("Horizontal");
        gameObject.transform.Rotate(new Vector3(0.0f, val, 0.0f));
    }

    void Dead()
    {
        // the character is dead.
        characterAnimator.SetBool("Dead", true);
    }
}
