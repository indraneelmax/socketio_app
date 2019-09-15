from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, static_url_path = "")
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('my event')
def handle_message(message):
    print('received on server my event: ', message)

@socketio.on('ping_event')
def handle_ping(message):
    print('Ping received on server: ', message)


@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
    print "Runnning...."
