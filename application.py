from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://afflat3b1.com/lnk.asp?o=11504&c=918273&a=279700&k=FD30C0A12AA3AB7D4FFFDEB75CEA03F1&l=11596", code=302)
