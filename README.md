# CLI Quiz Master

CLI Quiz Master is a terminal trivia game built with Python. Choose a
category and difficulty, answer multiple-choice questions, and receive a
score summary. A completed quiz can be saved to the local high-score
leaderboard with a unique username.

## Features

- Four categories: Science, History, Algebra, and Sports
- Easy, Normal, and Hard difficulty choices
- Hints for Easy questions
- Four answer choices for every question
- Input validation for menu and question responses
- A score of 10 points for each correct answer
- Quiz summaries showing score, correct and incorrect answers, percentage, and
  questions attempted
- A high-score leaderboard saved in `src/quiz_data.json`
- Options to view category information, read the rules, and delete the current
  user's saved score

## Requirements

- Python 3.10 or newer
- No third-party packages are needed to run the game

## How to Run

From this project directory, run:

```sh
python3 src/main.py
```

The game stores leaderboard changes in `src/quiz_data.json`. If you want to
keep the original data unchanged, make a backup of that file before playing.

## How to Play

1. Select **Start Quiz** from the main menu.
2. Select a category and difficulty.
3. Enter the number for your answer.
4. Type `q` at a question prompt to leave the quiz early.
5. Complete every question to enter a username and save the score.

The main menu also includes **View High Scores**, **Browse Categories**,
**Rules**, **Delete My High Score**, and **Exit**.

## Example Session

```text
Main Menu:

1. Start Quiz
2. View High Scores
3. Browse Categories
4. Rules
5. Delete My High Score
6. Exit

Please select an option (1-6): 1

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

After the final question, the game displays the summary and asks whether you
want to register a username for the leaderboard.
