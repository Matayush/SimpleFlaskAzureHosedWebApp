from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mateusz,<br><br>Best regards,<br>World"

if __name__ == "__main__":
    app.run(debug=True)

