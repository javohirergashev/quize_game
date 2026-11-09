# Reflections

## 1. Challenge

One challenging part of building this project was coordinating the quiz flow
with the different menus. The program needs to collect a category and
difficulty, display each question, validate the answer, update the score, and
then return to the main menu. I overcame this by separating responsibilities
into functions and modules: `main.py` controls the session, `menu.py` handles
terminal output and input, and `quiz.py` loads and updates the JSON data. This
made each part easier to follow and helped me handle invalid input without
crashing the game.

## 2. Technical Concept

I gained a deeper understanding of lists of dictionaries. Each question is a
dictionary containing its question text, answer choices, correct-answer index,
and sometimes a hint. The questions for a category and difficulty are stored
in a list, so the game can loop through them one at a time. The quiz session
and each leaderboard record are also dictionaries, which lets the program
store related values such as the score, category, difficulty, and number of
correct answers under descriptive keys instead of relying on positions.
