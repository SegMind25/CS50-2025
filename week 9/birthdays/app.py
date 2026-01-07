import os
import sqlite3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('birthdays.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Basic validation
        if not name or not month or not day:
            return redirect("/")

        try:
            month = int(month)
            day = int(day)
            # Validate month (1-12) and day (1-31)
            if month < 1 or month > 12 or day < 1 or day > 31:
                return redirect("/")
        except ValueError:
            return redirect("/")

        # Insert into database
        conn = get_db_connection()
        conn.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
                     (name, month, day))
        conn.commit()
        conn.close()

        return redirect("/")

    else:
        # TODO: Display the entries in the database on index.html
        conn = get_db_connection()
        birthdays = conn.execute("SELECT * FROM birthdays").fetchall()
        conn.close()

        return render_template("index.html", birthdays=birthdays)
