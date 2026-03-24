# flask-product-dashboard
Flask-based product dashboard that fetches data from an API, stores it in MySQL, and provides search, filtering, and Excel export features.
---
A full-stack web application built using Flask that fetches product data from an API, stores it in MySQL, and displays it in a dynamic dashboard.
---
## > Features
*    Fetch data from API
*    Store data in MySQL database
*    Search products by title
*    Refresh data from API
*    Display products in dashboard (Flask + HTML + CSS)
*    Export data to Excel
---
##  Tech Stack
* Python (Flask)
* MySQL
* Pandas
* HTML, CSS
* REST API (FakeStore API)
---

## 📂 Project Structure
```
flask-product-dashboard/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```
--
## ⚙️ Installation & Setup

### 1️ Clone the repository

```bash
git clone https://github.com/hemantgoswami-24/flask-product-dashboard.git
cd flask-product-dashboard
```

### 2️ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️ Setup MySQL Database
```sql
CREATE DATABASE flask;
```
> Update your MySQL credentials in `app.py`.
---
### 5️ Run the application
```bash
python app.py
```
> Open in browser:
```
http://127.0.0.1:5000/
```
---
## 📸 Screenshots
(Add your project screenshots here)
---
##  What I Learned
* Working with APIs and JSON data
* Integrating Flask with MySQL
* Building dynamic dashboards
* Data handling using Pandas
* Backend development workflow
---
##  Future Improvements
* Add user authentication (login system)
* Add product filters (price range, category)
* Deploy on cloud (Render / AWS)
* Improve UI with React
---
## 👨‍💻 Author
Hemant Giri
---
## ⭐ Show Your Support
If you like this project, give it a ⭐ on GitHub!
