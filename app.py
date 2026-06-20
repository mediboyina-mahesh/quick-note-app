from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database table
conn = sqlite3.connect("notes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT
)
""")

conn.commit()
conn.close()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save-note', methods=['POST'])
def save_note():
    data = request.json
    note = data['note']

    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO notes(note) VALUES(?)",
        (note,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "saved"})


@app.route('/notes')
def get_notes():

    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT note FROM notes")

    notes = cursor.fetchall()

    conn.close()

    return jsonify(notes)


if __name__ == "__main__":
    app.run(debug=True)