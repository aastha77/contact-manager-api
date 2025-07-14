# 📞 Contact Manager API

![Django](https://img.shields.io/badge/Backend-Django-092E20?style=flat&logo=django&logoColor=white)
![REST API](https://img.shields.io/badge/API-REST--Framework-ff69b4)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This is a simple Django REST Framework-based Contact Manager API that allows users to perform full CRUD operations on contact records.

---

## 🔧 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (default)

---

## 📁 Features

- Add a new contact
- View all contacts
- View a single contact
- Update contact details
- Delete a contact
- Admin Panel for managing contacts

---

## 🧪 API Endpoints

| Method | Endpoint                | Description            |
|--------|-------------------------|------------------------|
| GET    | /api/contacts/          | List all contacts      |
| POST   | /api/contacts/          | Create new contact     |
| GET    | /api/contacts/{id}/     | Get contact details    |
| PUT    | /api/contacts/{id}/     | Update contact         |
| DELETE | /api/contacts/{id}/     | Delete contact         |

---

## ▶️ How to Run Locally

```bash
# 1. Clone this repo
git clone https://github.com/aastha77/contact-manager-api.git
cd contact-manager-api

# 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser (for admin panel)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver

🔐 Admin Panel: http://127.0.0.1:8000/admin/

🧑‍💻 Author
Aastha Pandey
GitHub | LinkedIn

