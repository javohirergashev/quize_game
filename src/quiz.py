"""
Quiz game module.
This module only contains the main game loop and logic for running the quiz game.
All user interface and terminal rendering is handled in the menu.py module.
"""

import quiz_data


def get_category() -> list[str]:
    """Return a list of available categories.
    :return: List of category names.
    :rtype: list[str]
    """

    return [category.capitalize() for category in quiz_data.QUIZ_DATA]


def get_category_and_count() -> list[(str, int)]:
    """Return a list of available categories and their question counts.

    :return: List of tuples containing (category_name, question_count).
    :rtype: list[tuple[str, int]]
    """
    categories_and_counts = []

    for category in quiz_data.QUIZ_DATA:
        category_name = category.capitalize()
        question_count = len(quiz_data.QUIZ_DATA[category]["hard"]) + len(quiz_data.QUIZ_DATA[category]["normal"])
        categories_and_counts.append((category_name, question_count))

    return categories_and_counts


def get_menu_options() -> list[str]:
    """Return a list of main menu options.

    :return: List of menu option strings.
    :rtype: list[str]
    """
    return ["Start Quiz", "View High Scores", "Browse Categories", "Rules", "Exit"]


def get_questions_for_category(category: str, difficulty: str) -> list[dict]:
    """Return a list of questions for the specified category and difficulty.

    :param category: The name of the category to retrieve questions for.
    :type category: str
    :param difficulty: The difficulty level of the questions to retrieve (e.g., "easy", "medium", "hard").
    :type difficulty: str
    :return: List of question dictionaries.
    :rtype: list[dict]
    """

    if difficulty.lower() == "easy":
        difficulty = "normal"  # Map "easy" to "normal" in the quiz data

    return [question for question in quiz_data.QUIZ_DATA[category.lower()][difficulty.lower()]]


def get_high_scores() -> list[dict]:
    """Return a list of past high scores. Sorted in descending order by score.

    :return: List of dictionaries representing past user session data.
    :rtype: list[dict]
    """

    if not quiz_data.HIGH_SCORES:
        return []

    return sorted(quiz_data.HIGH_SCORES.values(), key=lambda x: x["score"], reverse=True)


def get_past_usernames() -> list[str]:
    """Return a list of past usernames in all lower case from the high scores.

    :return: List of usernames.
    :rtype: list[str]
    """
    return [username for username in quiz_data.HIGH_SCORES]


def save_high_score(session_dict: dict) -> bool:
    """Save the current session's score to the high scores list.

    :param session_dict: Dictionary containing the current quiz session's data.
    :type session_dict: dict
    :return: True if the score was saved successfully, False otherwise.
    :rtype: bool
    """
    quiz_data.HIGH_SCORES[session_dict["player_name"].lower()] = session_dict
    return True


def get_rules() -> str:
    """Return the game rules, scoring mechanics, and hint details.

    :return: A string containing the game rules and mechanics.
    :rtype: str
    """

    return quiz_data.QUIZ_RULES
