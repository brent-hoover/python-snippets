from flask import Flask
from flask import render_template
from walkdir import filtered_walk, file_paths

app = Flask(__name__)


def index_podcasts():
    files = file_paths(filtered_walk('static/podcasts', included_files=['*.mp3'], ))
    return files


def index_videos():
    files = file_paths(filtered_walk('static/podcasts', included_files=['*.mp4'], ))
    return files


@app.route('/directory', methods=['GET', 'POST'])
def directory():
    pass

@app.route('/')
def index():
    filenames = index_podcasts()
    videos = index_videos()
    return render_template('index.html', filenames=filenames, videos=videos)


@app.route('/video/<path:filename>')
def video(filename=None):
    return render_template('video.html', filename=filename)


@app.route('/audio/<path:filename>')
def audio(filename=None):
    return render_template('audio.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
