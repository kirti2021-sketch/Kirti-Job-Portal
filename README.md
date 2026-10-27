# Job Portal Website

## Project Overview

The Job Portal Website is a web-based application developed using Django. It helps users explore job opportunities and apply for jobs through a simple interface.

## Features

* User Registration and Login
* View Available Jobs
* View Job Details
* Apply for Jobs
* User Dashboard
* About Page
* Contact Page

## Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python, Django
* **Database:** SQLite
* **Tools:** Visual Studio Code, Git, GitHub

## Project Structure

```text
jobporta/
├── manage.py
├── jobporta/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── jobs/
    ├── migrations/
    ├── templates/
    ├── models.py
    ├── views.py
    └── urls.py
```

## How to Run the Project

1. Install Python on your computer.

2. Open the project folder in the terminal.

3. Install Django:

   ```bash
   pip install django
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open this address in your browser:

   `http://127.0.0.1:8000/`

## Project Purpose

This project was developed for learning web development and understanding frontend and backend integration using Django.
