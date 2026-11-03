def show_setup_menu(categories: list[str]) -> tuple[str, str]:
    """Prompt the user to select a category and difficulty.

    :param categories: Available category names to display to the user.
    :type categories: list[str]
    :return: A tuple containing the selected (category, difficulty).
    :rtype: tuple[str, str]
    """


def show_menu() -> str:
    """Display the main menu options and prompt the user for input.

    :return: The trimmed choice entered by the user.
    :rtype: str
    """


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
