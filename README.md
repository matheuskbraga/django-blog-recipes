# Django Recipe Blog

A simple blog application for sharing and viewing recipes, built with Django.

## Features

*   View a list of recipes.
*   See the details of a specific recipe, including ingredients and instructions.
*   Admin interface to manage recipes (add, edit, delete).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.8+
*   Pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/django-blog-recipes.git
    cd django-blog-recipes
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    *(Note: A `requirements.txt` file is not yet present in the project. You should create one using `pip freeze > requirements.txt` after installing Django)*
    ```sh
    pip install Django
    ```

4.  **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```sh
    python manage.py createsuperuser
    ```
    Follow the prompts to create a username, email, and password.

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## Usage

*   Access the main site at `http://127.0.0.1:8000/` to see the recipe list.
*   Access the admin panel at `http://127.0.0.1:8000/admin/` to log in and manage recipes.

## Built With

*   [Django](https://www.djangoproject.com/) - The web framework used
*   [Python](https://www.python.org/) - The programming language

## License

This project is licensed under the terms of the LICENSE file.
