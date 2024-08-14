from flask import Blueprint, render_template, request, redirect, url_for
import requests

customer_devices_bp = Blueprint("customer_devices_bp", __name__)

API_BASE_URL = "http://127.0.0.1:5000/customer_devices/customer_device"


@customer_devices_bp.route(
    "/customer_devices", methods=["GET", "POST", "PUT", "DELETE"]
)
def index():
    response = requests.get(API_BASE_URL)
    data = response.json()
    customer_devices = data[0] if isinstance(data, list) and len(data) > 0 else []
    return render_template(
        "customer_devices_pages/customer_devices_table.html",
        customer_devices=customer_devices,
    )


@customer_devices_bp.route("/add_customer_devices", methods=["GET", "POST"])
def add_customer_devices():
    if request.method == "POST":
        payload = {
            "customerId": request.form["customerId"],
            "deviceTypeId": request.form["deviceTypeId"],
            "port": request.form["port"],
            "ipHost": request.form["ipHost"],
        }
        requests.post(API_BASE_URL, json=payload)
        return redirect(url_for("customer_devices_bp.index"))
    return render_template("customer_devices_pages/add_customer_devices.html")


@customer_devices_bp.route("/update_customer_devices/<int:id>", methods=["GET", "POST"])
def update_customer_devices(id):
    if request.method == "POST":
        firstName = request.form["customerId"]
        lastName = request.form["deviceTypeId"]
        mail = request.form["port"]
        phoneNumber = request.form["ipHost"]
        payload = {
            "customerId": firstName,
            "deviceTypeId": lastName,
            "port": mail,
            "ipHost": phoneNumber,
        }
        requests.put(f"{API_BASE_URL}/{id}", json=payload)
        return redirect(url_for("customer_devices_bp.index"))

    response = requests.get(f"{API_BASE_URL}/{id}")
    customer_device = response.json() if response.status_code == 200 else {}
    return render_template(
        "customer_devices_pages/update_customer_devices.html", customer_device=customer_device
    )


@customer_devices_bp.route("/delete_customer_devices/<int:id>")
def delete_customer_devices(id):
    requests.delete(f"{API_BASE_URL}/{id}")
    return redirect(url_for("customer_devices_bp.index"))
