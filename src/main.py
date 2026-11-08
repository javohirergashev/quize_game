import sys

import menu
import quiz

# Retro-Arcade Palette
GOLD = "\033[1;93m"
GREEN = "\033[1;92m"
CYAN = "\033[1;96m"
WHITE = "\033[1;97m"
DIM = "\033[2;37m"
RESET = "\033[0m"


def print_welcome() -> None:
    """Clear screen and display arcade welcome"""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("\n\n")
    print(f"""
    {GOLD}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲{RESET}
          {GREEN}★  {WHITE}CLI QUIZ MASTER{RESET} {GREEN}: READY PLAYER ONE  ★{RESET}
    {GOLD}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲{RESET}
    {CYAN}► Test your trivia skills across categories & ranks!{RESET}
    """)


def print_goodbye() -> None:
    """Display the energetic retro-arcade exit banner."""
    print(f"""
        {GOLD}★ ★ ★  {GREEN}GAME OVER : THANK YOU FOR PLAYING!{GOLD}  ★ ★ ★{RESET}
            {CYAN}► {WHITE}Final stats logged to the leaderboard.{RESET}
    {DIM}Press up-arrow in your shell to restart anytime. Until next run!{RESET}
    """)


def init_quiz_session() -> dict:
    """Initialize a new quiz session with default values.

    :return: A dictionary representing the initial state of the quiz session.
    :rtype: dict
    """
    return {
        "player_name": None,
        "score": 0,
        "total_questions": 0,
        "correct_answers": 0,
        "incorrect_answers": 0,
        "category": None,
        "difficulty": None,
        "percentage": 0.0,
        "date": None,
    }


def start_quiz() -> None:
    """Start the quiz game by initializing a session and displaying the setup menu."""
    quiz_session = init_quiz_session()
    quiz_session["category"], quiz_session["difficulty"] = menu.show_setup_menu(quiz.get_category())

    # while True:


def main(first_run=True) -> None:
    """Main entry point for the quiz game application."""

    # If this is the first run, display the welcome message
    if first_run:
        print_welcome()

    quiz_options = quiz.get_menu_options()  # Get the main menu options from the quiz module
    user_choice = menu.show_main_menu(quiz_options)  # Get the user's menu choice from the menu module

    if user_choice == quiz_options.index("Exit"):
        print_goodbye()
        return  # Exit the program

    if user_choice == quiz_options.index("Start Quiz"):
        start_quiz()  # Start the quiz if the user selected "Start Quiz"
        menu.wait_and_clear_screen()
        main(False)  # Restart the main menu after the quiz

    menu_actions = {
        quiz_options.index("View High Scores"): lambda: menu.show_high_scores(quiz.get_high_scores()),
        quiz_options.index("Browse Categories"): lambda: menu.browse_categories(quiz.get_category_and_count()),
        quiz_options.index("Rules"): lambda: menu.show_rules(quiz.get_rules()),
    }

    if user_choice in menu_actions:
        menu_actions[user_choice]()  # Execute the corresponding action
        menu.wait_and_clear_screen()
        main(False)  # Restart the main menu


if __name__ == "__main__":
    main()
