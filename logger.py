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
