Flask To-Do App

A simple to-do list web app built with Flask and SQLite. You log in, add tasks, and move each task through three stages: Pending → Working → Done.

Features
Login and logout (session based)
Add new tasks
Change task status: Pending → Working → Done (then back to Pending)
Clear all tasks
Flash messages for success and error feedback
Pages are protected: you must be logged in to see tasks
Tech Stack
Python 3
Flask
Flask-SQLAlchemy (SQLite database)
HTML, CSS, Jinja2 templates
Project Structure
todo_app/
├── run.py                  # starts the app
├── requirements.txt        # packages needed
├── app/
│   ├── __init__.py         # creates the app, sets config, registers routes
│   ├── models.py           # Task database model
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py         # login and logout
│   │   └── tasks.py        # add, toggle, clear tasks
│   ├── templates/
│   │   ├── base.html       # shared layout (header, flash messages, footer)
│   │   ├── login.html
│   │   └── tasks.html
│   └── static/
│       └── css/
│           └── style.css
How to Run
1. Clone the project
bash
git clone https://github.com/YOUR-USERNAME/todo_app.git
cd todo_app
2. Make a virtual environment

Windows (PowerShell):

powershell
py -m venv venv
.\venv\Scripts\Activate.ps1

Mac / Linux:

bash
python3 -m venv venv
source venv/bin/activate
3. Install packages
bash
pip install -r requirements.txt
4. Start the app
bash
python run.py

Open http://127.0.0.1:5000 in your browser.

Demo Login
Username	Password
admin	admin123

The login is hard-coded for learning. For a real app, store users in the database with hashed passwords.

How It Works
run.py creates the app and the database tables, then starts the server.
Tasks are saved in a SQLite file (instance/todo.db), created automatically on first run.
Each task has a title and a status (pending, working, done).
Clicking Next on a task moves it to the next status.
Ideas for Later
Register page with real users in the database
Hashed passwords (werkzeug.security)
Delete or edit a single task
Move the secret key into an environment variable
Deploy online (Render, Railway, PythonAnywhere)
Notes

If you change a column in models.py, delete instance/todo.db and run again so the database is rebuilt.
