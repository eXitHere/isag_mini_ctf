from flask import Flask, send_from_directory, render_template, jsonify
import os
from flask_cors import CORS

static_folder = os.path.abspath('./build')
app = Flask(__name__, static_folder=static_folder)
CORS(app)

#problems_type_by_xx.html
list_problem = []
dict_problem = {}
list_type = set()
def findHtmlFile():
    for file in os.listdir('build/problems'):
        if file.startswith('problem') and file.endswith('.html'):
            file_name_split = file.split('_')
            if len(file_name_split) == 5:
                list_type.add(file_name_split[2])
                try:
                    dict_problem[file_name_split[2]].append(file)
                except:
                    dict_problem[file_name_split[2]] = [file]

@app.route('/api/getProblems', methods=['GET'])
def getProblems():
    return jsonify({
        "type": list(list_type),
        "name": dict_problem
    })

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

findHtmlFile()
#print(dict_problem)
#print(list(list_type))
app.run(debug=False, host='0.0.0.0', port=6543)