import csv, json
#import os
from io import TextIOWrapper
from flask import Flask, request,render_template
#from werkzeug.utils import secure_filename

UPLOAD_FOLDER ='D:/Flask/demo_project/uploads'


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_csv():
   return render_template('csv_json.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        data = {}
        csvfile = request.files['file']
        csvfile = TextIOWrapper(csvfile)
        csvreader = csv.DictReader(csvfile, delimiter = ',') #first row of csv taken as column names
        print(csvreader)
        data = {}
        for rows in csvreader:
            id = rows['Test']
            data[id] = rows       
        with open('survey.json', 'w') as jsonfile:
            jsonfile.write(json.dumps(data, indent=4))
    return 'converted successfully'
        
if __name__ == '__main__':
    app.run(debug=True, port = 3000)