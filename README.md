# Django PostgreSQL Example

This repository provides a sample project demonstrating how to set up and use Django with a PostgreSQL database. The project is ideal for learning, experimenting, or as a starting point for your own Django applications.

## Features

- Django web framework integration
- PostgreSQL as the primary database backend
- PostgreSQL database hosted and configured on the [Neon](https://neon.tech/) platform
- Example settings and environment configuration for seamless local and cloud development
- This part is also has a notion page [Notion](https://www.notion.so/Django-Configure-Databases-25aab55ddcc980879160fb8e3db13d82)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- PostgreSQL (database hosted on Neon platform)
- `psycopg2` (PostgreSQL adapter for Python)

### Setting Up the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/abderrahim-dj/django-postgreSQL-example.git
   cd django-postgreSQL-example
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your database credentials provided by the Neon platform.

   ```
   DATABASE_NAME=your_database_name
   DATABASE_USER=your_database_user
   DATABASE_PASSWORD=your_database_password
   DATABASE_HOST=your_neon_host
   DATABASE_PORT=5432
   ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**

   Open your browser and navigate to [http://localhost:8000/](http://localhost:8000/).

## PostgreSQL on Neon

This project uses [Neon](https://neon.tech/) to host and manage the PostgreSQL database. Neon provides a fully managed, serverless PostgreSQL solution with easy setup and scaling. To create your Neon database:

- Sign up at [Neon](https://neon.tech/)
- Create a new project and a database
- Obtain your connection details and update your `.env` file as described above

## License

This project is licensed under the MIT License.

