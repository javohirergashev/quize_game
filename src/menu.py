"""
Menu and user interface system for the quiz game.

Handles all terminal rendering and user input, keeping business logic
and state management isolated in other modules.
"""

import sys


def wait_and_clear_screen() -> None:
    """Prompt the user to press Enter, then clear the terminal screen."""
    input("\nPress \033[32mEnter\033[0m to continue...")
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def show_setup_menu(categories: list[str]) -> tuple[str, str]:
    """Prompt the user to select a category and difficulty.

    :param categories: Available category names to display to the user.
    :type categories: list[str]
    :return: A tuple containing the selected (category, difficulty).
    :rtype: tuple[str, str]
    """

    while True:
        print("\n\033[1;39;49mSetup Menu:\033[0m\n")
        print("Available Categories:")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        try:
            category_choice = int(input(f"\nPlease select a category (1-{len(categories)}): "))
            if 1 <= category_choice <= len(categories):
                selected_category = categories[category_choice - 1]
                break
            else:
                print(f"\n\033[0;91;49mInvalid Choice.\033[0m Please enter a number between \033[32m1 and {len(categories)}.\033[0m")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

        wait_and_clear_screen()

    while True:
        print("\nSelect Difficulty Level:")
        difficulties = ["Easy", "Medium", "Hard"]
        for index, difficulty in enumerate(difficulties, start=1):
            print(f"{index}. {difficulty}")

        try:
            difficulty_choice = int(input(f"\nPlease select a difficulty (1-{len(difficulties)}): "))
            if 1 <= difficulty_choice <= len(difficulties):
                selected_difficulty = difficulties[difficulty_choice - 1]
                break
            else:
                print(f"\n\033[0;91;49mInvalid Choice.\033[0m Please enter a number between \033[32m1 and {len(difficulties)}.\033[0m")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

        wait_and_clear_screen()

    return selected_category, selected_difficulty


def show_main_menu(menu) -> int:
    """Display the main menu options and prompt the user for input.

    :param menu: List of menu option strings to display.
    :type menu: list[str]
    :return: The 0-based index of the user's selected menu option.
    :rtype: int
    """

    while True:
        print("\n\033[1;39;49mMain Menu:\033[0m\n")
        for index, option in enumerate(menu, start=1):
            print(f"{index}. {option}")

        try:
            choice = int(input("\nPlease select an option (1-5): "))
            if 1 <= choice <= len(menu):
                # Only clear if they picked an active menu option, NOT exit
                # Assuming the last option in menu is 'Exit':
                if choice != len(menu):
                    wait_and_clear_screen()
                return choice - 1
            else:
                print(f"\n\033[0;91;49mInvalid Choice.\033[0m Please enter a number between \033[32m1 and {len(menu)}.\033[0m")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

        wait_and_clear_screen()


def show_rules() -> None:
    """Display game rules, scoring mechanics, and hint details."""


def show_high_scores(high_scores: list[dict]) -> None:
    """Display past high scores.

    :param high_scores: List of dicts representing past user scores and dates.
    :type high_scores: list[dict]
    """


def browse_categories(categories: list[tuple[str, int]]) -> None:
    """Display available categories and the total question count for each.

    :param categories: List of tuples containing (category_name, question_count).
    :type categories: list[tuple[str, int]]
    """


def get_user_info() -> str:
    """Prompt the user to enter their name for score tracking.

    :return: The trimmed username entered by the player.
    :rtype: str
    """


def display_question_and_get_choice(question: str, choices: list[str], hint: str | None) -> int:
    """Display a question prompt, list choices, and optionally provide a hint.

    Handles input validation and returns the 0-indexed selection.

    :param question: The question text to display.
    :type question: str
    :param choices: List of answer choices to present to the user.
    :type choices: list[str]
    :param hint: Optional hint text to assist the user.
    :type hint: str or None
    :return: The 0-based index of the user's selected choice.
    :rtype: int
    """


def display_result(is_correct: bool, correct_choice: str) -> None:
    """Display feedback to the user based on whether their answer was correct.

    :param is_correct: True if the user's answer was correct, False otherwise.
    :type is_correct: bool
    :param correct_choice: The label or text of the correct answer.
    :type correct_choice: str
    """


def display_summary(score: int) -> None:
    """Display the final score summary after the quiz session.

    :param score: The user's final score. Score is presented as a percentage of correct answers out of number of questions attempted.
    :type score: int
    """
