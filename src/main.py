import menu
import quiz


def welcome_message() -> None:
    """Display a welcome message to the user."""
    print("Welcome to the CLI QUIZ MASTER!")
    print("Get ready to test your knowledge across various categories and difficulties.")


def main() -> None:
    """Main entry point for the quiz game application."""
    welcome_message()
    quiz_options = quiz.get_menu_options()  # Get the main menu options from the quiz module
    user_choice = menu.show_main_menu(quiz_options)

    if user_choice == quiz_options.index("Exit"):
        print("Thank you for playing! Goodbye!")

    print(user_choice)


if __name__ == "__main__":
    main()
