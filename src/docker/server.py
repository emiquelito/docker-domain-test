from flask import Flask

app = Flask(__name__)
app.url_map.host_matching = True


@app.route('/', host='<host>')
def index(host):
    return '<body><a href="/about/">About this page</a><h2 style="text-align: center">Application A</h2></body>'


@app.route('/about/', host='<host>')
def about(host):
    return f'<body>This is the about page for {host}</body>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
