from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import json

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, session
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import data as info
import loaddb as load

app = Flask(__name__)

print('Check http://127.0.0.1:5000/')


@app.route('/', methods=['GET'])
def index():
    # Main page
    data = info.ResumeData().createdata()
    return render_template('index.html',data = data)
    
@app.route('/projects', methods=['GET'])
def project():
    # Project page
    data = info.ResumeData().createdata()
    return render_template('projects.html',data = data, pagename = 'Projects', init = 'proj_'+str(len(data['proj_list'])))
    
@app.route('/artworks', methods=['GET'])
def artwork():
    # Artwork page
    data = info.ResumeData().createdata()
    return render_template('artworks.html',data = data, pagename = 'Artworks', init = 'art_'+str(len(data['artwork'])))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == "POST":
        if 'login' in request.form:
            pwd = request.form["pwd"]
            if pwd == "nitish503":
                session['admin'] = True
                return redirect('/adminpage')
    session['admin'] = False
    return render_template('login.html')
    
@app.route('/adminpage', methods=['GET', 'POST'])
def adminpage():
    if not session['admin']:
        session['admin'] = False
        return redirect('/admin')
    else:
        if request.method == "POST":
            if 'submit' in request.form:
                form_title = request.form["submit"]
                form_data = json.loads(request.form[form_title].replace("\'", "\""))
                final_data = json.dumps(form_data, indent=4)
                file_name = "data/" + form_title.split("_")[-1] + ".json"
                with open(file_name, "w") as outfile:
                    outfile.write(final_data)
            elif 'load_jobs' in request.form:
                load.LoadData().load_jobs()
            elif 'load_exp' in request.form:
                load.LoadData().load_exp()
            elif 'load_edu' in request.form:
                load.LoadData().load_edu()
            elif 'load_projects' in request.form:
                load.LoadData().load_projects()
            elif 'load_art' in request.form:
                load.LoadData().load_art()
                

        data_edit = info.ResumeData().editdata()
        data = info.ResumeData().createdata()
        for key in data_edit:
            data_edit[key] = json.dumps(data_edit[key], indent = 4)
        return render_template('admin.html',data = data, data_edit = data_edit)

if __name__ == '__main__':
    # app.run(port=5002, debug=True)
    app.secret_key = 'hhaahh'
    app.debug = True
    # Session(app)
    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0',5000),app)
    http_server.serve_forever()
