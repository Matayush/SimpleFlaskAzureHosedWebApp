# AutoLog

AutoLog is a simple Flask web app for tracking vehicle maintenance, mileage, planned repairs, and running cost.

## Features
- View a clean dashboard with vehicle details and service metrics
- Add maintenance entries from a simple form
- Track completed and planned work
- Store data in a local JSON file for an easy starter setup
- Dark/light theme toggle

## Tech stack
- Python
- Flask
- HTML + Jinja2
- CSS
- JSON storage

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:8000`.

## Project structure
```text
autolog-flask/
├── app.py
├── data.json
├── LICENSE
├── README.md
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Ideas for next steps
- Switch JSON storage to SQLite
- Add edit/delete entry actions
- Add vehicle profiles for multiple cars
- Filter by completed or planned items
- Add cost charts and monthly summaries

## License
MIT
