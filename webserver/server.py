from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")    

@app.route("/blog")
def blog():
    return "<h1>This is for the blogs</h1>"

@app.route("/blog/2022/dogs")
def blog2():
    return "<h1>Snoop Doug</h1>"   

