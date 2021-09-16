# import os
# import glob
# from werkzeug.utils import secure_filename
# from datetime import timedelta
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask,request,redirect,send_file,render_template, session

# UPLOAD_FOLDER = 'uploads/'
# ALLOWED_ENDINGS =   ["txt", "md", "json", "jar",
#                     "png", "jpg", "jpeg", "gif",
#                     "mp3", "wav", "mp4", "avi",
#                     "apk", "pdf", "doc", "docx", "ppt", "pptx",
#                     "zip", "rar", "tar", "iso",
#                     "py", "cpp", "c", "cs", "java"]

# app = Flask(__name__, template_folder='templates')
# app.secret_key = "FQkil92aTY"
# app.permanent_sesion_lifetime = timedelta(days=1)
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':

#         if 'file' not in request.files:
#             print('no file')
#             return redirect(request.url)
#         file = request.files['file']

#         if file.filename == '':
#             print('no filename')
#             return redirect(request.url)
#         else:
#             if check_allowed_ending(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
#                 print("saved file successfully")
#             else:
#                 print("no allowed type")
#                 return redirect(request.url)

#             return redirect('/download')
#     return render_template('upload.html')

# @app.route("/download", methods = ['GET'])
# def download_file():
#     try:
#         l = []
#         for filepath in glob.iglob(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], "*")):
#             path = filepath.split("uploads/")
#             l.append("/"+path[1])
#         return render_template("download.html", files=l)
#     except:
#         print("f")
#         return render_template("download.html", files=[])
#     return render_template('download.html')

# @app.route('/return-files/<filename>')
# def return_files_tut(filename):
#     file_path = UPLOAD_FOLDER + filename
#     return send_file(file_path, as_attachment=True, attachment_filename='')

# @app.route('/delete-files/<filename>')
# def delete_files_tut(filename):
#     # os.remove(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
#     os.remove(f"uploads/{filename}")
#     return redirect("/download")

# if __name__ == "__main__":
#     app.run(debug=True)


import website

app = website.crate_app()

if __name__ == "__main__":
    app.run(debug=True)