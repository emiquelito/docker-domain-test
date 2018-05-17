from flask import Flask, abort

app = Flask(__name__)
app.url_map.host_matching = True
allowed_domains = ['squash.io', 'deployrun.com']


@app.route('/', host='<host>')
def index(host):
    for domain in allowed_domains:
        if domain in host:
            return f'<body><h3 style="margin-top: 10%;"><ul><li>Application B</li><li>something</li></ul></h3></body>'
    abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
