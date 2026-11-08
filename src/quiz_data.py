"""
Data structures and constants for the quiz game.
"""

QUIZ_DATA = {
    "science": {
        "hard": [
            {
                "question": "What is the chemical symbol for gold?",
                "choices": ["Au", "Ag", "Gd", "Go"],
                "answer": 0,
            },
            {
                "question": "What is the speed of light in a vacuum?",
                "choices": ["3.00 x 10^8 m/s", "1.50 x 10^8 m/s", "3.00 x 10^6 m/s", "1.50 x 10^6 m/s"],
                "answer": 0,
            },
            {
                "question": "What is the powerhouse of the cell?",
                "choices": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
                "answer": 1,
            },
            {
                "question": "What is the chemical formula for water?",
                "choices": ["H2O", "CO2", "O2", "NaCl"],
                "answer": 0,
            },
            {
                "question": "What is the most abundant gas in Earth's atmosphere?",
                "choices": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
                "answer": 1,
            },
            {
                "question": "What is the unit of electrical resistance?",
                "choices": ["Ohm", "Volt", "Ampere", "Watt"],
                "answer": 0,
            },
            {
                "question": "What is the process by which plants make their own food?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
                "answer": 0,
            },
            {
                "question": "What is the chemical symbol for sodium?",
                "choices": ["Na", "S", "So", "N"],
                "answer": 0,
            },
        ],
        "normal": [
            {
                "question": "What is the boiling point of water at sea level?",
                "choices": ["100°C", "90°C", "80°C", "70°C"],
                "answer": 0,
                "hint": "It's a three-digit number in Celsius.",
            },
            {
                "question": "What is the chemical symbol for iron?",
                "choices": ["Fe", "Ir", "In", "I"],
                "answer": 0,
                "hint": "It's derived from the Latin word 'ferrum'.",
            },
            {
                "question": "What is the largest planet in our solar system?",
                "choices": ["Jupiter", "Saturn", "Earth", "Mars"],
                "answer": 0,
                "hint": "It's a gas giant with a prominent red spot.",
            },
            {
                "question": "What is the chemical symbol for oxygen?",
                "choices": ["O", "Ox", "O2", "O3"],
                "answer": 0,
                "hint": "It's a single letter symbol.",
            },
            {
                "question": "What is the process by which plants convert sunlight into energy?",
                "choices": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
                "answer": 0,
                "hint": "It starts with 'Photo'.",
            },
            {
                "question": "What is the chemical symbol for hydrogen?",
                "choices": ["H", "Hy", "Hd", "Hg"],
                "answer": 0,
                "hint": "It's the first letter of the alphabet.",
            },
            {
                "question": "What is the unit of force in the metric system?",
                "choices": ["Newton", "Joule", "Watt", "Pascal"],
                "answer": 0,
                "hint": "It's named after a famous scientist.",
            },
            {
                "question": "What is the chemical symbol for carbon?",
                "choices": ["C", "Ca", "Co", "Cr"],
                "answer": 0,
                "hint": "It's a single letter symbol.",
            },
        ],
    },
    "history": {
        "hard": [
            {
                "question": "Who was the first emperor of China?",
                "choices": ["Qin Shi Huang", "Han Wudi", "Tang Taizong", "Ming Hongwu"],
                "answer": 0,
            },
            {
                "question": "In which year did the Berlin Wall fall?",
                "choices": ["1987", "1989", "1991", "1993"],
                "answer": 1,
            },
            {
                "question": "Who was the British Prime Minister during World War II?",
                "choices": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Anthony Eden"],
                "answer": 0,
            },
            {
                "question": "What was the name of the ship that carried the Pilgrims to America in 1620?",
                "choices": ["Mayflower", "Santa Maria", "Endeavour", "Beagle"],
                "answer": 0,
            },
            {
                "question": "Who was the first President of the United States?",
                "choices": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                "answer": 0,
            },
            {
                "question": "In which year did World War II end?",
                "choices": ["1943", "1944", "1945", "1946"],
                "answer": 2,
            },
            {
                "question": "Who was the first man to step on the moon?",
                "choices": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
                "answer": 0,
            },
            {
                "question": "What was the name of the ship that sank in 1912 after hitting an iceberg?",
                "choices": ["Titanic", "Lusitania", "Britannic", "Olympic"],
                "answer": 0,
            },
        ],
        "normal": [
            {
                "question": "Who was the first President of the United States?",
                "choices": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
                "answer": 0,
                "hint": "He is often called the 'Father of His Country'.",
            },
            {
                "question": "In which year did World War II end?",
                "choices": ["1943", "1944", "1945", "1946"],
                "answer": 2,
                "hint": "It ended in the mid-1940s.",
            },
            {
                "question": "Who was the first man to step on the moon?",
                "choices": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
                "answer": 0,
                "hint": "He famously said, 'That's one small step for man, one giant leap for mankind.'",
            },
            {
                "question": "What was the name of the ship that sank in 1912 after hitting an iceberg?",
                "choices": ["Titanic", "Lusitania", "Britannic", "Olympic"],
                "answer": 0,
                "hint": "It was a British passenger liner and is one of the most famous shipwrecks in history.",
            },
            {
                "question": "In which year did the Berlin Wall fall?",
                "choices": ["1987", "1989", "1991", "1993"],
                "answer": 1,
                "hint": "It happened in the late 1980s, marking the end of the Cold War.",
            },
            {
                "question": "Who was the British Prime Minister during World War II?",
                "choices": ["Winston Churchill", "Neville Chamberlain", "Clement Attlee", "Anthony Eden"],
                "answer": 0,
                "hint": "He is famous for his speeches and leadership during the war.",
            },
            {
                "question": "What was the name of the ship that carried the Pilgrims to America in 1620?",
                "choices": ["Mayflower", "Santa Maria", "Endeavour", "Beagle"],
                "answer": 0,
                "hint": "It is a famous ship in American history, associated with Thanksgiving.",
            },
            {
                "question": "Which ancient wonder was located in Giza, Egypt?",
                "choices": ["Great Pyramid of Giza", "Hanging Gardens of Babylon", "Statue of Zeus at Olympia", "Temple of Artemis at Ephesus"],
                "answer": 0,
                "hint": "It is the only one of the Seven Wonders of the Ancient World that still exists today.",
            },
        ],
    },
    "algebra": {
        "hard": [
            {
                "question": "Solve for x: log_2(x) + log_2(x - 2) = 3",
                "choices": ["x = 4", "x = -2", "x = 4 and x = -2", "x = 8"],
                "answer": 0,
            },
            {
                "question": "If 3^(2x + 1) - 10 * 3^x + 3 = 0, what are the real solutions for x?",
                "choices": ["x = 0 and x = 2", "x = -1 and x = 1", "x = 1 and x = 3", "x = -1 and x = 0"],
                "answer": 1,
            },
            {
                "question": "Find all real solutions to |2x - 5| = x + 1.",
                "choices": ["x = 6", "x = 4/3", "x = 6 and x = 4/3", "x = 2 and x = 6"],
                "answer": 2,
            },
            {
                "question": "What is the sum of the roots of the quadratic equation 3x^2 - 12x + 5 = 0?",
                "choices": ["-4", "4", "5/3", "-5/3"],
                "answer": 1,
            },
            {
                "question": "Solve the system: 2x + 3y = 7 and 4x + 6y = 14.",
                "choices": ["x = 2, y = 1", "No solution", "Infinitely many solutions", "x = 1, y = 2"],
                "answer": 2,
            },
            {
                "question": "What is the solution set for the inequality (x - 3)/(x + 2) <= 0?",
                "choices": ["(-2, 3]", "[-2, 3]", "(-inf, -2) U [3, inf)", "(-2, 3)"],
                "answer": 0,
            },
            {
                "question": "Find the remainder when P(x) = 2x^3 - 5x^2 + 4x - 7 is divided by (x - 2).",
                "choices": ["-3", "-7", "1", "-1"],
                "answer": 0,
            },
            {
                "question": "For what value of k will the equation x^2 - 6x + k = 0 have exactly one real solution?",
                "choices": ["k = 3", "k = -9", "k = 9", "k = 36"],
                "answer": 2,
            },
        ],
        "normal": [
            {
                "question": "Solve for x: 3x - 4 = 11.",
                "choices": ["x = 3", "x = 4", "x = 5", "x = 6"],
                "answer": 2,
                "hint": "Add 4 to both sides, then divide by 3.",
            },
            {
                "question": "What is the value of x if 4(x + 2) = 24?",
                "choices": ["x = 2", "x = 4", "x = 6", "x = 8"],
                "answer": 1,
                "hint": "Divide both sides by 4 first, then subtract 2.",
            },
            {
                "question": "Solve for x: x^2 - 9 = 0.",
                "choices": ["x = 3", "x = -3", "x = 3 and x = -3", "x = 9 and x = -9"],
                "answer": 2,
                "hint": "Factor this as a difference of squares: (x - 3)(x + 3) = 0.",
            },
            {
                "question": "What is the slope of the line given by y = -2x + 5?",
                "choices": ["5", "-2", "2", "-5"],
                "answer": 1,
                "hint": "Recall the slope-intercept form y = mx + b, where m is the slope.",
            },
            {
                "question": "Solve for x: 5x + 3 = 2x + 12.",
                "choices": ["x = 3", "x = 5", "x = 4", "x = 2"],
                "answer": 0,
                "hint": "Subtract 2x from both sides, then subtract 3 from both sides.",
            },
            {
                "question": "Evaluate the expression 2a^2 - 3b when a = 3 and b = 2.",
                "choices": ["12", "18", "6", "15"],
                "answer": 0,
                "hint": "Square 3 first (3^2 = 9), multiply by 2, then subtract 3 * 2.",
            },
            {
                "question": "Solve for y: y/4 + 6 = 10.",
                "choices": ["y = 12", "y = 16", "y = 4", "y = 24"],
                "answer": 1,
                "hint": "Subtract 6 from both sides to get y/4 = 4, then multiply by 4.",
            },
            {
                "question": "Which of the following is equivalent to 2(3x - 5) + 4x?",
                "choices": ["10x - 10", "10x - 5", "7x - 10", "6x - 1"],
                "answer": 0,
                "hint": "Distribute 2 into (3x - 5) to get 6x - 10, then combine like terms.",
            },
        ],
    },
    "sports": {
        "hard": [
            {
                "question": "Who is the only player in Major League Baseball history to hit two grand slams in a single inning?",
                "choices": ["Alex Rodriguez", "Fernando Tatís", "Lou Gehrig", "Albert Pujols"],
                "answer": 1,
            },
            {
                "question": "Which NFL team completed the only undefeated season and Super Bowl victory in league history?",
                "choices": ["1972 Miami Dolphins", "1985 Chicago Bears", "2007 New England Patriots", "1976 Oakland Raiders"],
                "answer": 0,
            },
            {
                "question": "Which MLB player holds the single-season record for the most RBIs (191 in 1930)?",
                "choices": ["Babe Ruth", "Hank Aaron", "Lou Gehrig", "Hack Wilson"],
                "answer": 3,
            },
            {
                "question": "Who holds the NFL record for the most career sacks with 200?",
                "choices": ["Reggie White", "Bruce Smith", "Lawrence Taylor", "Kevin Greene"],
                "answer": 1,
            },
            {
                "question": "Who was the first boxer to win world titles in five different weight classes?",
                "choices": ["Sugar Ray Leonard", "Thomas Hearns", "Manny Pacquiao", "Roberto Durán"],
                "answer": 1,
            },
            {
                "question": "Which NBA player holds the record for the most assists in a single regular season (1,164)?",
                "choices": ["Magic Johnson", "John Stockton", "Chris Paul", "Steve Nash"],
                "answer": 1,
            },
            {
                "question": "What is the only country to have participated in every FIFA World Cup tournament?",
                "choices": ["Germany", "Argentina", "Italy", "Brazil"],
                "answer": 3,
            },
            {
                "question": "Who was the first WNBA player to win both Rookie of the Year and MVP in the same season?",
                "choices": ["Lisa Leslie", "Diana Taurasi", "Candace Parker", "Maya Moore"],
                "answer": 2,
            },
        ],
        "normal": [
            {
                "question": "In American football, how many points is a touchdown worth before the extra point or two-point attempt?",
                "choices": ["3 points", "6 points", "7 points", "4 points"],
                "answer": 1,
                "hint": "A standard field goal is 3 points; a touchdown awards double that base value.",
            },
            {
                "question": "How many holes are played in a standard, full round of golf?",
                "choices": ["9", "12", "18", "21"],
                "answer": 2,
                "hint": "A full round is twice the length of a standard 9-hole executive course.",
            },
            {
                "question": "What is the term for rolling three strikes in a row in ten-pin bowling?",
                "choices": ["Spare", "Turkey", "Triple", "Eagle"],
                "answer": 1,
                "hint": "This bowling term shares its name with a bird commonly eaten on Thanksgiving.",
            },
            {
                "question": "How many players from one team are on the basketball court at the same time during active play?",
                "choices": ["4", "5", "6", "7"],
                "answer": 1,
                "hint": "Standard team lineups feature two guards, two forwards, and one center.",
            },
            {
                "question": "Which Grand Slam tennis tournament is played exclusively on outdoor red clay courts?",
                "choices": ["Wimbledon", "US Open", "Australian Open", "The French Open (Roland-Garros)"],
                "answer": 3,
                "hint": "This major takes place in Paris and is also known as Roland-Garros.",
            },
            {
                "question": "In baseball, how many strikes result in a strikeout for the batter?",
                "choices": ["2", "3", "4", "5"],
                "answer": 1,
                "hint": "Think of the famous lyric from 'Take Me Out to the Ball Game'.",
            },
            {
                "question": "Which swimmer holds the record for the most Olympic gold medals won of all time (23)?",
                "choices": ["Mark Spitz", "Ian Thorpe", "Michael Phelps", "Ryan Lochte"],
                "answer": 2,
                "hint": "This American swimmer dominated butterfly, individual medley, and freestyle events from 2004 to 2016.",
            },
            {
                "question": "How many players are on the field for one team during a regulation soccer match?",
                "choices": ["9", "10", "11", "12"],
                "answer": 2,
                "hint": "This total includes ten outfield players and one goalkeeper.",
            },
        ],
    },
}

# Retro-Arcade Palette
GOLD = "\033[1;93m"
GREEN = "\033[1;92m"
CYAN = "\033[1;96m"
WHITE = "\033[1;97m"
DIM = "\033[2;37m"
RESET = "\033[0m"

QUIZ_RULES: str = f"""\n\n
        {GOLD}★ ★ ★  {GREEN}HOW TO PLAY : RULES & DIRECTIVES{GOLD}  ★ ★ ★{RESET}

  {CYAN}[1] SELECTION{RESET}
      {WHITE}• Pick a challenge category and difficulty mode to begin.{RESET}

  {CYAN}[2] DIFFICULTY MODES{RESET}
      {WHITE}• {GREEN}Easy{WHITE}   : Standard questions with helpful tactical hints.{RESET}
      {WHITE}• {GOLD}Normal{WHITE} : Standard questions without hints.{RESET}
      {WHITE}• {CYAN}Hard{WHITE}   : Advanced questions designed to test your limits.{RESET}

  {CYAN}[3] SCORING{RESET}
      {WHITE}• Enter the matching number (1-4) for each prompt.{RESET}
      {WHITE}• Correct answers yield points; wrong guesses carry no penalty.{RESET}

  {CYAN}[4] LEADERBOARD & ALIASES{RESET}
      {WHITE}• Submit an {GOLD}alias or username{WHITE} after the run to log your score.{RESET}
      {WHITE}• Handles must be unique across the board—no duplicates allowed.{RESET}
      {DIM}• Leave the alias blank at the end if you prefer not to register.{RESET}
"""
