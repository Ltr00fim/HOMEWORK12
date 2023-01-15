from flask import Flask, request, render_template, send_from_directory, url_for
from functions import *

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route("/")
def page_index():
    print(url_for('page_index'))
    return render_template('index.html')


@app.route("/list/", methods=["POST"])
def page_tag():
    if len(search_by_name(request.form["name_of_post"])) >= 1:
        print(url_for('page_tag'))
        return render_template('post_list.html', posts=search_by_name(request.form["name_of_post"]), task=request.form["name_of_post"])
    else:
        print(url_for('page_tag'))
        return render_template('none.html', task=request.form["name_of_post"])


@app.route("/post/")
def page_post_form():
    print(url_for('page_post_form'))
    return render_template('post_form.html')


@app.route("/upload", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    filename = picture.filename
    if is_filename_allowed(filename):
        picture.save(f"./static/images/{filename}")
        write_in_json({'pic': f"/static/images/{filename}", "content": request.form['content']})
        print(url_for('page_post_upload'))
        return render_template('post_uploaded.html', pic=filename, text=request.form['content'])
    else:
        extension = filename.split(".")[-1]
        print(url_for('page_post_upload'))
        return render_template("error.file.html", text=f"Тип файлов {extension} не поддерживается")


@app.errorhandler(413)
def page_not_found(e):
    print(url_for('page_not_found'))
    return render_template("error.file.html", text="Файл слишком большой")


app.run()
