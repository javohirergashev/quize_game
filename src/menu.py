"""
Menu and user interface system for the quiz game.

Handles all terminal rendering and user input, keeping business logic
and state management isolated in other modules.
"""

import sys


def wait_and_clear_screen() -> None:
    """Prompt the user to press Enter, then clear the terminal screen."""
    input("\nPress \033[32mEnter\033[0m to continue...")
    sys.stdout.write("\033[2J\033[1;1H")
    sys.stdout.flush()


def display_setup_menu(categories: list[str]) -> tuple[str, str]:
    """Prompt the user to select a category and difficulty.

    :param categories: Available category names to display to the user.
    :type categories: list[str]
    :return: A tuple containing the selected (category, difficulty).
    :rtype: tuple[str, str]
    """

    while True:
        print("\n\033[1;39;49mSetup Menu:\033[0m\n")
        print("\033[1;93m ★ ★ ★  \033[1;92mChoose Categories\033[1;93m  ★ ★ ★\033[0m\n")
        for index, category in enumerate(categories, start=1):
            print(f"{index}. {category}")

        try:
            category_choice = int(input(f"\nPlease select a category (1-{len(categories)}): "))
            if 1 <= category_choice <= len(categories):
                selected_category = categories[category_choice - 1]
                wait_and_clear_screen()
                break
            else:
                print(f"\n\033[0;91;49mInvalid Choice.\033[0m Please enter a number between \033[32m1 and {len(categories)}.\033[0m")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

        wait_and_clear_screen()

    while True:
        print("\n\033[1;93m ★ ★ ★  \033[1;92mSelect Difficulty Level\033[1;93m  ★ ★ ★\033[0m\n")
        difficulties = ["Easy", "Normal", "Hard"]
        for index, difficulty in enumerate(difficulties, start=1):
            print(f"{index}. {difficulty}")

        try:
            difficulty_choice = int(input(f"\nPlease select a difficulty (1-{len(difficulties)}): "))
            if 1 <= difficulty_choice <= len(difficulties):
                selected_difficulty = difficulties[difficulty_choice - 1]
                wait_and_clear_screen()
                break
            else:
                print(f"\n\033[0;91;49mInvalid Choice.\033[0m Please enter a number between \033[32m1 and {len(difficulties)}.\033[0m")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

        wait_and_clear_screen()

    return selected_category, selected_difficulty


def display_main_menu(menu) -> int:
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
                print(f"\n\033[0;91;49mInvalid Choice.\033[0m Please enter a number between\033[0;36;49m 1 and {len(menu)}.\033[0m")
        except ValueError:
            print("\n\033[1;31mInvalid input.\033[0m Please enter a number.")

        wait_and_clear_screen()


def display_rules(rule: str) -> None:
    """Display game rules, scoring mechanics, and hint details.
    :param rule: Quiz rules and scoring mechanics to display.
    :type rule: str
    """
    print(rule)


def display_high_scores(high_scores: list[dict]) -> None:
    """Display past high scores.

    :param high_scores: List of dicts representing past user sessions data.
    :type high_scores: list[dict]
    """

    if not high_scores:
        print("\n\033[1;93m ★ ★ ★  \033[1;92mNo High Scores Yet\033[1;93m  ★ ★ ★\033[0m\n")
        return

    print("\n\033[1;93m ★ ★ ★  \033[1;92mHigh Scores\033[1;93m  ★ ★ ★\033[0m\n")
    for index, score_record in enumerate(high_scores, start=1):
        player_name = score_record.get("player_name", "N/A")
        score = score_record.get("score", 0)
        category = score_record.get("category", "N/A")
        difficulty = score_record.get("difficulty", "N/A")
        date = score_record.get("date", "N/A")
        max_score = score_record.get("total_questions", 0) * 10  # Assuming each question is worth 10 points

        print(f"{index}. \033[1;36m{player_name.capitalize()}\033[0m - Score: {score} / {max_score} - Category: {category} - Difficulty: {difficulty} - Date (mm/dd/yy): {date}")
        print(f"\t\033[1;32mCorrect Answers: {score_record.get('correct_answers', 0)}\033[0m, \033[1;31mIncorrect Answers: {score_record.get('incorrect_answers', 0)}\033[0m")


def display_category_info(categories: list[tuple[str, int]]) -> None:
    """Display available categories and the total question count for each.

    :param categories: List of tuples containing (category_name, question_count).
    :type categories: list[tuple[str, int]]
    """
    print("\n\033[1;93m ★ ★ ★  \033[1;92mAvailable Category Info\033[1;93m  ★ ★ ★\033[0m\n")

    for index, (category, count) in enumerate(categories, start=1):
        print(f"\033[1;32m{index}. {category}:\033[0m {count} questions available.")


def get_user_info() -> str:
    """Prompt the user to enter their name for score tracking.

    :return: The trimmed username entered by the player.
    :rtype: str
    """

    print("\n\033[1;93m ★ ★ ★  \033[1;92mEnter Your Username\033[1;93m  ★ ★ ★\033[0m\n")
    return input("Name (leave blank to not record your score): ").strip()


def display_question_and_get_choice(category: str, question: str, choices: list[str], hint: str | None, question_index: int, total_questions: int) -> int | None:
    """Display a question prompt, list choices, and optionally provide a hint.

    Handles input validation and returns the 0-indexed selection.

    :param category: The category of the question being asked.
    :type category: str
    :param question: The question text to display.
    :type question: str
    :param choices: List of answer choices to present to the user.
    :type choices: list[str]
    :param hint: Optional hint text to assist the user.
    :type hint: str or None
    :param question_index: The index of the current question.
    :type question_index: int
    :param total_questions: The total number of questions in the quiz.
    :type total_questions: int
    :return: The 0-based index of the user's selected choice. Returns None if the user chooses to exit.
    :rtype: int | None
    """

    print("\033[0;30;46m\nCategory:\033[0m \033[1;32m" + category + "\033[0m")
    print(f"\033[0;39;100mQuestion ({question_index}/{total_questions}):\033[0m \033[1;32m" + question + "\033[0m")

    for i, choice in enumerate(choices, start=1):
        print(f"\033[1;32m{i}.\033[0m {choice}")

    if hint:
        print(f"\n\033[1;96mHint:\033[0m \033[1;97m{hint}\033[0m")

    while True:
        try:
            user_input = input("\nYour answer (1-4) or 'q' to quit: ").strip()

            if user_input.lower() == "q":
                return None

            if user_input.isdigit():
                choice_index = int(user_input) - 1
                if 0 <= choice_index < len(choices):
                    return choice_index
                else:
                    print("\n\033[1;31mInvalid input. Please enter a number between 1 and 4. Or 'q' to quit.\033[0m")
            else:
                print("\n\033[1;31mInvalid input. Please enter a number. Or 'q' to quit.\033[0m")
        except ValueError:
            print("\n\033[1;31mInvalid input. Please enter a number. Or 'q' to quit.\033[0m")


def display_result(is_correct: bool, correct_choice: str) -> None:
    """Display feedback to the user based on whether their answer was correct.

    :param is_correct: True if the user's answer was correct, False otherwise.
    :type is_correct: bool
    :param correct_choice: The label or text of the correct answer.
    :type correct_choice: str
    """
    if is_correct:
        print(f"\n\033[1;32mCorrect!\033[0m Your choice was {correct_choice}.")
    else:
        print(f"\n\033[1;31mIncorrect.\033[0m Your choice was {correct_choice}.")


def display_summary(current_session_record: dict) -> None:
    """Display the final score summary after the quiz session.

    :param current_session_record: Dictionary containing the current quiz session's data.
    :type current_session_record: dict
    """

    category = current_session_record.get("category", "N/A")
    difficulty = current_session_record.get("difficulty", "N/A")
    score = current_session_record.get("score", 0)
    correct_answers = current_session_record.get("correct_answers", 0)
    incorrect_answers = current_session_record.get("incorrect_answers", 0)
    number_of_questions_attempted = current_session_record.get("questions_attempted", 0)
    total_questions = current_session_record.get("total_questions", 0)

    # Calculate percentage based on attempted questions, avoiding division by zero
    percentage = (correct_answers / number_of_questions_attempted * 100) if number_of_questions_attempted > 0 else 0.0

    print("\n\033[1;93m★ ★ ★  \033[1;92mQUIZ SUMMARY\033[1;93m  ★ ★ ★\033[0m\n")
    print(f"Score: {score} / {10 * total_questions} (10 points per question)")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")
    print(f"Percentage based on attempted questions: {round(percentage)}%")
    print(f"Questions Attempted: {number_of_questions_attempted}")
    print(f"Total Questions in {category} ({difficulty}): {total_questions}")

    # Clear the screen after displaying the summary
    wait_and_clear_screen()


def display_delete_high_score_result(is_deleted: bool, username) -> None:
    """Prompt the user to enter their username to delete their high score.

    :param is_deleted: True if the high score was deleted successfully, False otherwise.
    """
    if is_deleted:
        print(f"\n\033[1;32mHigh score for '{username}' deleted successfully!\033[0m")
    else:
        print(f"\n\033[1;31mNo high score found for '{username}'\033[0m")
        print("\n\033[1;33mHigh score deletion canceled.\033[0m")
