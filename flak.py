from flask import Flask, render_template, request, redirect, send_file
import requests
import mysql.connector
import pandas as pd

app = Flask(__name__)

# 🔹 DB Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="enter your password",  #i have not given my password for security reasons, you can put your password here
        database="flask"
    )

# 🔹 API se data fetch
def fetch_from_api():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    return response.json()

# 🔹 API data ko DB me store/update
def store_data(data):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS webproduct(
        id INT PRIMARY KEY,
        title VARCHAR(255),
        price FLOAT
    )
    """)

    for product in data:
        cursor.execute("""
        INSERT INTO webproduct (id,title,price)
        VALUES (%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        title=VALUES(title),
        price=VALUES(price)
        """, (product["id"], product["title"], product["price"]))

    conn.commit()
    conn.close()

# 🔹 fetch data from database with search
def get_products(search=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if search:
        cursor.execute(
            "SELECT * FROM webproduct WHERE title LIKE %s",
            ('%' + search + '%',)
        )
    else:
        cursor.execute("SELECT * FROM webproduct")

    data = cursor.fetchall()
    conn.close()
    return data

# 🔹 Home (Display + Search)
@app.route("/")
def home():
    search = request.args.get("search")
    products = get_products(search)
    return render_template("index.html", products=products)

# 🔹 API Refresh Button
@app.route("/refresh")
def refresh():
    data = fetch_from_api()   # API call
    store_data(data)          # DB update
    return redirect("/")      # Home pe wapas

# 🔹 Excel Download
@app.route("/export")
def export():
    products = get_products()
    df = pd.DataFrame(products)
    file_name = "products.xlsx"
    df.to_excel(file_name, index=False)
    return send_file(file_name, as_attachment=True)

# 🔹 Run App
if __name__ == "__main__":
    app.run(debug=True)