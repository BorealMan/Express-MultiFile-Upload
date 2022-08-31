from flask import Flask, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "mmdf98309sfmdlfsdnfiudunfd"
# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['png', "webp"])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return '''
    <html>
        <head>
            <title>Upload Imgs App</title>
            <style>
                h1 {
                    font-size:2.5rem;
                    font-family: "Arial";
                    text-align:center;
                }
                #Image_Form {
                    display:flex;
                    flex-direction:column;
                    gap:1rem;
                    font-size:1.25rem;
                    padding: .5rem;
                    width:fit-content;
                    margin-left:auto;
                    margin-right:auto;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the test site!</h1>

            <form id="Image_Form" method='POST' name="Image_Form" action="/submit" enctype="multipart/form-data">
                <label>Please Upload Your Images:</label>
                <input name="images" type="file" webkitdirectory directory multiple></input>
                <input type="submit"></input>
            </form>
        </body>
    </html>
    '''



@app.route("/submit", methods=["POST"])
def post():
    images = request.files.getlist("images")
    print(images)

    for img in images:
        if img and allowed_file(img.filename):
            filename = secure_filename(img.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return '''
        <html>
            <head>
                <title>Upload Imgs App</title>
            </head>
            <body>
                <h2>Request Recieved.</h2>     
            </body>
        </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)