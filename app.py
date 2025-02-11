from flask import Flask, request, jsonify, render_template
import sqlite3
import subprocess
import json
import os
import threading
import time
import logging

app = Flask(__name__)

DB_PATH = r"DataBases\products.db"
JSON_PATH = "static/data.json"

def get_db_connection():
    """ Establish and return a database connection. """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    """ Render the main HTML page. """
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    
    """ Handle barcode scanning and return product details. """
    data = request.get_json()
    barcode = data.get("barcode")

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT product_name, price, previous_price, inventory FROM products WHERE barcode = ?", (barcode,))
    result = cursor.fetchone()
    conn.close()

    if result:
        product_data = {
            "barcode": barcode,
            "item_name": result[0],
            "price": result[1],
            "previous_price": result[2],
            "inventory": result[3]
        }
    else:
        product_data = {"error": "Product not found"}

    # Save data to JSON file for frontend access
    with open(JSON_PATH, "w") as f:
        json.dump(product_data, f)

    # Reset JSON file after 30 seconds
    reset_json_after_delay()

    return jsonify(product_data)

    
def reset_json_after_delay():
    """ Clear the JSON file 30 seconds after the last scan. """
    global reset_timer

    if "reset_timer" in globals() and reset_timer.is_alive():
        reset_timer.cancel()  # Cancel any ongoing timer if a new scan occurs

    reset_timer = threading.Timer(30, clear_json_file)
    reset_timer.start()

def clear_json_file():
    """ Empty the JSON file. """
    open(JSON_PATH, "w").close()
    print("✅ JSON file has been cleared after 30 seconds of inactivity.")

if __name__ == "__main__":
    
    # log = logging.getLogger('werkzeug')
    # log.setLevel(logging.ERROR)
    # Ensure JSON file is empty at startup
    open(JSON_PATH, "w").close()

    # Start the scanner process automatically
    subprocess.Popen(["python", "scanner.py"])
    
    app.run(debug=True)
