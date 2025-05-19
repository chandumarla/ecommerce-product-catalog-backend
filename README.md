# 🛍️ E-Commerce Product Catalog API (Backend)

This is the backend for the **E-Commerce Product Catalog** built using Django and Django REST Framework. It provides RESTful API endpoints to manage and serve product data, including product listing, detail view, admin CRUD, and user authentication.

---

## 🚀 Features

- 🧾 Product catalog with title, description, price, and image
- 🔐 Admin authentication with token-based access
- 🧩 Django REST Framework APIs
- ⚙️ MySQL database support (configured for PythonAnywhere)
- 🛠️ Django Admin Panel for content management

---

## 🧰 Tech Stack

- Python 3
- Django 4+
- Django REST Framework
- MySQL (PythonAnywhere)
- Token Authentication

---

## 📁 Project Structure

ecommerce-product-catalog-backend/
├── catalog/ # App containing models, views, serializers
├── ecommerce_backend/ # Main Django project settings
├── db.sqlite3 / MySQL # Database
├── manage.py
└── requirements.txt

## 🔧 Setup Instructions (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/chandumarla/product_catalog_api.git
   cd product_catalog_api

## Create virtual environment and install dependencies
 ```bash
   python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Configure .env or settings for MySQL (optional)

Update DATABASES in settings.py if using MySQL

## Run migrations
 ```bash
python manage.py migrate
Create superuser

 ## create superuser
 ```bash
python manage.py createsuperuser

## Run development server
 ```bash

python manage.py runserver

## 🔐Token Authentication (Admin)
Generate token for a user (e.g., admin):
Run this command in terminal
 ```bash
python manage.py shell
# add this code
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
token, _ = Token.objects.get_or_create(user=user)
print(token.key)

## 📦 API Endpoints
Method     	Endpoint	          Description	             Auth Required
GET	      /api/products/	     List all products	          ❌ No
GET	     /api/products/<id>/	 Get single product details	  ❌ No
POST	   /api/products/	       Create a product	            ✅ Yes (Admin)
PUT	    /api/products/<id>/	   Update a product           	✅ Yes (Admin)
DELETE	/api/products/<id>/	   Delete a product           	✅ Yes (Admin)

## 🛰️ Deployment
This backend is deployed on PythonAnywhere using:

MySQL database (free tier)

WSGI configuration

Admin and token auth enabled

# API Base URL:
https://yourusername.pythonanywhere.com/api/products/











