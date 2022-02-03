from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/download')
def download():
    return send_file("index.html", as_attachment=True)
