ATS Resume Analyzer

A Django-based ATS Resume Analyzer that extracts skills from resumes and generates an ATS score to help students optimize their resumes according to modern recruitment standards.

Overview

The ATS Resume Analyzer is a web-based application developed using Django. It allows users to upload resumes, extract relevant skills, and generate an ATS (Applicant Tracking System) score. The application helps students evaluate and improve their resumes to enhance their chances of passing automated recruitment screening systems.

Features

* Resume upload and analysis
* Skill extraction from resumes
* ATS score generation
* User-friendly interface
* Automated resume evaluation
* Recruitment-focused feedback

Technologies Used

* Python
* Django
* HTML
* CSS
* JavaScript
* SQLite (Development Database)

Installation

Install Dependencies:

pip install PyPDF2

Configuration

The settings.py file is not included in this repository.

Create a Django settings file and configure:

* SECRET_KEY
* DEBUG
* ALLOWED_HOSTS
* DATABASES
* INSTALLED_APPS
* MIDDLEWARE
* STATIC settings
* MEDIA settings

Database Setup

Apply migrations:

python manage.py migrate

Create an admin account:

python manage.py createsuperuser

Running the Application

Start the development server:

python manage.py runserver
Run locally.

Files Excluded from Repository

* venv/
* .env
* db.sqlite3
* db_new_backup.sqlite3
* pycache/
* *.pyc
* settings.py

Future Enhancements

* Resume keyword matching
* Job description comparison
* PDF report generation
