
# DeepTakToe

A simple command-line Tic-Tac-Toe game featuring a recursive algorithmic opponent that evaluates all possible outcomes to determine the optimal move.

## Description

**deepTakToe.py**  plays Tic-Tac-Toe by thinking ahead through every possible move. Not just its next one, but every possible game that could happen from the current board.

Here's how it works:  
1. The computer looks at all the empty spots it could play in.  
2. For each possible move, it creates a "virtual game" to see what would happen.
3. Then, it imagines how you might respond to each of those moves. Not just what it thinks you might do, but *every* move you could make.  
4. It keeps building out more possible games — move after move — until the game would end in a win, loss, or draw. These form pyramids of options where one move can lead to thousands of possible outcomes.
5. After imagining all possible outcomes, it looks back and asks:  
   "Which first move gives me the best chance of winning?"  
If it sees that no options remaing can lead to a win it will go for a draw and try to block you to force a tie.  

## Features

- Inefficient, brute-force AI using full-depth recursive game tree evaluation.
- Human vs Computer gameplay in the terminal.
- Move recommendation scoring and outcome tracking.
- Fully self-contained with no external dependencies.

## Future

- Add a GUI interface
- Eventually adapt this into a training program to teach a neural network AI to play tic-tac-toe  

## Author

**Russell Johnson**  
Created: May 31, 2025  
Version: 1.1

## How to Run

### Prerequisites


Ensure you have Python 3 installed on your computer. You can check this by running the following in your terminal:

```bash
# On Mac/Linux:
python3 --version

# On Windows:
python --version
````



If not installed, download it from [python.org](https://www.python.org/downloads/).

### Method 1: Run via Terminal

1. Open Terminal.
2. Navigate to the directory containing `deepTakToe.py`.
3. Run the script with the following terminal command:


```bash
# On Mac/Linux:
python3 deepTakToe.py

# On Windows:
python deepTakToe.py
````

### Method 2: GUI

#### On PC
1. In Windows explorer, open the file *Run_For_Windows.bat* to launch the python script   

#### On Mac
1. Right-click on *deepTakToe.py*   
2. Select **Open With >> Python Launcher**

## How to Play

* The board is indexed from 0 to 8, left to right, top to bottom.
* You play as **`x`**, and the AI plays as **`o`**.
* When prompted, enter the number corresponding to the square you want to play.
* After each game, you can choose to play again or quit.

##  Example Gameplay

```
0: _ 1: _ 2: _
3: _ 4: x 5: _
6: _ 7: _ 8: _
make your move: 4
Considered 549945 possible outcomes.
Square 1 : 0.34
Square 2 : 0.27
...
Best move is to go to square 1 that has a score of 0.34
```

## 📝 License

### GNU GENERAL PUBLIC LICENSE
#### Version 3, 29 June 2007  
This project is for educational use and experimentation.

