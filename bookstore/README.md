# Bookstore Management System

## Project Overview
This is a Bookstore Management System built with Django. It features user authentication, a custom admin panel for managing books, a user-facing book catalog, and a session-based shopping cart. The project uses Class-Based Views (CBV) exclusively and manual HTML forms with custom validation.

## Features
- User Registration, Login, and Logout
- Custom Admin Panel (Add/Edit/Delete Books)
- Book Listing and Details
- Add to Cart functionality using Django sessions
- No use of Django Admin or Django Forms

## Tech Stack
- Python 3.10
- Django 4.x
- SQLite (default database)
- Docker & Docker Compose
- Jenkins for CI/CD

## Setup & Run Instructions

### Prerequisites
- Docker and Docker Compose installed
- Jenkins installed for CI/CD (optional)

### Running with Docker
1. Build and start the containers:
   ```
   docker-compose up --build
   ```
2. The application will be available at `http://localhost:8000`

### Running Locally without Docker
1. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser (optional for admin access):
   ```
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```
6. Access the app at `http://localhost:8000`

## Docker Usage
- Dockerfile and docker-compose.yml are included for containerized deployment.
- The web service runs on port 8000.
- PostgreSQL is configured as the database in docker-compose.

## Jenkins Usage
- Jenkinsfile is included to automate build, test, and deploy stages.
- The pipeline sets up a Python environment, runs tests, builds a Docker image, and deploys using docker-compose.

## Screenshots
*(Add screenshots here if available)*

## Notes
- The project uses sessions to manage the shopping cart.
- All views are implemented as Class-Based Views.
- Manual HTML forms are used with custom validation logic.
