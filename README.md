# IFRI Comotorage Backend

Backend for the IFRI Comotorage ride-sharing application.

## Project Structure

```
ifri_comotorage/      <-- Root Django project directory (contains manage.py)
├── core/             <-- Django project configuration (settings.py, urls.py)
├── users/            <-- User management app
├── rides/            <-- Ride management app
├── messaging/        <-- Messaging app (including WebSockets)
├── utils/            <-- Utility functions (matching algorithm, validations)
├── templates/        <-- HTML templates (if needed for backend testing)
├── static/           <-- Static files (CSS, JS, images - if served by Django)
└── manage.py
requirements.txt      <-- Python dependencies
README.md             <-- This file
.gitignore            <-- Specifies intentionally untracked files that Git should ignore
venv/                 <-- Virtual environment directory (if created here)
```

## Setup

1.  **Clone the repository (if applicable) or ensure you have the project files.**

2.  **Navigate to the project's root directory (where this README is located):**
    ```bash
    cd /path/to/Projet-Eunice
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure the database:**
    *   Ensure PostgreSQL is installed and running.
    *   Create a PostgreSQL database (e.g., `ifri_comotorage_db`).
    *   Create a PostgreSQL user with a password.
    *   Grant privileges to this user on the created database.
    *   Update the `DATABASES` setting in `ifri_comotorage/core/settings.py` with your database name, user, password, host, and port.

6.  **Set up environment variables (recommended for sensitive data):**
    *   Create a `.env` file in the `ifri_comotorage` directory (alongside `manage.py`).
    *   Add your `SECRET_KEY` and database credentials to this file. Example:
        ```env
        DJANGO_SECRET_KEY='your_very_secret_django_key_here'
        DB_NAME='ifri_comotorage_db'
        DB_USER='your_db_user'
        DB_PASSWORD='your_db_password'
        DB_HOST='localhost'
        DB_PORT='5432'
        DJANGO_DEBUG='True'
        ```
    *   The `core/settings.py` is set up to read these (you might need `python-dotenv` package if you want to load it automatically, or set them in your shell environment).

7.  **Navigate into the Django project directory:**
    ```bash
    cd ifri_comotorage
    ```

8.  **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9.  **Create a superuser (for admin panel access):**
    ```bash
    python manage.py createsuperuser
    ```

10. **Run tests:**
    ```bash
    pytest
    ```
    (Ensure you are in the `ifri_comotorage` directory where `manage.py` is located, or configure pytest to find it.)

11. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

The API will be accessible at `http://127.0.0.1:8000/`.
WebSocket endpoints for messaging will also be available (e.g., `ws://127.0.0.1:8000/ws/chat/<conversation_id>/`).

## API Endpoints Overview

(This section would be populated with details of major API endpoints once defined, e.g., user registration, login, ride creation, etc.)

*   **Users:** `/api/users/`
*   **Rides:** `/api/rides/`
*   **Messaging:** `/api/messaging/`

Refer to the `urls.py` files in each app for detailed routes.
