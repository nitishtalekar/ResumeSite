from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import json

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import data as info

app = Flask(__name__)

print('Check http://127.0.0.1:5000/')


@app.route('/', methods=['GET'])
def index():
    # Main page
    data = info.ResumeData().createdata()
    return render_template('index.html',data = data)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # Main page
    if request.method == "POST":
        form_title = request.form["button"]
        form_data = json.loads(request.form[form_title].replace("\'", "\""))
        final_data = json.dumps(form_data, indent=4)
        file_name = "data/" + form_title.split("_")[-1] + ".json"
        with open(file_name, "w") as outfile:
            outfile.write(final_data)

    data_edit = info.ResumeData().editdata()
    data = info.ResumeData().createdata()
    # print(data, list(data.keys()))

    return render_template('admin.html',data = data, data_edit = data_edit)

if __name__ == '__main__':
    # app.run(port=5002, debug=True)
    app.debug = True
    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0',5000),app)
    http_server.serve_forever()
