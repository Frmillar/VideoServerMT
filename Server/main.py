from flask import Flask, stream_with_context, request, Response

import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "Video Server"

#HD video using pure Flask
@app.route('/HQ')
def stream_data_HQ():
    def generate():
        file_path = os.path.dirname(os.path.abspath(__file__)) + "/HQ.mp4"
        file_size = os.stat(file_path).st_size
        start = 0
        length = file_size - start
        with open(file_path, "rb") as f:
            f.seek(start)
            chunk = f.read(length)
            yield chunk
    return Response(stream_with_context(generate()), mimetype="video/mp4")

#HD video using pure Flask
@app.route('/HD')
def stream_data_HD():
    def generate():
        file_path = os.path.dirname(os.path.abspath(__file__)) + "/HD.mp4"
        file_size = os.stat(file_path).st_size
        start = 0
        length = file_size - start
        with open(file_path, "rb") as f:
            f.seek(start)
            chunk = f.read(length)
            yield chunk
    return Response(stream_with_context(generate()), mimetype="video/mp4")

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)
