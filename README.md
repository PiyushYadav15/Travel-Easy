# Travel-Easy
A **Django-based Travel Management Application** that allows users to explore travel destinations,  read blogs. This project is designed to simulate a real-world travel website with authentication, booking system, and content management features. (all code avilable in sub-branch)

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

<img width="1920" height="1200" alt="Screenshot 2025-09-17 102523" src="https://github.com/user-attachments/assets/3bf0d0f1-e6bc-4376-9642-3aa77537d121" />

<img width="1920" height="1200" alt="Screenshot 2025-09-17 102620" src="https://github.com/user-attachments/assets/a9f039cf-3c96-4afe-b10b-25d374d0d7e8" />


🏠 Home Page
<img width="1920" height="1200" alt="Screenshot 2025-09-17 102542" src="https://github.com/user-attachments/assets/6b7bdf1c-ac08-45e1-b703-34ea3955232f" />

🌍 Destination List
<img width="1920" height="1200" alt="Screenshot 2025-09-17 102605" src="https://github.com/user-attachments/assets/e2de3401-cc66-4e18-a551-8a703aafc1ac" />


📖 Destination Detail

<img width="1920" height="1200" alt="Screenshot 2025-09-17 111521" src="https://github.com/user-attachments/assets/f9aa4861-cbdc-4de9-a543-3b389e517986" />
<img width="1920" height="1200" alt="Screenshot 2025-09-17 102646" src="https://github.com/user-attachments/assets/81f451df-f0b3-4c29-a735-d3eb3058ec37" />

<img width="1920" height="1200" alt="Screenshot 2025-09-17 102637" src="https://github.com/user-attachments/assets/2cf94c5b-7dd4-4957-9f2b-8e25f23c839e" />


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
