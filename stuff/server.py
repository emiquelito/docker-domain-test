from flask import Flask

app = Flask(__name__)
app.url_map.host_matching = True


@app.route('/', host='<host>')
def index(host):
    if 'deployrun.com' in host:
        return '<body><h2>It is flask domain-specific page.</h2></body>'
    return '<body><link href="/mobile-icon-57.png">Hello world. <a href="/about/">About this page</a>. <img src="/some.png" /></body>'


@app.route('/about/', host='<host>')
def about(host):
    return '<body>This is the about page</body>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
