from flask import Flask
import gunicorn
import readpdf
import utils
import json
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/text/<filename>', methods=['GET'])
def get_pdf_content(filename):
    file_path = './resume/' + filename
    return readpdf.convert_pdf_to_txt(file_path)

@app.route('/api/ranking/<query>', methods=['GET'])
def rank_documents(query):
    pdf_file_list = os.listdir('./resume/')
    candidate_list = utils.parse_candidate(pdf_file_list)
    return json.dumps(candidate_list)

if __name__ == '__main__':
    app.run()
