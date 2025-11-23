🎓 Student Management System — Django (Full Project)

A simple and clean Student Management System built using Django, supporting:
✔ Add Students
✔ Update Students
✔ Delete Students
✔ Search Students
✔ Bootstrap UI

📌 1. Clone the Repository
git clone https://github.com/mkshuklaaa/Student-Management-System.git
cd Student-Management-System

📌 2. Install Requirements

Make sure Python is installed.

Install Django (or all dependencies if you have requirements.txt):

pip install -r requirements.txt


OR (if Django only):

pip install django

📌 3. Apply Migrations
python manage.py makemigrations
python manage.py migrate

📌 4. Run the Server

Start Django development server:

python manage.py runserver

📌 5. Open the Application

After running the server, Django will open at:

http://127.0.0.1:8000/


Click the link or paste it into your browser to access the project.

📁 Project Structure (Summary)
student_project/
│
├── students/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
│       ├── home.html
│       ├── add.html
│       └── edit.html
│
├── student_project/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
