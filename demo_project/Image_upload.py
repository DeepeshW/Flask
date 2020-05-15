from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os



UPLOAD_FOLDER ='D:/Flask/demo_project/uploads'
Allowed_Extentions = {'png','jpg', 'jpeg'}

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.form,
    ))

def allowed_filename(filename):
    return '.' in filename and filename.split('.',1)[1].lower() in Allowed_Extentions

@app.route('/')
def upload_template():
    return render_template('upload.html')

@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(f.items)
        pretty_print_POST(request)
        return 'test'
        #f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        #return 'file uploaded successfully'
        if f not in request.files:
            flash('File not found')
            return redirect(request.url)
        
        if f.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if f and allowed_filename(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('/', filename = filename))
    

if __name__ == '__main__':
    app.run(debug=True)
        