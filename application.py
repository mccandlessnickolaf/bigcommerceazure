from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("http://www.example.com", code=302)
