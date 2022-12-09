using System;
using System.Collections;
using System.Collections.Generic;
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
        if (input == "1")
        {
            level = 1;
            password = level1Passwords[2];
            StartGame();
        }
        else if (input == "2")
        {
            level = 2;
            password = level2Passwords[2];
            StartGame();
        }
        else if (input == "007")
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
        Terminal.WriteLine("You have chosen level " + level);
        Terminal.WriteLine("Please neter your password: ");
    }


    // Update is called once per frame
    void CheckPassword(string input)
    {
        if (input == password)
        {
            Terminal.WriteLine("Well DONE!");
        }
        else
        {
            Terminal.WriteLine("Wrong password, sorry");
        }
    }
}
