from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Connect to the SQLite database
conn = sqlite3.connect('contact_messages.db')
cursor = conn.cursor()

# Create the necessary tables in the SQLite database
cursor.execute('''CREATE TABLE IF NOT EXISTS contact_messages
                 (name TEXT, email TEXT, number TEXT, message TEXT)''')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        message = request.form['msg']

        cursor.execute("INSERT INTO contact_messages (name, email, number, message) VALUES (?, ?, ?, ?)",
                       (name, email, number, message))
        conn.commit()

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)