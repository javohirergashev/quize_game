"""
Quiz game module.
This module only contains the main game loop and logic for running the quiz game.
All user interface and terminal rendering is handled in the menu.py module.
"""

# import quiz_data


def run_quiz_game() -> None:
    """Run the main quiz game loop, handling question display, user input, and scoring."""


def get_available_categories() -> list[str]:
    """Return a list of available quiz categories."""
    # return quiz_data.get_categories()


def get_menu_options() -> list[str]:
    """Return a list of main menu options."""
    return ["Start Quiz", "View High Scores", "Browse Categories", "Rules", "Exit"]


def get_questions_for_category(category: str) -> list[dict]:
    """Return a list of questions for the specified category."""
    # return quiz_data.get_questions_by_category(category)
