from flask import Flask, render_template, send_file, request
import process
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def process_image(): 
    m1, m2 = request.form['m1'], request.form['m2']

    image_bytes = BytesIO()
    process.create_image(m1, m2).save(image_bytes, 'JPEG', quality=80, optimize=True, progressive=True)

    file = f'data:image/jpeg;base64,{b64encode(image_bytes.getvalue()).decode()}'
    # return send_file(file, mimetype='image/jpeg', as_attachment=True, attachment_filename='image.jpg')
    return f'<img src="{file}" alt=\'nothing\'>'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='localhost', port='8080')
