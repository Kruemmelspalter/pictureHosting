import flask, os
app = flask.Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static'

from werkzeug import secure_filename

@app.route('/')
@app.route('/index')
@app.route('/upload', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('upload.html')
    elif flask.request.method == 'POST':
        f = flask.request.files['file']
        fname = secure_filename((flask.request.form.get('fname') if flask.request.form.get('fname')!="" else f.filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
        return 'File uploaded successful <a href="static/'+fname+'">here</a>'


if __name__ == "__main__":
    app.run(port=80)