
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.get_json()
    bubble_id = data.get('bubble_id')
    note = data.get('note')
    # Here you can save the note to a database or a file
    return jsonify({'status': 'success', 'bubble_id': bubble_id, 'note': note})

if __name__ == '__main__':
    app.run(port=5000)
