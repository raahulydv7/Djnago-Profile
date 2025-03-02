# Django User Profile System

## Introduction
This is a Django-based user profile system where users can create an account, log in, and upload their profile picture. Users can update their profile details including username, email, and password.

## Features
- User registration
- User login/logout
- Profile management (update username, email, profile picture)
- Password change functionality

## Technologies Used
- Django
- Bootstrap (for UI styling)
- SQLite (default database)
- Pillow (for image handling)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-profile-system.git
cd django-profile-system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```

### 6. Run the Server
```bash
python manage.py runserver
```

## Usage
1. Open the browser and go to `http://127.0.0.1:8000/register/` to create an account.
2. Log in at `http://127.0.0.1:8000/login/`.
3. Navigate to `http://127.0.0.1:8000/profile/` to update profile details and upload a profile picture.

## Folder Structure
```
|-- project_root/
    |-- manage.py
    |-- db.sqlite3
    |-- requirements.txt
    |-- myapp/
        |-- models.py  # UserProfile model
        |-- views.py  # Registration, login, profile views
        |-- forms.py  # Django forms for profile update
        |-- urls.py  # URL routing
        |-- templates/
            |-- register.html
            |-- login.html
            |-- profile.html
```

## Models
```python
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics/', default='default/default.jpg')

    def __str__(self):
        return self.user.username
```


