from flask import Flask, request, redirect
from flask import render_template
from werkzeug.utils import secure_filename
from p_card_ninja import file_handler

import os, time
app = Flask(__name__)

UPLOAD_FOLDER = '/tmp/'
@app.route('/submit_list', methods=['POST'])
def submit_list():
        #store the data, reload page originated
    file = request.files['fileupload']
    filename = secure_filename(file.filename)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filepath = os.path.join(UPLOAD_FOLDER, timestr + filename)
    file.save(filepath)
    #probably return some success or failure message
    # rturn output
    return render_template('hello.html')
    #return secure_filename(file.filename)

@app.route('/')
def hello_world():
    return render_template('hello.html')
