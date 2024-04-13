from flask import Flask, render_template, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {'12': '12', '1': '1'}

jolly_messages = [
    "Here's to a fantastic day ahead, ~username~!",
    "Welcome ~username~ to the portal, login success! Have a blast today!",
    "Great to see you here, ~username~! Enjoy your time on the portal!"
]

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:

            jolly_message = random.choice(jolly_messages)

            return render_template('login_success.html', username=username, jolly_message=jolly_message)
        else:
            flash('Invalid username or password!', 'error')
    return render_template('login.html')

@app.route('/register-prompt')
def register_prompt():
    return render_template('register_prompt.html')

@app.route('/register', methods=['POST'])
def register():

    username = request.form['username']
    password = request.form['password']

    users[username] = password
    flash('Registration successful!', 'success')
    return redirect(url_for('login'))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/quiz1')
def quiz1():
    return render_template('quiz1.html')

@app.route('/quiz2')
def quiz2():
    return render_template('quiz2.html')

@app.route('/video')
def video():

    videos = [{'title': 'Video 1', 'url': 'https://www.youtube.com/embed/dQw4w9WgXcQ'}]
    return render_template('video.html', videos=videos)

@app.route('/course-selection')
def course_selection():

    courses = [{'title': 'Course 1', 'description': 'Description of Course 1'},
               {'title': 'Course 2', 'description': 'Description of Course 2'}]
    return render_template('course_selection.html', courses=courses)

@app.route('/documents')
def documents():
    return render_template('documents.html')
2
if __name__ == '__main__':
    app.run(debug=True)
