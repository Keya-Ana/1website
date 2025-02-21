from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Create SQLite database and table if they don't exist
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS submissions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  message TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Save data into the database
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO submissions (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    return "Thank you for your submission!"

if __name__ == '__main__':
    init_db()
    app.run( debug=True)
