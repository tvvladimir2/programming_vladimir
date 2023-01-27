// Tutorial from:
// https://www.youtube.com/watch?v=GkHmp8xj2O0
// Stopped at: 45:20

// Save method as a variable and call later
// https://stackoverflow.com/questions/6695537/is-there-a-way-to-save-a-method-in-a-variable-then-call-it-later-what-if-my-met

using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using System;

// TODO BUG: if all hidden buttons are pushable, taken
// Inter + operator1,  still makes an operation, but it can't add to the list
// Inter + operator2 + Integer 2,  still makes an operation, but it can't add to the list
// These operations do not check if the hidden list has atleast one available slot

// TODO: Grand WIN, grand prize
// Calculate all available time options 
// 00:00    / list 1
// 00:01
// 00:02
// 23:58
// 23:59    / last list
// add lists to a list
// Sort each individual list from lowest to highest
// Check if each each next list is the same and delete copies
// Save available combinations
// Show player how many combinations he has opened out of available

// Surprises
// Enter game at 00:00  // condition at start() ? show $$$$$$
// Enter game at 06:66 - not possible, make something up
// Open a secret button


public class Game : MonoBehaviour
{
    enum GameStatus
    {
        NotStarted,
        AtTheStart,
        FirstIntegerChosen,
        OperatorChosen,
        GameLost,
        GameWon,
    }
    GameStatus gameStatus = GameStatus.NotStarted;  // set the default value GameStatus

    enum GameMessage
    {
        Welcome,
        Success,
        NotInteger,
        TooBig,
        Unconcatenable,
        ShowingOperations,
        GameLost,
        GameWon,
    }
    GameMessage gameMessage = GameMessage.Welcome;

    // Row1: Timer references & input variables
    public CalcButton hour0Button;
    public CalcButton hour1Button;
    public CalcButton minute0Button;
    public CalcButton minute1Button;
    public CalcButton secondsButton;
    private int systemHour0;
    private int systemHour1;
    private int systemMinute0;
    private int systemMinute1;
    private int systemSeconds;

    // Row2: DigitStrip reference & input variables
    // TODO: calculate maximum amount of charachters in a inputTextDigitStrip before Text size starts to diminish
    public Text inputTextDigitStrip;
    private string _welcomeMessage = "      Use timer digits and calculator operators to null the digits under a minute to win. Only operations resulting in integers are allowed."; // Define input values
    private string _usedWelcomeMessage;
    private string _inputString = "";

    // Variables for controlling Frame Independant Update speed
    public float speed = 0.2f;
    private float timer = 0;

    // Row3: Button operations references
    public CalcButton firstCalculatedNumber;
    public CalcButton secondCalculatedNumber;
    public CalcButton thirdCalculatedNumber;
    public CalcButton fourthCalculatedNumber;

    // Row4: Button operations references
    public CalcButton buttonDivide;
    public CalcButton buttonMinus;
    public CalcButton buttonPlus;
    public CalcButton buttonMultiply;
    public CalcButton buttonClear;
    public CalcButton buttonSquareRootOfTwo;
    public CalcButton buttonSquareRootOfThree;
    public CalcButton buttonSquareRootOfFour;
    public CalcButton buttonToThePowerOfTwo;
    public CalcButton buttonToThePowerOfThree;
    public CalcButton buttonToThePowerOfFour;
    public CalcButton buttonConcatenate;
    public CalcButton buttonUnconcatenate;

    // Create lists
    public List<CalcButton> operatorButtonList = new List<CalcButton>();
    public List<CalcButton> CheckFloatToIntegerOperatorButtonList = new List<CalcButton>();
    public List<CalcButton> CheckMaximumDigitsOperatorButtonList = new List<CalcButton>();
    public List<CalcButton> integerButtonList = new List<CalcButton>();
    public List<CalcButton> hiddenButtonList = new List<CalcButton>();

    // Cycle timer
    private int _GameTimer; // Count to 60
    private int _CycleCounter;  // Make sure we make at least one circle
    private int _successCounter;    // Checks if all buttons are pressed
    private int _numberOfOpenedButtons; // Number of buttons that needs to be closed

    // Optional game configurations
    [SerializeField] private bool _fullRestartEnabled = true;
    [SerializeField] private bool _gameLostEnabled = true;
    [SerializeField] private int _maxButtonTextDigitAmount = 6;

    // References for temporary clickable buttons and temmporary variables
    public CalcButton firstSelectedIntegerButton;
    public CalcButton firstSelectedOperatorButton;
    public CalcButton secondSelectedIntegerButton;
    private int _firstIntegerInt;
    private string _firstIntegerString;
    private string _firstOperatorName;
    private string _firstOperatorText;
    private int _secondInteger;
    private float _resultFloat;
    private int _resultInteger;
    private List<int> _unconcatenateResultIntegersList = new List<int>();

    void Start()
    {
        // Clear the lists if Start() runs again and create lists
        operatorButtonList.Clear();
        integerButtonList.Clear();
        hiddenButtonList.Clear();
        CreateButtonLists();

        // Digitstrip running message
        _usedWelcomeMessage = _welcomeMessage;
        _inputString = "";
        // Pass the first _passDigitStripAmountOfLetter letter to the inputTextDigitStrip
        for (int i = 0; i < 20; i++)
        {
            _inputString += _usedWelcomeMessage[i];
        }
        _usedWelcomeMessage = _usedWelcomeMessage.Remove(0, 20);
        inputTextDigitStrip.text = _inputString;

        _successCounter = 0;    // Check if all buttons are pressed

        // Initial update of hours/minutes/seconds
        UpdateSeconds();
        UpdateHoursMinutes();

        EnableDisableIntegersAtStart();
        HideHiddenButtonsAtStart();
        UnpushableOperatorButtonsAtStart();
        secondsButton.SecondsButton();  // Seconds button has custom design at Start
        gameStatus = GameStatus.NotStarted;
    }

    private void PartialStart()
    {
        gameStatus = GameStatus.AtTheStart;
        _successCounter = 0;

        UnpushableOperatorButtonsAtStart();
        //EnableDisableIntegersAtStart();   // Don't need it, because all used buttons are controlled in Main logic
    }

    void Update()
    {
        UpdateSeconds();
        SuccessFailureCheck();
        GameStatusMessage();
    }

    private void UpdateSeconds()
    {
        systemSeconds = System.DateTime.Now.Second;

        // Update secondsButton color from Green to Red (Reversely)
        secondsButton.rgbGreen = (byte)(255 - (systemSeconds * (255 / 60)));    // <max.255 byte> / <total 60 seconds> = 4.25 bytes per second

        // Seconds text for the secondsButton
        secondsButton.thisButtonText.text = "" + systemSeconds;

        // Game timer for full restart
        _GameTimer = systemSeconds;
        if (systemSeconds == 59)
        {
            _CycleCounter = 1;
        }
        if (_GameTimer == 0 && _CycleCounter == 1)
        {
            _CycleCounter = 0;
            if (_fullRestartEnabled)
            {
                Start();
            }
        }
    }

    //TODO Game lost if the last button is equal to 1
    // If time is 00:01, that means you lost before the game started.
    // Need to make an alternative, for example if at least one operation has been performed successfully
    private void SuccessFailureCheck()
    {
        // value 8 means game is won
        // value 7 means one button left
        _successCounter = NumberOfClosedButtons();

        // Game Won conditions
        if (_successCounter == (hiddenButtonList.Count + integerButtonList.Count))
        {
            gameStatus = GameStatus.GameWon;
        }
        // Game lost conditions
        // If only one button left
        else if (_successCounter == (hiddenButtonList.Count + integerButtonList.Count - 1) && _gameLostEnabled )
        {
            gameStatus = GameStatus.GameLost;
        }

        _successCounter = 0;
    }

    private void CreateButtonLists()
    {
        // Add all hidden buttons to a hiddenButtonList
        hiddenButtonList.Add(firstCalculatedNumber);
        hiddenButtonList.Add(secondCalculatedNumber);
        hiddenButtonList.Add(thirdCalculatedNumber);
        hiddenButtonList.Add(fourthCalculatedNumber);

        // Add all operator buttons to a operatorList
        operatorButtonList.Add(buttonDivide);
        operatorButtonList.Add(buttonMinus);
        operatorButtonList.Add(buttonPlus);
        operatorButtonList.Add(buttonMultiply);
        operatorButtonList.Add(buttonClear);
        operatorButtonList.Add(buttonSquareRootOfTwo);
        operatorButtonList.Add(buttonSquareRootOfThree);
        operatorButtonList.Add(buttonSquareRootOfFour);
        operatorButtonList.Add(buttonToThePowerOfTwo);
        operatorButtonList.Add(buttonToThePowerOfThree);
        operatorButtonList.Add(buttonToThePowerOfFour);
        operatorButtonList.Add(buttonConcatenate);
        operatorButtonList.Add(buttonUnconcatenate);

        // Add all operator buttons that require checking for Float to Integer convertion
        CheckFloatToIntegerOperatorButtonList.Add(buttonSquareRootOfTwo);
        CheckFloatToIntegerOperatorButtonList.Add(buttonSquareRootOfThree);
        CheckFloatToIntegerOperatorButtonList.Add(buttonSquareRootOfFour);

        // Add all operator buttons that require checking for Maximum amount of digits
        CheckMaximumDigitsOperatorButtonList.Add(buttonToThePowerOfTwo);
        CheckMaximumDigitsOperatorButtonList.Add(buttonToThePowerOfThree);
        CheckMaximumDigitsOperatorButtonList.Add(buttonToThePowerOfFour);
        CheckMaximumDigitsOperatorButtonList.Add(buttonConcatenate);

        // Add all integer buttons to a integerList
        integerButtonList.Add(hour0Button);
        integerButtonList.Add(hour1Button);
        integerButtonList.Add(minute0Button);
        integerButtonList.Add(minute1Button);
    }

    private void GameStatusMessage()    // In Update() method
    {
        if (gameStatus == GameStatus.NotStarted)
        {
            if (timer >= speed) // Execute code only one `speed` seconds have passed
            {
                if (_usedWelcomeMessage.Length == 0)
                {
                    _usedWelcomeMessage = _welcomeMessage;
                }
                // Make the string like a running line
                _inputString = _inputString.Remove(0, 1);
                _inputString = _inputString + _usedWelcomeMessage[0];
                _usedWelcomeMessage = _usedWelcomeMessage.Remove(0, 1);
                inputTextDigitStrip.text = _inputString;
                timer = 0f;
            }
            else
            {
                // We skip all frames until `timer`is equal to `speed`.
                timer += Time.deltaTime;    // `Time.deltaTime` per frame is around 0.001 seconds. 
            }
        }
        else if (gameStatus == GameStatus.AtTheStart)
        {
            if (gameMessage == GameMessage.Success)
            {
                inputTextDigitStrip.text = NumberOfOpenedButtons() + " integers remaining";
            }
            else if (gameMessage == GameMessage.NotInteger)
            {
                inputTextDigitStrip.text = "Only whole numbers";
            }
            else if (gameMessage == GameMessage.TooBig)
            {
                inputTextDigitStrip.text = "Max int length is " + _maxButtonTextDigitAmount;
            }
            else if (gameMessage == GameMessage.Unconcatenable)
            {
                inputTextDigitStrip.text = "unconcatenable";
            }
        }
        else if (gameStatus == GameStatus.FirstIntegerChosen)
        {
            inputTextDigitStrip.text = "" + _firstIntegerInt;
        }
        else if (gameStatus == GameStatus.OperatorChosen)
        {
            inputTextDigitStrip.text = "" + _firstIntegerInt + " " + _firstOperatorText + " ";
        }
        else if (gameStatus == GameStatus.GameLost)
        {
            inputTextDigitStrip.text = "Game lost. Wait...";
        }
        else if (gameStatus == GameStatus.GameWon)
        {
            inputTextDigitStrip.text = "GameWon!!!";
        }

    }

    private void EnableDisableIntegersAtStart()
    {
        // Push status for integer buttons
        for (int i = 0; i < integerButtonList.Count; i++)
        {
            if (integerButtonList[i].thisButtonText.text == "0")
            {
                integerButtonList[i].DisableButton();
            }
            else
            {
                integerButtonList[i].PushableButton();
            }
        }
    }

    private void UnpushableOperatorButtonsAtStart()
    {
        // Deactivate all operator buttons at Start()
        for (int i = 0; i < operatorButtonList.Count; i++)
        {
            operatorButtonList[i].UnpushableButton();
        }
    }

    private void MakePushableOperatorButtons()
    {
        // Enable operator buttons
        for (int i = 0; i < operatorButtonList.Count; i++)
        {
            operatorButtonList[i].PushableButton();
        }

        gameStatus = GameStatus.FirstIntegerChosen;
    }

    private void HideHiddenButtonsAtStart()
    {
        // Push status
        for (int i = 0; i < hiddenButtonList.Count; i++)
        {
            hiddenButtonList[i].HiddenButton();
        }
    }

    private void DistributeValueToFirstAvailableHiddenButton(int passedValue)
    {
        if (_resultInteger != 0)
        {
            for (int i = 0; i < hiddenButtonList.Count; i++)
            {
                if (hiddenButtonList[i].buttonStatus == CalcButton.ButtonStatus.Hidden)
                {
                    hiddenButtonList[i].thisButtonText.text = "" + passedValue;
                    hiddenButtonList[i].PushableButton();
                    return; // Makes sure it inserts it only once
                }
            }
        }
    }

    /// <summary>
    /// This method returns a total number of Unnulled and UnHidden buttons.
    /// </summary>
    /// <returns>Returns nPushableInIntegers + nUnhiddenInHidden</returns>
    private int NumberOfOpenedButtons()
    {
        _numberOfOpenedButtons = (hiddenButtonList.Count + integerButtonList.Count) - NumberOfClosedButtons();
        return _numberOfOpenedButtons;
    }

    /// <summary>
    /// This method returns a sum of nDisabledInIntegers + nHiddenInHidden
    /// </summary>
    /// <returns>Returns nDisabledInIntegers + nHiddenInHidden</returns>
    private int NumberOfClosedButtons()
    {
        int x = 0;

        for (int i = 0; i < integerButtonList.Count; i++)
        {
            if (integerButtonList[i].buttonStatus == CalcButton.ButtonStatus.Disabled)
            {
                x += 1;
            }
        }

        x = x + NumberOfAvailableHiddenButtons();

        return x;
    }

    /// <summary>
    /// Returns number of available hiddenButtons.
    /// </summary>
    /// <returns>Integer</returns>
    private int NumberOfAvailableHiddenButtons()
    {
        int x = 0;

        for (int i = 0; i < hiddenButtonList.Count; i++)
        {
            if (hiddenButtonList[i].buttonStatus == CalcButton.ButtonStatus.Hidden)
            {
                x += 1;
            }
        }
        return x;
    }

    private void UpdateHoursMinutes()
    {
        // Update the timer for hours
        if (System.DateTime.Now.Hour < 10)
        {
            systemHour0 = 0;
            systemHour1 = System.DateTime.Now.Hour;
        }
        else
        {
            systemHour0 = (System.DateTime.Now.Hour - (System.DateTime.Now.Hour % 10)) / 10;
            systemHour1 = (System.DateTime.Now.Hour) % 10;
        }

        // Update the timer for minutes
        if (System.DateTime.Now.Minute < 10)
        {
            systemMinute0 = 0;
            systemMinute1 = System.DateTime.Now.Minute;
        }
        else
        {
            systemMinute0 = (System.DateTime.Now.Minute - (System.DateTime.Now.Minute % 10)) / 10;
            systemMinute1 = (System.DateTime.Now.Minute) % 10;
        }

        hour0Button.thisButtonText.text = "" + systemHour0;
        hour1Button.thisButtonText.text = "" + systemHour1;
        minute0Button.thisButtonText.text = "" + systemMinute0;
        minute1Button.thisButtonText.text = "" + systemMinute1;
    }

    public void ButtonPressed() // Main logic
    {
        // Round 1
        if (gameStatus == GameStatus.NotStarted || gameStatus == GameStatus.AtTheStart)
        {
            gameMessage = GameMessage.ShowingOperations;
            GetFirstIntegerButtonInfo();
            MakePushableOperatorButtons();
        }
        // Round 2
        else if (gameStatus == GameStatus.FirstIntegerChosen)
        {
            // If we press Integer after the Integer, send us the round one
            if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Integer"))
            {
                firstSelectedIntegerButton.PushableButton();
                gameStatus = GameStatus.AtTheStart;
                ButtonPressed();
                return;
            }
            // If we press Operator2, we go to Round 3 (needs a second Integer)
            else if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Operator2"))
            {
                GetOperatorButtonInfo();
                gameStatus = GameStatus.OperatorChosen;
            }
            // If we press Unconcatenate
            else if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Unconcatenate"))
            {
                GetOperatorButtonInfo();

                // Return to PartialStart() - an integer from integerButtonList always has one digit
                if (integerButtonList.Contains(firstSelectedIntegerButton))
                {
                    Unconcatenate();
                    firstSelectedIntegerButton.DisableButton();
                    firstSelectedOperatorButton.PushableButton();

                    // Create new buttons by distributing integers
                    DistributeUnconcatenatedNumbers();
                    PartialStart();
                }
                else if (hiddenButtonList.Contains(firstSelectedIntegerButton))
                {
                    // If it is possible to insert, proceeds (Use absolute number
                    if ((NumberOfAvailableHiddenButtons() + 1) >= Math.Abs(_firstIntegerInt).ToString().Length)     // _firstIntegerString.Length
                    {
                        Unconcatenate();
                        firstSelectedIntegerButton.HiddenButton();
                        firstSelectedOperatorButton.PushableButton();

                        // Create new buttons by distributing integers
                        DistributeUnconcatenatedNumbers();
                        gameMessage = GameMessage.Success;
                        PartialStart();
                    }
                    // If failed to concatenate
                    else
                    {
                        firstSelectedIntegerButton.PushableButton();
                        firstSelectedOperatorButton.PushableButton();
                        gameMessage = GameMessage.Unconcatenable;
                        PartialStart();
                    }
                }
            }
            // If we press Clear, we move to PartialStart()
            else if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Clear"))
            {
                firstSelectedIntegerButton.PushableButton();
                firstSelectedOperatorButton.PushableButton();
                EventSystem.current.SetSelectedGameObject(null);
                gameMessage = GameMessage.Welcome;
                PartialStart();
            }
            // If we press Operator 1
            else if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Operator1"))
            {
                GetOperatorButtonInfo();
                _resultFloat = CalculateOneIntegerOperation(_firstOperatorName, _firstIntegerInt);
                OneIntegerSequence();
            }
        }
        // Round 3
        else if (gameStatus == GameStatus.OperatorChosen)
        {
            // If we press Operator after the Operator, send us the round two
            if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Operator2"))
            {
                firstSelectedOperatorButton.PushableButton();   // Previous button is now pushable
                gameStatus = GameStatus.FirstIntegerChosen;
                ButtonPressed();    // Launches EventSystem and automatically choose another operator
                return;
            }
            // If we press Operator1 during Round 3
            else if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Operator1"))
            {
                firstSelectedOperatorButton.PushableButton();
                gameStatus = GameStatus.FirstIntegerChosen;
                ButtonPressed();    // Launches EventSystem and automatically choose another operator
                return;
            }
            // If we press Clear
            else if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Clear"))
            {
                // Deselect current objects
                EventSystem.current.SetSelectedGameObject(null);
                firstSelectedIntegerButton.PushableButton();
                firstSelectedOperatorButton.PushableButton();
                gameMessage = GameMessage.Welcome;
                PartialStart();
            }
            // If we choose second Integer
            else if (EventSystem.current.currentSelectedGameObject.GetComponent<Button>().CompareTag("Integer"))
            {
                GetSecondIntegerButtonInfo();

                if (_firstOperatorName == "Concatenate" && _secondInteger < 0)
                {
                    // Failure to concatenate because _secondInteger is below 0
                    firstSelectedIntegerButton.PushableButton();
                    firstSelectedOperatorButton.PushableButton();
                    secondSelectedIntegerButton.PushableButton();
                    gameMessage = GameMessage.Unconcatenable;
                    PartialStart();
                }
                else
                {
                    TwoIntegersOperation();

                    // Check if the resultValue is an Integer
                    if (CheckIfFloatIsAnInteger(_resultFloat))
                    {
                        // If True, hide used buttons and Null or Zero them
                        SuccessFirstSelectedButtonDisableOrHide();
                        SuccessSecondSelectedButtonDisableOrHide();

                        // Create a new button
                        // If resultInteger is zero, do not create a new button
                        _resultInteger = (int)_resultFloat;
                        DistributeValueToFirstAvailableHiddenButton(_resultInteger);
                        gameMessage = GameMessage.Success;
                        PartialStart();
                    }
                    else
                    {
                        firstSelectedIntegerButton.PushableButton();
                        firstSelectedOperatorButton.PushableButton();
                        secondSelectedIntegerButton.PushableButton();
                        PartialStart();
                        gameMessage = GameMessage.NotInteger;
                    }
                }
            }
        }
    }

    private void SuccessSecondSelectedButtonDisableOrHide()
    {
        if (hiddenButtonList.Contains(secondSelectedIntegerButton))
        {
            secondSelectedIntegerButton.thisButtonText.text = "";
            secondSelectedIntegerButton.HiddenButton();
        }
        else
        {
            secondSelectedIntegerButton.thisButtonText.text = "0";
            secondSelectedIntegerButton.DisableButton();
        }
    }

    private void OneIntegerSequence()
    {
        if (CheckFloatToIntegerOperatorButtonList.Contains(firstSelectedOperatorButton))
        {
            // Check if the resultValue is an Integer
            if (CheckIfFloatIsAnInteger(_resultFloat))
            {
                // If True, hide used buttons and Null or Zero them
                SuccessFirstSelectedButtonDisableOrHide();

                // Create a new button and pass value to it
                // If resultInteger is zero, do not create a new button
                _resultInteger = (int)_resultFloat;
                DistributeValueToFirstAvailableHiddenButton(_resultInteger);
                gameMessage = GameMessage.Success;
                PartialStart();
            }
            else
            {
                firstSelectedIntegerButton.PushableButton();
                firstSelectedOperatorButton.PushableButton();
                gameMessage = GameMessage.NotInteger;
                PartialStart();
            }
        }
        else if (CheckMaximumDigitsOperatorButtonList.Contains(firstSelectedOperatorButton))
        {
            // Check if the resultValue is an Integer
            if (CheckMaximumAmountOfDigits(_resultFloat))
            {
                // If True, hide used buttons and Null or Zero them
                SuccessFirstSelectedButtonDisableOrHide();

                // Create a new button and pass value to it
                // If resultInteger is zero, do not create a new button
                _resultInteger = (int)_resultFloat;
                DistributeValueToFirstAvailableHiddenButton(_resultInteger);
                gameMessage = GameMessage.Success;
                PartialStart();
            }
            else
            {
                firstSelectedIntegerButton.PushableButton();
                firstSelectedOperatorButton.PushableButton();
                gameMessage = GameMessage.TooBig;
                PartialStart();
            }
        }
    }

    private void SuccessFirstSelectedButtonDisableOrHide()
    {
        if (hiddenButtonList.Contains(firstSelectedIntegerButton))
        {
            firstSelectedIntegerButton.thisButtonText.text = "";
            firstSelectedIntegerButton.HiddenButton();
        }
        else if (integerButtonList.Contains(firstSelectedIntegerButton))
        {
            firstSelectedIntegerButton.thisButtonText.text = "0";
            firstSelectedIntegerButton.DisableButton();
        }
    }

    private void DistributeUnconcatenatedNumbers()
    {
        for (int i = 0; i < hiddenButtonList.Count; i++)
            if (hiddenButtonList[i].buttonStatus == CalcButton.ButtonStatus.Hidden && _unconcatenateResultIntegersList.Count > 0)
            {
                hiddenButtonList[i].thisButtonText.text = "" + _unconcatenateResultIntegersList[0];
                _unconcatenateResultIntegersList.RemoveAt(0);
                hiddenButtonList[i].PushableButton();
            }
    }

    private void GetFirstIntegerButtonInfo()
    {
        // Detect text and click
        _firstIntegerString = EventSystem.current.currentSelectedGameObject.GetComponentInChildren<Text>().text;
        _firstIntegerInt = int.Parse(_firstIntegerString);  // Positive or negative
        firstSelectedIntegerButton = EventSystem.current.currentSelectedGameObject.GetComponent<CalcButton>();
        firstSelectedIntegerButton.PressedButton();

        // Deselect current object
        EventSystem.current.SetSelectedGameObject(null);
    }

    private void GetSecondIntegerButtonInfo()
    {
        // Click to detect button name
        _secondInteger = int.Parse(EventSystem.current.currentSelectedGameObject.GetComponentInChildren<Text>().text);
        secondSelectedIntegerButton = EventSystem.current.currentSelectedGameObject.GetComponent<CalcButton>();
        secondSelectedIntegerButton.PressedButton();

        // Deselect current object
        EventSystem.current.SetSelectedGameObject(null);
    }

    private void GetOperatorButtonInfo()
    {
        // Click to detect operator button name
        _firstOperatorName = EventSystem.current.currentSelectedGameObject.name;
        _firstOperatorText = EventSystem.current.currentSelectedGameObject.GetComponentInChildren<Text>().text;
        firstSelectedOperatorButton = EventSystem.current.currentSelectedGameObject.GetComponent<CalcButton>();
        firstSelectedOperatorButton.PressedButton();

        // Deselect current object
        EventSystem.current.SetSelectedGameObject(null);
    }

    bool CheckIfFloatIsAnInteger(float x)   // we receive _resultFloat
    {
        try
        {
            int y = Int32.Parse(x.ToString());  // Does not give us very high numbers
            return true;
        }
        catch
        {
            return false;
        }
    }

    bool CheckMaximumAmountOfDigits(float x)
    {
        int y = (int)x;
        string z = y.ToString();
        if (z.Length <= _maxButtonTextDigitAmount)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    private void TwoIntegersOperation()
    {
        if (_firstOperatorName == "Plus")
        {
            _resultFloat = _firstIntegerInt + _secondInteger;
        }
        else if (_firstOperatorName == "Minus")
        {
            _resultFloat = _firstIntegerInt - _secondInteger;
        }
        else if (_firstOperatorName == "Multiply")
        {
            _resultFloat = _firstIntegerInt * _secondInteger;
        }
        else if (_firstOperatorName == "Divide")
        {
            _resultFloat = (float)_firstIntegerInt / (float)_secondInteger;
        }
        else if (_firstOperatorName == "Concatenate")
        {
            _resultFloat = int.Parse(string.Concat(_firstIntegerInt, _secondInteger));
        }
    }

    private float CalculateOneIntegerOperation(string _firstOperatorName, int _firstIntegerInt)
    {
        if (_firstOperatorName == "SquareRootOfTwo")
        {
            _resultFloat = Mathf.Sqrt(_firstIntegerInt);
        }
        else if (_firstOperatorName == "SquareRootOfThree")
        {
            _resultFloat = Mathf.Pow(_firstIntegerInt, 1f / 3f);
        }
        else if (_firstOperatorName == "SquareRootOfFour")
        {
            _resultFloat = Mathf.Pow(_firstIntegerInt, 1f / 4f);
        }
        else if (_firstOperatorName == "ToThePowerOfTwo")
        {
            _resultFloat = (float)Math.Pow(_firstIntegerInt, 2);
        }
        else if (_firstOperatorName == "ToThePowerOfThree")
        {
            _resultFloat = (float)Math.Pow(_firstIntegerInt, 3);
        }
        else if (_firstOperatorName == "ToThePowerOfFour")
        {
            _resultFloat = (float)Math.Pow(_firstIntegerInt, 4);
        }
        return _resultFloat;
    }

    private void Unconcatenate()
    {
        // Clean the list from previous operations, just in case there were some
        //_unconcatenateResultIntegersList.Clear();

        // Convert each `Char` to an `Int` & add to a list 
        //foreach (char i in _firstIntegerString)
        //{
        //    // Skip integers == 0
        //    if (int.Parse(i.ToString()) == 0)
        //        continue;

        //    _unconcatenateResultIntegersList.Add(int.Parse(i.ToString()));
        //}

        // Clean the list from previous operations, just in case there were some
        _unconcatenateResultIntegersList.Clear();

        // If the String is negative, delete index [0] and remember this fact
        bool negativeInFirstIntegerString = false;
        if (_firstIntegerString.StartsWith("-"))
        {
            negativeInFirstIntegerString = true;
            _firstIntegerString = _firstIntegerString.Remove(0, 1);
        }

        //// Convert each `Char` to an `Int` & add to a list 
        foreach (char i in _firstIntegerString)
        {
            // If Char is "0", we skip
            if (i == '0')    // Delete previous: int.Parse(i.ToString()) == 0
            {
                continue;
            }
            // If negative was detected before, apply minus to first iteration
            if (i == 0 && negativeInFirstIntegerString == true)
            {
                _unconcatenateResultIntegersList.Add(int.Parse(i.ToString()) * (-1));   // Simply multiply the number by -1, was before: 
                continue;
            }
            _unconcatenateResultIntegersList.Add(int.Parse(i.ToString()));  // was before 
        }
    }
}
