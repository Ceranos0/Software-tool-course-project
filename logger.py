import csv
import os
from datetime import datetime

def log_request(ip, endpoint, method, status):
    file_exists = os.path.isfile("logs.csv")

    with open("logs.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["timestamp", "ip_address", "endpoint", "method", "status"])

        writer.writerow([datetime.now(), ip, endpoint, method, status])

def suspicious_input(text):
    bad_patterns = ["<script>", "' OR 1=1", "--"]

    for pattern in bad_patterns:
        if pattern in text:
            return True
    return False
