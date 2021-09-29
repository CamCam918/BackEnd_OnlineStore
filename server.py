from mock_data import mock_data
from flask import Flask, render_template, request, abort
import json
from flask_cors import CORS
from config import db

app = Flask(__name__)
CORS(app)
me = {
    "name": "Cameron",
    "last": "Campbell",
    "email": "test@email.com",
    "age": 30,
    "hobbies": [],
    "address": {
        "street": "main",
        "number": "42"
    }
}


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return f"{me['name']} {me['last']}"


@app.route("/about/email")
def get_email():
    return me["email"]


@app.route("/about/address")
def get_address():
    address = me["address"]
    return address["number"] + " " + address["street"]

# API Methods


@app.route("/api/catalog", methods=["GET"])
def get_catalog():
    # read products from database and return it
    cursor = db.products.find({})  # get all records/documents
    catalog = []
    for prod in cursor:
        catalog.append(prod)

    return json.dumps(catalog)


@app.route("/api/catalog", methods=["POST"])
def save_product():
    product = request.get_json()
    if not "price" in product or product["price"] <= 0:
        abort(400, "Price is required and should be greater than zero")

    if not "title" in product or len(product["title"]) < 5:
        abort(400, "Title is required and should be at least 5 chars long")

    mock_data.append(product)
    product["_id"] = len(product["title"])
    return json.dumps(product)


@app.route("/api/categories")
def get_categories():
    # return a list of with all products

    categories = []
    for product in mock_data:
        cat = product["category"]

        if cat not in categories:
            categories.append(cat)


@app.route("/api/product/<id>")
def get_by_id(id):
    # find the product with such id
    # return the product as json string
    found = False
    for prod in mock_data:
        if prod["_id"] == id:
            found = True
            return json.dumps(prod)
    if not found:
        abort(404)


@app.route("/api/catalog/<cat>")
def get_by_cat(category):
    prods = []
    for prod in mock_data:
        if (prod["category"].lower() == category.lower()):
            prods.append(prod)

    return json.dumps(prods)


@app.route("/api/cheapest")
def get_cheapest():
    for prod in mock_data:
        if prod["price"] < cheapest["price"]:
            cheapest = prod
    return json.dumps(cheapest)


@app.route("/api/test/loadData")
def load_data():

    return "Data Already Loaded"
    # load every product int he mock_data into the database
    for prod in mock_data:
        db.products.insert_one(prod)

    return "Data Loaded"


app.run(debug=True)
