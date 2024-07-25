# api/app.py
from flask import Flask, request, jsonify
from models import Case, session
from utils.docx_generator import populate_template

app = Flask(__name__)

@app.route('/cases', methods=['GET'])
def get_cases():
    cases = session.query(Case).all()
    return jsonify([case.case_name for case in cases])

@app.route('/populate', methods=['POST'])
def populate():
    data = request.json
    output_path = populate_template('templates/case_template.hd', data)
    return jsonify({'output_path': output_path})

if __name__ == '__main__':
    app.run(debug=True)
