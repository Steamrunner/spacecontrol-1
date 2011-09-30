from flask import Flask, Response, request, render_template, g
from spacecontrol import SpaceControl

SERIAL_PORT = "/dev/tty.usbserial-A6008cOY"
ABOUT_RATE = 2400

app = Flask(__name__)
app.debug = True

@app.before_request
def before_request():
    g.space_control = SpaceControl(SERIAL_PORT, ABOUT_RATE)

@app.after_request
def after_request(response):
    g.space_control.close()
    return response

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/api/button/<int:id>')
def button(id):
    g.space_control.button(id)
    return 'OK'

@app.route('/api/switch_on/<int:id>')
def switch_on(id):
    g.space_control.switch(id, True)
    return 'OK'

@app.route('/api/switch_off/<int:id>')
def switch_off(id):
    g.space_control.switch(id, False)
    return 'OK'

@app.route('/api/switch_all_on')
def switch_all_on():
    g.space_control.switch(3, True)
    g.space_control.switch(4, True)
    g.space_control.switch(5, True)
    return 'OK'

@app.route('/api/switch_all_off')
def switch_all_off():
    g.space_control.switch(3, False)
    g.space_control.switch(4, False)
    g.space_control.switch(5, False)
    return 'OK'

@app.route('/hostname.js')
def hostname():
    return Response('HOSTNAME = "%s";' % request.host, mimetype='application/javascript');

if __name__ == '__main__':
    app.run('0.0.0.0', 5555)
