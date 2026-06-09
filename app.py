from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.json')

DEFAULT_DATA = {
    "vehicle": {
        "name": "BMW E91 Touring",
        "model_year": 2006,
        "plate": "KK 76747",
        "current_mileage": 288000
    },
    "entries": [
        {
            "id": 1,
            "service": "Engine oil and filter",
            "date": "2026-05-20",
            "mileage": 184900,
            "cost": 420,
            "status": "Completed",
            "notes": "Changed oil, oil filter, cabin filter."
        },
        {
            "id": 2,
            "service": "Rear suspension refresh",
            "date": "2026-06-30",
            "mileage": 186800,
            "cost": 1800,
            "status": "Planned",
            "notes": "Subframe check, bump stops, rollers, rear shocks."
        },
        {
            "id": 3,
            "service": "Brake fluid service",
            "date": "2026-04-11",
            "mileage": 183100,
            "cost": 230,
            "status": "Completed",
            "notes": "Brake fluid flush and quick brake inspection."
        }
    ]
}


def load_data():
    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


@app.route('/')
def index():
    data = load_data()
    entries = sorted(data['entries'], key=lambda x: x['date'], reverse=True)
    total_cost = sum(float(item.get('cost', 0) or 0) for item in entries)
    planned_count = sum(1 for item in entries if item['status'] == 'Planned')
    completed_count = sum(1 for item in entries if item['status'] == 'Completed')
    next_service = next((item for item in sorted(entries, key=lambda x: x['date']) if item['status'] == 'Planned'), None)
    return render_template(
        'index.html',
        vehicle=data['vehicle'],
        entries=entries,
        total_cost=total_cost,
        planned_count=planned_count,
        completed_count=completed_count,
        next_service=next_service,
        now=datetime.utcnow()
    )


@app.route('/add', methods=['POST'])
def add_entry():
    data = load_data()
    entries = data['entries']
    new_id = max((item['id'] for item in entries), default=0) + 1
    entries.append({
        'id': new_id,
        'service': request.form['service'],
        'date': request.form['date'],
        'mileage': int(request.form['mileage']),
        'cost': float(request.form['cost'] or 0),
        'status': request.form['status'],
        'notes': request.form['notes']
    })
    try:
        data['vehicle']['current_mileage'] = max(data['vehicle']['current_mileage'], int(request.form['mileage']))
    except Exception:
        pass
    save_data(data)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
