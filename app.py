from flask import Flask, render_template, send_file, redirect
import process
import time
from io import BytesIO

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/create/<m1>/<m2>')
def process_image(m1, m2): 
    file = BytesIO()
    process.create_image(m1, m2).save(file, 'JPEG', quality=80, optimize=True, progressive=True)
    return send_file(file, mimetype='image/jpeg', as_attachment=True, attachment_filename='image.jpg')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='localhost', port='8080')
