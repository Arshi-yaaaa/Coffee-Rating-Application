from flask import Flask, render_template, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "coffee-rating-local-demo"
DATABASE = Path(__file__).with_name("coffee_votes.db")

COFFEES = [
    ("Ethiopian Yirgacheffe", "Floral aroma with bright citrus notes", "☕"),
    ("Sumatra Mandheling", "Rich, earthy flavour with a smooth finish", "🫘"),
    ("Cold Brew Nitro", "Smooth, chilled coffee with a creamy texture", "🧊"),
    ("Vanilla Latte", "Espresso blended with milk and vanilla", "🥛"),
    ("Mexican Chiapas", "Balanced coffee with chocolate notes", "☕"),
    ("Classic Cappuccino", "Espresso topped with steamed milk foam", "🍵"),
    ("Caramel Macchiato", "Espresso with milk and caramel flavour", "🍮"),
]

def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS coffees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL,
                icon TEXT NOT NULL,
                votes INTEGER NOT NULL DEFAULT 0
            )
        """)
        for name, description, icon in COFFEES:
            connection.execute(
                "INSERT OR IGNORE INTO coffees (name, description, icon) VALUES (?, ?, ?)",
                (name, description, icon)
            )

@app.route("/")
def index():
    with get_connection() as connection:
        coffees = connection.execute(
            "SELECT id, name, description, icon, votes FROM coffees ORDER BY id"
        ).fetchall()
    total_votes = sum(coffee["votes"] for coffee in coffees)
    return render_template("index.html", coffees=coffees, total_votes=total_votes)

@app.route("/vote/<int:coffee_id>", methods=["POST"])
def vote(coffee_id):
    with get_connection() as connection:
        result = connection.execute(
            "UPDATE coffees SET votes = votes + 1 WHERE id = ?",
            (coffee_id,)
        )
        if result.rowcount == 0:
            flash("That coffee item could not be found.", "error")
        else:
            flash("Thanks! Your vote has been recorded.", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
