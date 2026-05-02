from flask import Flask, render_template, request, jsonify
import os
from .database import init_db, add_item, get_items

app = Flask(__name__)

# Ініціалізація БД при запуску
init_db()

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/api/add', methods=['POST'])
def api_add():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    add_item(data['name'])
    return jsonify({"status": "success"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)