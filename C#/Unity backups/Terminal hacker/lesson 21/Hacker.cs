/*
using System;
using System.Collections;
using System.Collections.Generic;
*/
using UnityEngine;

// Lesson: 18. Arrays Of Variables
// Source code at:
// https://github.com/CompleteUnityDeveloper2/2_Terminal_Hacker/blob/master/Assets/Hacker.cs

public class Hacker : MonoBehaviour
{
    // Game configuration data
    string[] level1Passwords = { "books", "aisle", "self", "password", "font", "borrow"};
    string[] level2Passwords = { "prisoner", "handcuffs", "holster", "uniform", "arrest"};

    // Game state
    int level;
    enum Screen { MainMenu, Password, Win};
    Screen currentScreen;
    string password;

    /*
    // A test function. Test if random number is generating or not. Can delete this function.
    void Update()
    {
        int index = Random.Range(0, level1Passwords.Length);
        print(index);
    }
    */

    //Use this for initialization
    void Start()
    {
        ShowMainMenu ();
    }

    void ShowMainMenu ()
    {
        currentScreen = Screen.MainMenu;
        Terminal.ClearScreen();
        Terminal.WriteLine("What would you like to hack into?");
        Terminal.WriteLine("Pess 1 for the local library");
        Terminal.WriteLine("Press 2 for the police station");
        Terminal.WriteLine("Enter your selection");
    }

    void OnUserInput(string input)
    {
        if (input == "menu")    // we can always go direct to main menu
        {
            ShowMainMenu();
        }
        else if (currentScreen == Screen.MainMenu)
        {
            RunMainMenu(input);
        }
        else if (currentScreen == Screen.Password)
        {
            CheckPassword(input);
        }
    }

    void RunMainMenu(string input)
    {
        bool  isValidLevelNumber = (input == "1" || input == "2");
        if (isValidLevelNumber)
        {
            level = int.Parse(input);   // Converts a string to an integer
            StartGame();
        }
        else if (input == "007")    // easter egg
        {
            Terminal.WriteLine("Please select a level Mr Bond");
        }
        else
        {
            Terminal.WriteLine("Please choose a valid level");
        }
    }

    void StartGame()
    {
        currentScreen = Screen.Password;
        Terminal.ClearScreen();
        switch(level)
        {
            case 1:
                password = level1Passwords[Random.Range(0, level1Passwords.Length)];
                break;
            case 2:
                password = level2Passwords[Random.Range(0, level2Passwords.Length)];
                break;
            default:
                Debug.LogError("Invalid level number");
                break;
        }
        Terminal.WriteLine("Enter your password: ");
    }


    // Update is called once per frame
    void CheckPassword(string input)
    {
        if (input == password)
        {
            DisplayWinScreen();
        }
        else
        {
            Terminal.WriteLine("Wrong password, sorry");
        }
    }

    void DisplayWinScreen()
    {
        currentScreen = Screen.Win;
        Terminal.ClearScreen();
        ShowLevelReward();
    }

    void ShowLevelReward()
    {
        switch(level)
        {
            case 1:
                Terminal.WriteLine("Have a book for level 1");
                Terminal.WriteLine(@"
|--|
|  |
====
                
                "); // draw ASCII
                break;
            case 2:
                Terminal.WriteLine("Have a ball for level 2");
                Terminal.WriteLine(@"
/--\
|   |
\--/             
                "); // draw ASCII
                break;
            default:
                Debug.LogError("Invalid level reached");
                break;

        }
    }
}
