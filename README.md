# ecommerce-product-catalog-backend
A Django REST API for managing and browsing products, with role-based admin access. Supports product listing, detail view, admin-only add/delete, and category-based filtering.

# Deploying to Heroku

Follow these steps to deploy this Django project to Heroku.

---

## 1. Prerequisites

- [Heroku account](https://signup.heroku.com/)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- [Git](https://git-scm.com/) installed

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
        MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
        ```
    - Set allowed hosts:
        ```python
        ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']
        ```
    - Set debug mode:
        ```python
        DEBUG = os.environ.get('DEBUG', 'False') == 'True'
        ```

---

## 4. Initialize Git

If not already a git repo:
```
git init
git add .
git commit -m "Prepare project for Heroku deployment"
```

---

## 5. Create and Configure Heroku App

1. **Login to Heroku:**
    ```
    heroku login
    ```

2. **Create a new Heroku app:**
    ```
    heroku create your-app-name
    ```

3. **Set environment variables:**
    ```
    heroku config:set SECRET_KEY='your-secret-key'
    heroku config:set DEBUG=False
    ```

---

## 6. Deploy to Heroku

1. **Push code:**
    ```
    git push heroku master
    ```
    *(or `git push heroku main` if your branch is named main)*

2. **Run migrations:**
    ```
    heroku run python manage.py migrate
    ```

3. **Create superuser:**
    ```
    heroku run python manage.py createsuperuser
    ```

4. **Collect static files:**
    ```
    heroku run python manage.py collectstatic --noinput
    ```

---

## 7. Open Your App

```
heroku open
```
Or visit `https://your-app-name.herokuapp.com/`

---

**Done! Your Django app is now live on Heroku.**