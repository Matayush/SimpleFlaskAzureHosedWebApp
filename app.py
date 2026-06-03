from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mateusz,\n\nBest regards,\nWorld"

if __name__ == "__main__":
    app.run(debug=True)

