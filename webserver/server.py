from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:pagename>")
def html_page(pagename):
    return render_template(pagename)

def write_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')        

def write_csv(data):
    with open('database.csv', mode='a', ) as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',newline='', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_file(data)
            write_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'cant save to DB'
    else:
        return 'error'    

# @app.route("/works.html")
# def work():
#     return render_template('works.html')

# @app.route("/blog/2022/dogs")
# def blog2():
#     return "<h1>Snoop Doug</h1>"   

