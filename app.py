
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission
    data = request.form.to_dict()
    # For now, just print the data to the console
    print(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000)
