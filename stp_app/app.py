from flask import Flask, render_template, request, abort, redirect, url_for, make_response
from markupsafe import escape, Markup
from time import sleep

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/<name>', methods=['GET'])
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/led/<command>', methods=['GET'])
def do_led(command):
    return 'led %s' % escape(command)

@app.route('/servo/<command>', methods=['GET'])
def do_servo(command):
    return 'servo %s' % escape(command)

@app.route('/sound/<command>', methods=['GET'])
def do_sound(command):
    return 'sound %s' % escape(command)

@app.route('/test/<command>', methods=['GET'])
def do_test(command):
    except_list = request.args.get('except-list', '')
    return 'test %s, request method: %s, except-list: %s' % (escape(command), request.method, except_list)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error=error), 404

@app.route('/status/')
@app.route('/status/<component>', methods=['GET'])
def do_status(component=None):
    resp = make_response(render_template('status.html', component=component))
    return resp
    return 'status %s' % escape(command)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

