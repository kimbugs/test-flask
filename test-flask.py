import os
from flask import Flask, jsonify, request, render_template, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

upload_folder = "uploads/"
if not os.path.exists(upload_folder):
    os.mkdir(upload_folder)

app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'name': 'kimbugs',
        'email': 'kimbugs@naver.com'
    })

@app.route('/update', methods=['GET'])
def file_send():
    #return request.args.to_dict()
    return send_file('firmware.bin')

# File upload rendering
@app.route('/upload')
def file_render():
    return render_template('upload.html')

# File upload
@app.route('/fileUpload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(file.filename)))
        return 'upload'

if __name__== '__main__':
    app.run(host='0.0.0.0', port=5000)