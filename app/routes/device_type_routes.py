from flask import Blueprint, render_template, request, redirect, url_for
import requests

device_bp = Blueprint("device_bp", __name__)

API_BASE_URL = "http://127.0.0.1:5000/device_types/device_type"


@device_bp.route("/device_types", methods=["GET"])
def index():
    response = requests.get(API_BASE_URL)
    data = response.json()
    devices = data[0] if isinstance(data, list) and len(data) > 0 else []
    return render_template("device_pages/device_list.html", devices=devices)


@device_bp.route("/add_device_type", methods=["GET", "POST"])
def add_device():
    if request.method == "POST":
        payload = {
            "deviceType": request.form["deviceType"],
            "protocol": request.form["protocol"],
            "command": request.form["command"],
        }
        requests.post(API_BASE_URL, json=payload)
        return redirect(url_for("device_bp.index"))
    return render_template("device_pages/add_device.html")


@device_bp.route("/update_device_type/<int:id>", methods=["GET", "POST"])
def update_device(id):
    if request.method == "POST":
        payload = {
            "deviceType": request.form["deviceType"],
            "protocol": request.form["protocol"],
            "command": request.form["command"],
        }
        requests.put(f"{API_BASE_URL}/{id}", json=payload)
        return redirect(url_for("device_bp.index"))

    response = requests.get(f"{API_BASE_URL}/{id}")
    device = response.json() if response.status_code == 200 else {}
    return render_template("device_pages/update_device.html", device=device)


@device_bp.route("/delete_device_type/<int:id>")
def delete_device(id):
    requests.delete(f"{API_BASE_URL}/{id}")
    return redirect(url_for("device_bp.index"))
