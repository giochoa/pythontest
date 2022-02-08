from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:pagename>")
def html_page(pagename):
    return render_template(pagename)    

# @app.route("/works.html")
# def work():
#     return render_template('works.html')

# @app.route("/blog/2022/dogs")
# def blog2():
#     return "<h1>Snoop Doug</h1>"   

