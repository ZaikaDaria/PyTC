from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    return render_template('homepage.html')


@app.route('/greet', methods=['POST', 'GET'])
def greet():
    name = request.form.get('name')
    greeting = f'Hello, {name}!'
    return render_template('greet.html', greeting=greeting)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
