from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file
from . import db, ALLOWED_ENDINGS, UPLOAD_FOLDER
import os, glob
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, logout_user, current_user

files = Blueprint("files", __name__)

def check_allowed_ending(file):
    try:
        filename = file.lower()
        end = str(filename).split(".")
        if end[1] in ALLOWED_ENDINGS:
            return True
        else:
            return False
    except:
        print("err")
        return False

@files.route("/")
def home():
    return render_template("index.html")

@files.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            if check_allowed_ending(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(files.root_path, UPLOAD_FOLDER, filename))
                print("saved file successfully")
            else:
                print("no allowed type")
                return redirect(request.url)

            return redirect('/download')
    return render_template('upload.html')

@files.route("/download", methods = ['GET'])
def download_file():
    try:
        l = []
        for filepath in glob.iglob(os.path.join(files.root_path, UPLOAD_FOLDER, "*")):
            path = filepath.split("uploads/")
            l.append("/"+path[1])
        return render_template("download.html", files=l)
    except:
        print("f")
        return render_template("download.html", files=[])

@files.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')

@files.route('/delete-files/<filename>')
def delete_files_tut(filename):
    os.remove(os.path.join(files.root_path, UPLOAD_FOLDER, filename))
    # os.remove(f"uploads/{filename}")
    return redirect("/download")