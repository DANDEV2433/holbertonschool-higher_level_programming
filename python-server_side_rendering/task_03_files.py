from flask import Flask, render_template, request
import json, csv

app= Flask(__name__)

@app.route('/products')
def data():
    source = request.args.get('source', type=str)
    id = request.args.get('id', type=int)
    products = []
    if source == "json":
        with open('products.json', 'r') as file:
            products = json.load(file)
    elif source == "csv":
        with open('products.csv', newline= "") as file:
            reader = csv.DictReader(file)
            products = [row for row in reader]
    else: # Si la source n'est ni "json" ni "csv".
        return render_template("product_display.html", error="Invalid source parameter.")
    if products:
        products = [product for product in products if int(product["id"]) == product_id]
    if not products: # Vérifie si la liste est vide après le filtrage.
        return render_template("product_display.html", error="Product not found.")


