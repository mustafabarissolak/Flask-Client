from flask import Blueprint, render_template, request, redirect, url_for
import requests

customer_bp = Blueprint("customer_bp", __name__)

API_BASE_URL = "http://127.0.0.1:5000/"
customer_url = "customers/customer"


@customer_bp.route("/customers", methods=["GET", "POST", "PUT", "DELETE"])
def index():
    response = requests.get(API_BASE_URL + customer_url)
    data = response.json()
    customers = data[0] if isinstance(data, list) and len(data) > 0 else []
    return render_template("customer_pages/customers.html", customers=customers)


@customer_bp.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    if request.method == "POST":
        payload = {
            "firstName": request.form["firstName"],
            "lastName": request.form["lastName"],
            "mail": request.form["mail"],
            "phoneNumber": request.form["phoneNumber"],
            "address": request.form["address"],
        }
        requests.post(API_BASE_URL+ customer_url, json=payload)
        return redirect(url_for("customer_bp.index"))
    return render_template("customer_pages/add_customer.html")


@customer_bp.route("/update_customer/<int:id>", methods=["GET", "POST"])
def update_customer(id):
    if request.method == "POST":
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        mail = request.form["mail"]
        phoneNumber = request.form["phoneNumber"]
        address = request.form["address"]
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "mail": mail,
            "phoneNumber": phoneNumber,
            "address": address,
        }
        requests.put(f"{API_BASE_URL}{customer_url}/{id}", json=payload)
        return redirect(url_for("customer_bp.index"))

    response = requests.get(f"{API_BASE_URL}{customer_url}/{id}")
    customer = response.json() if response.status_code == 200 else {}
    return render_template("/customer_pages/update_customer.html", customer=customer)


@customer_bp.route("/delete_customer/<int:id>")
def delete_customer(id):
    requests.delete(f"{API_BASE_URL}{customer_url}/{id}")
    return redirect(url_for("customer_bp.index"))
