from flask import Flask, render_template, request, redirect, url_for, session
import subprocess
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Dummy user data for demonstration
users = {"user": "password"}

def run_streamlit():
    subprocess.run(["python", "run_app.py"])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('recommendation'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        else:
            return "User already exists. Please login."
    return render_template('signup.html')

@app.route('/recommendation')
def recommendation():
    if 'username' in session:
        return redirect("http://localhost:8501")
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    threading.Thread(target=run_streamlit).start()
    app.run(port=5000)
