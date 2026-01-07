# WWII Quick Facts Quiz

#### Video Demo: (https://youtu.be/6txXIju3Qg0?si=WL0lPrU2cayT2ghU)
#### Description:

The **WWII Quick Facts Quiz** is a terminal-based educational application developed in Python that challenges users with historically accurate multiple-choice questions about World War II. As the creator of a YouTube channel dedicated to WWII history, I designed this tool to offer an interactive, knowledge-reinforcing experience for students, educators, and history enthusiasts. Unlike passive video consumption, this quiz encourages active recall—a proven method for retaining historical facts—while remaining lightweight, portable, and easy to use on any system with Python installed.

This project directly applies core concepts from CS50, including **structured data storage with SQLite**, **user input validation**, **modular program design**, and **robust error handling**. It demonstrates how software can serve educational purposes without requiring complex infrastructure or internet connectivity, making it ideal for classrooms or offline learning environments.

### Technical Implementation

The application is built entirely in **Python 3** and relies only on the standard library and SQLite3 (which is included with Python). There are no external dependencies, ensuring broad compatibility across operating systems and development environments, including the CS50 Codespace.

At startup, the program connects to a local SQLite database file named `quiz.db`. This database contains a single table, `questions`, with the following schema:
- `id` (INTEGER PRIMARY KEY): Unique identifier for each question.
- `question` (TEXT): The question prompt (e.g., "What year did WWII begin?").
- `option_a`, `option_b`, `option_c`, `option_d` (TEXT): The four multiple-choice options.
- `correct_answer` (TEXT): A single character ('A', 'B', 'C', or 'D') indicating the correct choice.

The program fetches all available questions, randomly shuffles them to ensure varied gameplay across sessions, and presents 10 questions per quiz. After each response, the user receives immediate feedback: a green checkmark (✅) for correct answers or a red X (❌) with the correct answer and explanation for incorrect ones. At the end, the user sees their final score out of 10, along with a personalized message based on performance (e.g., “Perfect score!” or “Keep learning!”).

Input validation ensures that users can only submit answers in the format A, B, C, or D. Invalid inputs are rejected with a clear prompt, enhancing usability and preventing crashes.

### File Structure and Responsibilities

- **`quiz.py`**: The main executable script. It handles program flow, database interaction, user interaction, scoring logic, and output formatting. The code is organized into a single `main()` function for clarity and simplicity, following CS50’s emphasis on readable, well-structured code.
- **`quiz.db`**: A pre-populated SQLite database containing 20+ verified WWII questions. Questions cover major battles (e.g., Stalingrad, Midway), political leaders (Churchill, Roosevelt, Hitler), key technologies (radar, atomic bomb), and pivotal events (D-Day, Pearl Harbor). All facts were cross-referenced with authoritative historical sources such as the Imperial War Museum and the U.S. National Archives to ensure accuracy.

### Design Decisions and Trade-offs

I chose a **command-line interface (CLI)** over a web or graphical interface for several reasons:
1. **Simplicity**: A CLI avoids the complexity of web frameworks, CSS, or JavaScript, allowing me to focus on core programming logic.
2. **Portability**: The app runs anywhere Python runs—no browser or server needed.
3. **CS50 Alignment**: CLI programs are emphasized in early problem sets (e.g., `cash`, `readability`), making this a natural evolution of those skills.

I opted for **SQLite** instead of a flat file (like CSV) because it provides structured querying, data integrity, and scalability. Adding new questions in the future requires only an `INSERT` statement—no code changes.

While a web version could embed my YouTube videos directly (e.g., showing a clip after a question), I prioritized a **minimal, functional MVP** that meets the course’s scope for a solo project. However, this CLI app serves as a solid foundation for a future web expansion.

### Educational Impact and Personal Motivation

As a content creator focused on WWII history, I often hear from viewers who want to test their knowledge after watching my videos. This quiz bridges that gap—it transforms passive viewing into active learning. Teachers could use it as a warm-up activity; students could run it before exams. By open-sourcing the code and database, others can contribute questions in different languages or focus on specific theaters of war (e.g., Pacific, North Africa).

### How to Run

1. Clone or download this project folder.
2. Open a terminal in the project directory.
3. Run: `python quiz.py`
4. Follow the on-screen prompts to begin the quiz.

No installation or setup is required beyond Python 3.

### Future Enhancements

Potential improvements include:
- Adding categories (e.g., “Leaders”, “Weapons”, “Treaties”) for filtered quizzes.
- Implementing a high-score system using a second database table.
- Creating a Flask-based web version with embedded YouTube videos for deeper context.
- Supporting internationalization for non-English audiences.

This project embodies CS50’s spirit: using code to solve real problems, serve communities, and extend learning beyond the screen. It’s a small tool with a clear purpose—and one I hope will outlive this course by helping others engage more deeply with history.
