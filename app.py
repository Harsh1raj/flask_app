from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to ITIL exam"

@app.route('/subjects')
def subjects():
    return "Subjects: COSA, ITIM, DevOps, CF"

@app.route('/contact')
def contact():
    return "Name: Harsh, PRN: 3011, Phone: 62005777332"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
