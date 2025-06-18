# IFRI Comotorage Django Backend

This directory contains the Django backend for the IFRI Comotorage application.

## Setup (from parent directory `Projet-Eunice`)

1.  **Ensure you are in the `Projet-Eunice` directory.**

2.  **Activate virtual environment:**
    ```bash
    source venv/bin/activate
    ```

3.  **Navigate into this Django project directory:**
    ```bash
    cd ifri_comotorage
    ```

4.  **Install dependencies (if not already done from parent):**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure `core/settings.py`:**
    *   Update `DATABASES` with your PostgreSQL credentials.
    *   Ensure `SECRET_KEY` is set (preferably via environment variable).

6.  **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run tests:**
    ```bash
    pytest
    ```

9.  **Run the development server:**
    ```bash
    python manage.py runserver
    # Or for Channels (ASGI):
    # daphne -p 8000 core.asgi:application
    ```

Refer to the `README.md` in the parent `Projet-Eunice` directory for more comprehensive setup instructions including virtual environment creation and initial dependency installation.
