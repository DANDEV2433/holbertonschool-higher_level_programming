import sqlite3
from flask import Flask, render_template, request
import json, csv

app= Flask(__name__)

@app.route('/products')
def data():
    source = request.args.get('source', type=str)
    id = request.args.get('id', type=int)
    products = []
    if source == "sql":
        products = get_products_from_sql()
        if isinstance(products, str):  # Vérifie si une erreur est retournée
            return render_template("product_display.html", error=products)
    elif source == "json":
        with open('products.json', 'r') as file:
            products = json.load(file)
    elif source == "csv":
        with open('products.csv', newline= "") as file:
            reader = csv.DictReader(file)
            products = [row for row in reader]
    else: # Si la source est invalide".
        return render_template("product_display.html", error="Invalid source parameter.")
    if id:
        products = [product for product in products if int(product["id"]) == id]
    if not products: # Vérifie si la liste est vide après le filtrage.
        return render_template("product_display.html", error="Product not found.")
    
    # Passer les produits au modèle HTML
    return render_template("product_display.html", products=products)

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

def get_products_from_sql():
        # Connecte à la base SQLite
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        # Exécute une requête pour récupérer tous les produits
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()

        # Transforme les résultats en une liste de dictionnaires
        products = [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in rows
        ]

        # Ferme la connexion
        conn.close()
        return products
    
if __name__ == '__main__':
    create_database()