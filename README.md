# 🎓 Student Management System — Django (Full Project)

A simple and clean Student Management System built using Django, featuring:

✔ Add Students  
✔ Update Students  
✔ Delete Students  
✔ Search Students  
✔ Bootstrap UI  

------------------------------------------------------------

# 📌 1. Clone the Repository

git clone https://github.com/mkshuklaaaa/Student-Management-System.git
cd Student-Management-System

------------------------------------------------------------

# 📌 2. Install Requirements

# Make sure Python + pip are installed.

# Install all dependencies
pip install -r requirements.txt

# OR install Django manually
pip install django

------------------------------------------------------------

# 📌 3. Apply Migrations

python manage.py makemigrations
python manage.py migrate

------------------------------------------------------------

# 📌 4. Run the Server

python manage.py runserver

------------------------------------------------------------

# 📌 5. Open the Application

# After the server starts, open this link in your browser:
http://127.0.0.1:8000/

------------------------------------------------------------

# 📁 Project Structure

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
