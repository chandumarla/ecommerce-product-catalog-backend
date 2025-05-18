# ecommerce-product-catalog-backend
A Django REST API for managing and browsing products, with role-based admin access. Supports product listing, detail view, admin-only add/delete, and category-based filtering.

# Deploying to Render

Follow these steps to deploy this Django project to [Render](https://render.com/).

---

## 1. Prerequisites

- [Render account](https://dashboard.render.com/register)
- [Git](https://git-scm.com/) installed
- Project code pushed to [GitHub](https://github.com/) (Render deploys from GitHub)

---

## 2. Prepare the Project

1. **Install required packages:**
    ```
    pip install gunicorn psycopg2-binary dj-database-url whitenoise
    ```

2. **Freeze requirements:**
    ```
    pip freeze > requirements.txt
    ```

3. **Create a `Procfile` in the project root:**
    ```
    web: gunicorn ecommerce.wsgi
    ```

---

## 3. Update Django Settings

- In `ecommerce/settings.py`:
    - Import at the top:
        ```python
        import os
        import dj_database_url
        ```
    - Replace the `DATABASES` setting:
        ```python
        DATABASES = {
            'default': dj_database_url.config(
                default=os.environ.get('DATABASE_URL')
            )
        }
        ```
    - Add static files settings:
        ```python
        STATIC_ROOT = BASE_DIR / 'staticfiles'
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
        # Add WhiteNoise middleware after SecurityMiddleware
        # Example:
        # MIDDLEWARE = [
        #     'django.middleware.security.SecurityMiddleware',
        #     'whitenoise.middleware.WhiteNoiseMiddleware',
        #     ...
        # ]
        ```
    - Set allowed hosts:
        ```python
        ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
        ```
    - Set debug mode:
        ```python
        DEBUG = os.environ.get('DEBUG', 'False') == 'True'
        ```

---

## 4. Push to GitHub

If not already a git repo:
```
git init
git add .
git commit -m "Prepare project for Render deployment"
git remote add origin <your-github-repo-url>
git push -u origin main
```

---

## 5. Deploy on Render

1. **Create a new Web Service** on [Render](https://dashboard.render.com/):
    - Connect your GitHub repo.
    - Set the **Build Command** to:
        ```
        pip install -r requirements.txt
        ```
    - Set the **Start Command** to:
        ```
        gunicorn ecommerce.wsgi
        ```
    - Add environment variables:
        - `SECRET_KEY` (your Django secret key)
        - `DEBUG` (set to `False`)
        - `DATABASE_URL` (if using a custom database; Render auto-sets this if you add a PostgreSQL database)

2. **Add a PostgreSQL database** (optional but recommended):
    - Create a new PostgreSQL database in Render.
    - Render will provide a `DATABASE_URL`—add it to your web service's environment variables if not set automatically.

---

## 6. Run Migrations and Create Superuser

After your service is built and deployed:
- Go to your service in the Render dashboard.
- Open the **Shell** tab.
- Run:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic --noinput
    ```

---

## 7. Update CORS and CSRF Settings

After deploying your frontend, add its URL to `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` in `settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8001",
    "https://your-frontend-app.onrender.com",  # or your actual frontend URL
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8001",
    "https://your-frontend-app.onrender.com",
]
```
Then commit and push changes to GitHub; Render will redeploy automatically.

---

## 8. Open Your App

Visit the URL provided by Render (e.g., `https://your-backend-app.onrender.com/`).

---

**Done! Your Django app is now live on Render.**

# Deploying to Render

Follow these steps to deploy this Django project to [Render](https://render.com/).

---

## 1. Prerequisites

- [Render account](https://dashboard.render.com/register)
- [Git](https://git-scm.com/) installed
- Project code pushed to [GitHub](https://github.com/) (Render deploys from GitHub)

---

## 2. Prepare the Project

1. **Install required packages:**
    ```
    pip install gunicorn psycopg2-binary dj-database-url whitenoise
    ```

2. **Freeze requirements:**
    ```
    pip freeze > requirements.txt
    ```

3. **Create a `Procfile` in the project root:**
    ```
    web: gunicorn ecommerce.wsgi
    ```

---

## 3. Update Django Settings

- In `ecommerce/settings.py`:
    - Import at the top:
        ```python
        import os
        import dj_database_url
        ```
    - Replace the `DATABASES` setting:
        ```python
        DATABASES = {
            'default': dj_database_url.config(
                default=os.environ.get('DATABASE_URL')
            )
        }
        ```
    - Add static files settings:
        ```python
        STATIC_ROOT = BASE_DIR / 'staticfiles'
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
        # Add WhiteNoise middleware after SecurityMiddleware
        # Example:
        # MIDDLEWARE = [
        #     'django.middleware.security.SecurityMiddleware',
        #     'whitenoise.middleware.WhiteNoiseMiddleware',
        #     ...
        # ]
        ```
    - Set allowed hosts:
        ```python
        ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
        ```
    - Set debug mode:
        ```python
        DEBUG = os.environ.get('DEBUG', 'False') == 'True'
        ```

---

## 4. Push to GitHub

If not already a git repo:
```
git init
git add .
git commit -m "Prepare project for Render deployment"
git remote add origin <your-github-repo-url>
git push -u origin main
```

---

## 5. Deploy on Render

1. **Create a new Web Service** on [Render](https://dashboard.render.com/):
    - Connect your GitHub repo.
    - Set the **Build Command** to:
        ```
        pip install -r requirements.txt
        ```
    - Set the **Start Command** to:
        ```
        gunicorn ecommerce.wsgi
        ```
    - Add environment variables:
        - `SECRET_KEY` (your Django secret key)
        - `DEBUG` (set to `False`)
        - `DATABASE_URL` (if using a custom database; Render auto-sets this if you add a PostgreSQL database)

2. **Add a PostgreSQL database** (optional but recommended):
    - Create a new PostgreSQL database in Render.
    - Render will provide a `DATABASE_URL`—add it to your web service's environment variables if not set automatically.

---

## 6. Run Migrations and Create Superuser

After your service is built and deployed:
- Go to your service in the Render dashboard.
- Open the **Shell** tab.
- Run:
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py collectstatic --noinput
    ```

---

## 7. Update CORS and CSRF Settings

After deploying your frontend, add its URL to `CORS_ALLOWED_ORIGINS` and `CSRF_TRUSTED_ORIGINS` in `settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8001",
    "https://your-frontend-app.onrender.com",  # or your actual frontend URL
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8001",
    "https://your-frontend-app.onrender.com",
]
```
Then commit and push changes to GitHub; Render will redeploy automatically.

---

## 8. Open Your App

Visit the URL provided by Render (e.g., `https://your-backend-app.onrender.com/`).

---

**Done! Your Django app is now live on Render.**