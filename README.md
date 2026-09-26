# Math Quiz Game (Python CLI Project)

A simple command-line quiz application built in Python that tests the user's
arithmetic skills across four topics: **Addition, Subtraction, Multiplication,
and Division**. This project was built as part of the Python Essentials
evaluated course project (VITyarthi).

## Overview

When the program runs, it asks the user for their name and then lets them
choose one of four math topics. Based on the topic selected, the program
presents 5 multiple-choice questions (a/b/c/d). For each question, the user's
answer is checked against the correct option, immediate feedback
("correct answer" / "wrong answer" / "invalid answer") is shown, and a final
score out of 5 is displayed at the end.

## Features

- Personalized welcome using the user's name
- Menu-driven topic selection (Addition / Subtraction / Multiplication / Division)
- 5 multiple-choice questions per topic, each with 4 options (a, b, c, d)
- Instant feedback after every answer
- Automatic score calculation and final result out of 5
- Handles unrecognized answer choices with an "invalid answer" message

## Technologies / Tools Used

- **Language:** Python 3
- **Concepts used:** `input()`/`output`, conditionals (`if`/`elif`/`else`),
  type casting (`int()`, `str()`), variables, basic scoring logic
- **Environment:** Runs from any terminal with Python 3 installed
- **Version Control:** Git & GitHub

## Project Structure

```
math-quiz-project/
│
├── main.py            # Complete quiz program (entry point)
├── README.md           # Project documentation (this file)
├── statement.md         # Problem statement, scope, and target users
└── screenshots/          # Screenshots of the program running
```

## How to Install & Run

### Prerequisites
- Python 3.7 or above installed on your system
  (check with `python --version` or `python3 --version`)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/arsh26bce11502/math-quiz-project.git
   cd math-quiz-project
   ```

2. **Run the program**
   ```bash
   python main.py
   ```
   (On some systems, use `python3 main.py` instead)

3. **Follow the on-screen prompts**
   - Enter your name when asked
   - Enter a number from 1-4 to choose a topic
   - Answer each question by typing `a`, `b`, `c`, or `d`
   - View your final score at the end

No external libraries or installation steps are required — the project uses
only Python's built-in `input()`/`print()` functions.

## Instructions for Testing

To manually test the program:

1. Run `python main.py`
2. Test each of the 4 menu options (1, 2, 3, 4) in separate runs to confirm
   all four topics (addition, subtraction, multiplication, division) work
   correctly.
3. For each topic, test:
   - Entering the **correct** option for a question → should print
     `correct answer`
   - Entering an **incorrect** option (one of the other 3 letters) →
     should print `wrong answer`
   - Entering something outside a/b/c/d (e.g. `x`) → should print
     `invalid answer`
4. Confirm that the final score displayed matches the number of questions
   answered correctly.

## Screenshots

_See the `screenshots/` folder for sample runs of the program (topic
selection, a question being answered, and the final score screen)._

## Author

Built by Arsh Gupta (Reg. No. 26BCE11502), 1st Year, VIT Bhopal — as part of
the Python Essentials evaluated course project.
