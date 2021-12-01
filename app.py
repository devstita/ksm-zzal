from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/create/<m1>/<m2>')
def create_image(m1, m2): 
    print(m1, m2)
    return "Ok"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(host='localhost', port='8080')