# Travel-Easy
A **Django-based Travel Management Application** that allows users to explore travel destinations,  read blogs. This project is designed to simulate a real-world travel website with authentication, booking system, and content management features.

## ✨ Features
### 🗺️ Destinations
- Browse a list of available travel destinations
- View detailed descriptions, images, country, and price
- Each destination has a dedicated detail page
- ✏️ Profile Update – users can update their personal details (name, email, etc.)

🔑 Password Update – users can securely change their password


### 📅 Booking System
- Authenticated users can book a destination
- Choose travel dates and number of people
- View and manage all your bookings in a **user dashboard*


### 📝 Blogs
- Read travel-related blogs with rich content and images
- Blogs are stored in the database and displayed dynamically


### 👤 Authentication
- User sign-up and login using Django’s built-in **User model**
- Secure booking only for logged-in users


---


## 🛠️ Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default, but easily switchable to PostgreSQL/MySQL)
- **Frontend:** HTML, CSS (with Django Templates)
- **Authentication:** Django built-in auth system
📸 Demo Screenshots
🏠 Home Page

🌍 Destination List

📖 Destination Detail



---
1. **Clone the repository**
```bash
git clone https://github.com/your-username/travel-project.git
cd travel-project
```


2. **Create virtual environment & activate**
```bash
python -m venv venv
source venv/bin/activate # On Linux/Mac
venv\Scripts\activate # On Windows
```


3. **Install dependencies**
```bash
pip install -r requirements.txt
```


4. **Run migrations**
```bash
python manage.py migrate
```


5. **Start development server**
```bash
python manage.py runserver
```


6. Open in browser:
```
http://127.0.0.1:8000/
```


---


## 📂 Project Structure
```
travel/
│── models.py # Database models for Destinations, Bookings, Blogs
│── views.py # Business logic and request handling
│── urls.py # Application routes
│── forms.py # Forms for bookings and authentication
│── templates/ # HTML templates (home, booking, blogs, etc.)
│── static/ # CSS, JS, and images
```


---


## 🔮 Future Enhancements
- Add **payment gateway integration** for bookings
- Add **reviews and ratings** for destinations
- Implement **search and filter** for destinations


---


## 🤝 Contributing
Contributions are welcome! Fork the repo, make changes, and submit a pull request.
