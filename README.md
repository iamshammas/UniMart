# 🛒 Django E-Commerce Web Application

A full-stack e-commerce web application built using **pure Django** (without Django REST Framework).
This project implements the complete shopping flow using server-rendered templates and relational database design.

---

## ✨ Features

* 🔐 User authentication (Register, Login, Logout)
* 👤 User profile with order history
* 📦 Product listing with categories
* 🔍 Product detail view
* 🧺 Shopping cart (add, update, remove items)
* 💳 Checkout with Cash on Delivery (COD)
* 🧾 Order creation with order items
* 📑 Order detail and history pages
* 🎨 Responsive UI using Bootstrap
* ⚙️ Django signals for automatic profile creation

---

## 🛠 Tech Stack

* **Backend:** Django (Function-based views, no DRF)
* **Frontend:** HTML, Bootstrap, minimal JavaScript
* **Database:** SQLite (development)
* **Auth:** Django built-in User model

---

## 📂 Project Highlights

* Clear separation between **Cart** and **Order**
* Uses proper database relationships (OneToOne, ForeignKey)
* Snapshot pricing stored in OrderItem
* Simple, scalable architecture suitable for beginners
* Focused on real-world Django learning, not over-engineering

---

## 🚀 Getting Started

```bash
git clone <repository-url>
cd project-folder
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 📌 Notes

* This project does **not** use Django REST Framework.
* Payment gateway integration is not included (COD only).
* Designed as a learning-focused project, not production-ready.

---

## 🎯 Purpose

Built to understand:

* Django models and relationships
* Cart → Order lifecycle
* Checkout and order processing
* Server-side rendering and form handling
* Clean Django project structure

---

## 📄 License

This project is for educational purposes.

