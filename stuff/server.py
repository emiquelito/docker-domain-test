import os
from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.config['SERVER_NAME'] = os.getenv('SQUASH_DOMAIN', 'localhost')


@app.route('/')
def index():
    domain = os.getenv('SQUASH_DOMAIN', 'localhost')
    return f'<body>Hello world. <a href="//static.{domain}/">Static page</a>.</body>'


@app.route('/', subdomain='<subdomain>')
def sub_index(subdomain):
    if subdomain == 'static':
        return render_template('static.html')
    context = {
        'user': subdomain,
    }
    try:
        return render_template('index.html', **context)
    except TemplateNotFound:
        abort(404)


@app.route('/about/', subdomain='<subdomain>')
def about(subdomain):
    context = {
        'user': subdomain,
    }
    try:
        return render_template('about.html', **context)
    except TemplateNotFound:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
