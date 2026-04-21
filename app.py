from flask import Flask, request
import csv
import os
from datetime import datetime

app = Flask(__name__)

def log_request(ip, endpoint, method, status):
    file_exists = os.path.isfile("logs.csv")

    with open("logs.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "ip_address", "endpoint", "method", "status"])

        writer.writerow([datetime.now(), ip, endpoint, method, status])

@app.route("/")
def home():
    log_request(request.remote_addr, request.path, request.method, "success")
    return "Flask server is running"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        log_request(request.remote_addr, request.path, request.method, "success")
        return f"Welcome, {username}"

    log_request(request.remote_addr, request.path, request.method, "success")
    return """
    <form method="POST">
        <input type="text" name="username" placeholder="Enter username">
        <button type="submit">Login</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
