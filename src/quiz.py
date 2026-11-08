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


def get_questions_for_category(category: str) -> list[dict]:
    """Return a list of questions for the specified category.

    :param category: The name of the category to retrieve questions for.
    :type category: str
    :return: List of question dictionaries.
    :rtype: list[dict]
    """
    return [question for question in quiz_data.QUIZ_DATA[category.lower()]]


def get_high_scores() -> list[dict]:
    """Return a list of past high scores.

    :return: List of dicts representing past user scores and dates.
    :rtype: list[dict]
    """


def save_high_score(session_dict: dict) -> bool:
    """Save the current session's score to the high scores list.

    :param session_dict: Dictionary containing the current quiz session's data.
    :type session_dict: dict
    :return: True if the score was saved successfully, False otherwise.
    :rtype: bool
    """


def get_rules() -> str:
    """Return the game rules, scoring mechanics, and hint details.

    :return: A string containing the game rules and mechanics.
    :rtype: str
    """

    return quiz_data.QUIZ_RULES
