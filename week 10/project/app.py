"""
WWII Quick Facts Quiz
Final Project for CS50x
Author: Mario
GitHub: [your-username]
edX: [your-edx-username]
City/Country: [Your City, Country]
Date: October 24, 2025

This command-line quiz tests the user's knowledge of World War II.
Built with Python and SQLite. Inspired by historical education and
my passion for WWII history content on YouTube.
"""

import sqlite3
import random
import sys

def main():
    print("\n🌍 Welcome to the WWII Quick Facts Quiz!")
    print("Test your knowledge of history. Each question has 4 choices.\n")

    # Connect to database
    try:
        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
    except sqlite3.Error as e:
        sys.exit(f"Database error: {e}")

    # Fetch all questions
    cursor.execute("SELECT id, question, option_a, option_b, option_c, option_d, correct_answer FROM questions")
    questions = cursor.fetchall()
    conn.close()

    if not questions:
        sys.exit("No questions found in the database!")

    # Shuffle questions for variety
    random.shuffle(questions)
    score = 0

    # Ask up to 10 questions
    for i, q in enumerate(questions[:10], 1):
        q_id, question, a, b, c, d, correct = q
        print(f"\n--- Question {i}/10 ---")
        print(question)
        print(f"A) {a}")
        print(f"B) {b}")
        print(f"C) {c}")
        print(f"D) {d}")

        while True:
            user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Please enter A, B, C, or D.")

        if user_answer == correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was: {correct}) {locals()[correct.lower()]}")

    # Final score
    print(f"\n🎉 Quiz complete! You scored {score}/10.")
    if score == 10:
        print("🎖️  Perfect score! You're a WWII expert!")
    elif score >= 7:
        print("📚 Great job! You know your history well.")
    else:
        print("📖 Keep learning—history is full of lessons!")

    print("\n💡 Thanks For Playing This Game :) ")

if __name__ == "__main__":
    main()
