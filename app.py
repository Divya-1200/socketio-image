from flask import Flask,render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)


app.config["SECRET_KEY"] = "SECRET_KEY"
socketio = SocketIO(app)


@app.route("/",methods=['GET','POST'])
def header():
    return render_template('index.html')

@app.route("/display",methods=['GET','POST'])
def display():
    return render_template('display.html')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET','POST']):
    #print('received my event: ' + str(json))
    socketio.emit('my response', json,broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)