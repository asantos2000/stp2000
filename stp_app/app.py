from flask import Flask, render_template, request, abort, redirect, url_for, make_response
from markupsafe import escape, Markup
from rasp_hw.status import status_report
from rasp_hw.generic_control import change_gpio
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET'])
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
    #resp = make_response(render_template('status.html', component=component))
    resp = status_report()
    return resp

@app.route("/<changePin>/<action>")
def action(changePin, action):
    change_gpio(changePin   , action)
    return redirect(url_for('do_status'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

