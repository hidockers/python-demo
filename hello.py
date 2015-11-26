from datetime import datetime
from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/env')
def env():
    html = "<h1>System Time:<h1>"
    html += '<h3>' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '</h3>'
    return Response(html, mimetype='text/plain')