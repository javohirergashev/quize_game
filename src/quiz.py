"""
Quiz game module.
This module only contains the main game loop and logic for running the quiz game.
All user interface and terminal rendering is handled in the menu.py module.
"""

import json
import pathlib

json_data_path = pathlib.Path(__file__).parent / "quiz_data.json"


def get_category() -> list[str]:
    """Return a list of available categories.
    :return: List of category names.
    :rtype: list[str]
    """

    # Load the quiz data from the JSON file and extract the category names
    with open(json_data_path, "r") as file:
        categories = list(json.load(file)["QUIZ_DATA"].keys())

    return [category.capitalize() for category in categories]


def get_category_and_count() -> list[(str, int)]:
    """Return a list of available categories and their question counts.

    :return: List of tuples containing (category_name, question_count).
    :rtype: list[tuple[str, int]]
    """

    with open(json_data_path, "r") as file:
        QUIZ_DATA = json.load(file)["QUIZ_DATA"]

    categories_and_counts = []

    for category in QUIZ_DATA:
        category_name = category.capitalize()
        question_count = len(QUIZ_DATA[category]["hard"]) + len(QUIZ_DATA[category]["normal"])
        categories_and_counts.append((category_name, question_count))

    return categories_and_counts


def get_menu_options() -> list[str]:
    """Return a list of main menu options.

    :return: List of menu option strings.
    :rtype: list[str]
    """
    with open(json_data_path, "r") as file:
        return json.load(file)["MENU_OPTIONS"]


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

    with open(json_data_path, "r") as file:
        QUIZ_DATA = json.load(file)["QUIZ_DATA"]
        return [question for question in QUIZ_DATA[category.lower()][difficulty.lower()]]


def get_high_scores() -> list[dict]:
    """Return a list of past high scores. Sorted in descending order by score.

    :return: List of dictionaries representing past user session data.
    :rtype: list[dict]
    """

    with open(json_data_path, "r") as file:
        HIGH_SCORES = json.load(file).get("HIGH_SCORES", None)

    if not HIGH_SCORES:
        return []

    return sorted(HIGH_SCORES.values(), key=lambda x: x["score"], reverse=True)


def get_past_usernames() -> list[str]:
    """Return a list of past usernames in all lower case from the high scores.

    :return: List of usernames.
    :rtype: list[str]
    """
    with open(json_data_path, "r") as file:
        return [username for username in json.load(file).get("HIGH_SCORES")]


def save_high_score(session_dict: dict) -> bool:
    """Save the current session's score to the high scores list.

    :param session_dict: Dictionary containing the current quiz session's data.
    :type session_dict: dict
    :return: True if the score was saved successfully, False otherwise.
    :rtype: bool
    """
    try:
        player_name = session_dict["player_name"].lower()

        # Read existing data
        with open(json_data_path, "r") as file:
            data = json.load(file)

        # Update data
        data["HIGH_SCORES"][player_name] = session_dict

        # Overwrite the file
        with open(json_data_path, "w") as file:
            json.dump(data, file, indent=4)

        return True

    except (FileNotFoundError, json.JSONDecodeError, KeyError, OSError) as e:
        print(f"Failed to save high score: {e}")
        return False


def get_rules() -> str:
    """Return the game rules, scoring mechanics, and hint details.

    :return: A string containing the game rules and mechanics.
    :rtype: str
    """

    with open(json_data_path, "r") as file:
        return json.load(file).get("QUIZ_RULES", "")


def delete_high_score(username: str) -> bool:
    """Delete the high score for the specified username.

    :param username: The username whose high score should be deleted.
    :type username: str
    :return: True if the high score was deleted successfully, False otherwise.
    :rtype: bool
    """

    username = username.lower()  # Ensure the username is in lower case for consistency

    try:
        # Read existing data
        with open(json_data_path, "r") as file:
            data = json.load(file)

        # Check if the username exists in the high scores
        if username in get_past_usernames():
            del data["HIGH_SCORES"][username]

            # Overwrite the file with updated data
            with open(json_data_path, "w") as file:
                json.dump(data, file, indent=4)

            return True
        else:
            return False

    except (FileNotFoundError, json.JSONDecodeError, KeyError, OSError) as e:
        print(f"Failed to delete high score: {e}")
        return False


def edit_username(old_username: str, new_username: str) -> tuple[bool, str]:
    """Edit the username in the high scores list.

    :param old_username: The current username of the user.
    :type old_username: str
    :param new_username: The new username to replace the old one.
    :type new_username: str
    :return: A tuple containing a boolean indicating success and a message string.
    :rtype: tuple[bool, str]
    """

    old_username = old_username.lower()
    new_username = new_username.lower()

    try:
        # Read existing data
        with open(json_data_path, "r") as file:
            data = json.load(file)

        # Check if the old username exists and the new username does not already exist
        if old_username in get_past_usernames() and new_username not in get_past_usernames():
            data["HIGH_SCORES"][new_username] = data["HIGH_SCORES"].pop(old_username)
            data["HIGH_SCORES"][new_username]["player_name"] = new_username  # Update the player_name in the session data

            # Overwrite the file with updated data
            with open(json_data_path, "w") as file:
                json.dump(data, file, indent=4)

            return (True, f"Username changed from '{old_username}' to '{new_username}' successfully.")
        elif new_username in get_past_usernames():
            return (False, f"Username '{new_username}' already exists in the high scores. Please choose a different name.")
        else:
            return (False, f"Username '{old_username}' does not exist in the high scores. Please finish the quiz and save your score first.")

    except (FileNotFoundError, json.JSONDecodeError, KeyError, OSError) as e:
        return (False, f"Failed to edit username: {e}")
