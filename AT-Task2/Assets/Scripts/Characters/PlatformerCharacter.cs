using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlatformerCharacter : MonoBehaviour {

    private Camera playerCam;
    private Animator characterAnimator;
    private Rigidbody characterBody;
    public int health = 100;
    private bool dead = false;

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
	
    public void damage(int damageValue)
    {
        health -= damageValue;
    }

    public int getHealth()
    {
        return health;
    }

	// Update is called once per frame
	void Update ()
    {
        if (health <= 0 && !dead)
        {
             Dead();
        }

        if (dead)
        {
            if (characterAnimator.GetCurrentAnimatorStateInfo(0).IsName("Dead"))
            {
                characterAnimator.SetBool("Dead", false);
            }
        }
        else
        {

            Jump();
            Forward();
            Rotation();
        }
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
        // Triggers death animation.
        characterAnimator.SetBool("Dead", true);
        dead = true;
    }
}
