// Tutorial at:
// https://www.youtube.com/watch?v=TCkDQwMhTtk
// Stopped at: 00:00
// Finished project: https://github.com//cwgtech/UICalc

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

// Make button exist on this game object
[RequireComponent(typeof(Button))]
public class CalcButton : MonoBehaviour
{
    // Every button needs a reference to its text label
    public Button thisButton;
    public Text thisButtonText;

    // Control seconds color
    public byte rgbRed = 125;   // not used
    public byte rgbGreen = 125; // from 255 to 0

    // Probably default states are not needed.
    public enum ButtonStatus
    {
        Pushable,
        Pressed,
        Unpushable,
        Disabled,
        Seconds,
        Hidden,
    }
    public ButtonStatus buttonStatus;  // set the default value to `Alive`

    // Start is called before the first frame update
    void Start()
    {
        // There are no parameters in `GetComponent()` to tell us how to find the Button
        // gives access to Rigidbody component of the object
        thisButton = GetComponent<Button>();    // Initialize the reference, fetches a componebnt of type Button
        thisButtonText = GetComponentInChildren<Text>();

        // Add listener - don't need it
        //thisButton.onClick.AddListener(OnButtonClicked);    // register a listener
    }

    public void PushableButton()
    {
        thisButton.GetComponent<Image>().color = new Color32(255, 100, 38, 255);    // Orange
        thisButtonText.GetComponent<Text>().color = new Color32(255, 255, 255, 255);    // White
        buttonStatus = ButtonStatus.Pushable;
        thisButton.interactable = true;
    }

    public void PressedButton()
    {
        thisButton.GetComponent<Image>().color = new Color32(50, 90, 220, 255);    // Blue
        thisButtonText.GetComponent<Text>().color = new Color32(255, 100, 38, 255);    // Orange
        buttonStatus = ButtonStatus.Pressed;
        thisButton.interactable = false;
    }

    public void UnpushableButton()
    {
        thisButton.GetComponent<Image>().color = new Color32(100, 100, 130, 255);    // Dark Grey 1
        thisButtonText.GetComponent<Text>().color = new Color32(50, 50, 50, 255);    // Light Grey 1
        buttonStatus = ButtonStatus.Unpushable;
        //thisButton.enabled = false;   // leaves the button on the screen, the user can't click it, but does NOT use the disabled color:
        thisButton.interactable = false;    // leaves the button on the screen with the disabled color and the user can't click it:
    }

    public void DisableButton()
    {
        thisButton.GetComponent<Image>().color = new Color32(35, 35, 48, 255);    // Dark Grey 2
        thisButtonText.GetComponent<Text>().color = new Color32(72, 72, 72, 255);    // Light Grey 2
        thisButtonText.text = "0";
        buttonStatus = ButtonStatus.Disabled;
        thisButton.interactable = false;
    }

    public void HiddenButton()
    {
        thisButton.GetComponent<Image>().color = new Color32(0, 0, 0, 255);    // Black
        thisButtonText.GetComponent<Text>().color = new Color32(0, 0, 0, 255);    // Black
        thisButtonText.text = "";
        buttonStatus = ButtonStatus.Hidden;
        thisButton.interactable = false;
    }

    public void SecondsButton()
    {
        thisButton.GetComponent<Image>().color = new Color32(125, rgbGreen, 0, 255);    // Light grey
        thisButtonText.GetComponent<Text>().color = new Color32(255, 255, 150, 255);    // Light yellow
        buttonStatus = ButtonStatus.Seconds;
        thisButton.interactable = false;
    }

    // Debug keys
    void Update()
    {
        // Update Seconds color
        if (buttonStatus == ButtonStatus.Seconds)
        {
            thisButton.GetComponent<Image>().color = new Color32(125, rgbGreen, 0, 255);    // Light grey
        }

        // Debug keys
        if (Input.GetKeyDown(KeyCode.U))
        {
            PushableButton();
        }
        if (Input.GetKeyDown(KeyCode.I))
        {
            PressedButton();
        }
        if (Input.GetKeyDown(KeyCode.O))
        {
            UnpushableButton();
        }
        if (Input.GetKeyDown(KeyCode.P))
        {
            DisableButton();
        }
    }

    // Method to hook up to our button function
    //public void OnButtonClicked()   // AddListener assigned
    //{
    //    if (buttonStatus == ButtonStatus.Pushable)
    //    //Debug.Log("Tapped: " + buttonTextField.text);   // returns `Button` `text` value
    //    //Debug.Log(EventSystem.current.currentSelectedGameObject.name);  // returns `Button` `name` in hierarchy
    //    print("Button Cliked");
    //    PressedButton();
    //}
}