# CLI Quiz Master

CLI Quiz Master is a Python terminal trivia game. Select a category and
difficulty, answer eight multiple-choice questions, and receive a score
summary. Completed quizzes can be saved to the local high-score leaderboard.

## Features

- Four categories: Science, History, Algebra, and Sports
- Three difficulty choices: Easy, Normal, and Hard
- Hints for Easy questions
- Four answer choices for each question
- Input validation for menu, setup, and question responses
- Ten points for every correct answer, with no penalty for incorrect answers
- A summary showing score, correct and incorrect answers, percentage, and
  questions attempted
- A JSON-backed high-score leaderboard
- Username viewing, editing, and setting
- High-score deletion

## Requirements

- Python 3.10 or newer
- No third-party packages are required to run the game

## How to Run

From the `quiz_game` project directory, run:

```sh
python3 src/main.py
```

Questions, rules, menu options, and saved high scores are stored in
`src/quiz_data.json`. Running the game can update the high-score data.

## Main Menu

1. **Start Quiz** - Choose a category and difficulty, then answer the
   questions.
2. **View High Scores** - Display saved scores in descending score order.
3. **Browse Categories** - Display each category and its available question
   count.
4. **Rules** - Display the game rules and scoring information.
5. **See Username** - Display the username currently associated with the
   session.
6. **Edit/Set Username** - Set a username for the current session or change
   the username associated with an existing saved high score.
7. **Delete My High Score** - Delete the current user's saved high score.
8. **Exit** - Close the game.

The main menu returns after each action until **Exit** is selected.

## How to Play

1. Select **Start Quiz**.
2. Select a category and difficulty.
3. Enter the number for your answer.
4. Type `q` at any question prompt to leave early.
5. Complete all questions to receive a score-saving prompt.
6. Enter a unique username to save the completed score, or leave it blank to
   skip saving.

Easy questions include hints. Normal and Hard questions do not display hints.
An early exit shows a summary but does not save the incomplete score.

## Example Session

```text
Main Menu:

1. Start Quiz
2. View High Scores
3. Browse Categories
4. Rules
5. See Username
6. Edit/Set Username
7. Delete My High Score
8. Exit

Please select an option: 1

Setup Menu:

1. Science
2. History
3. Algebra
4. Sports

Please select a category (1-4): 1

Select Difficulty Level
1. Easy
2. Normal
3. Hard

Please select a difficulty (1-3): 1

Question (1/8): What is the boiling point of water at sea level?
1. 100°C
2. 90°C
3. 80°C
4. 70°C

Your answer (1-4) or 'q' to quit: 1
Correct! Your choice was 100°C.
```

After the final question, the game displays the quiz summary and asks for a
username before saving the score.
