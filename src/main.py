import menu
import quiz


def welcome_message() -> None:
    """Display a welcome message to the user."""
    print("Welcome to the CLI QUIZ MASTER!")
    print("Get ready to test your knowledge across various categories and difficulties.")


def main() -> None:
    """Main entry point for the quiz game application."""
    welcome_message()
    user_choice = menu.show_main_menu(quiz.get_menu_options())

    print(user_choice)


if __name__ == "__main__":
    main()
