import datetime
from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/env')
def env():
    html = "System Time: \n\n"
    html += datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return Response(html, mimetype='text/plain')
