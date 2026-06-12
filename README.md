# StrategyPlus

# Running StrategyPlus Locally

## Prerequisites

Please ensure the following are installed:

* Python 3.10 or newer
* Git
* A terminal (Command Prompt, PowerShell, or Terminal)

## 1. Clone the Repository

```bash
git clone <repository-url>
cd StrategyPlus
```

## 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Apply Database Migrations

```bash
python manage.py migrate
```

## 5. Create an Admin User (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username and password.

## 6. Run the Development Server

```bash
python manage.py runserver
```

You should see output similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

## 7. Open the Application

Open a web browser and navigate to:

```text
http://127.0.0.1:8000/
```

## Admin Interface

If a superuser account was created, the Django admin interface can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

using the credentials created during the `createsuperuser` step.

## Current Features

The current build supports:

* User authentication
* Organisation creation
* Organisation deletion
* Project creation
* Project listing
* Project detail pages
* Data management through the Django admin panel

