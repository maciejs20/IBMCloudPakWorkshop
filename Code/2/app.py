import socket
import math  
from flask import Flask
app = Flask(__name__)

version = "2.0"
host = str(socket.gethostname())

print ("SimpleWebApp {} ready.".format(version))
print ("Hostname: "+host)


@app.route('/')
def hello():
    return ("Hello World from "+str(host))

@app.route('/alive')
def alive():
    return ("Yes, I'm v.{} and alive.".format(version))


@app.route('/version')
def show_version():
    return ("Ver: %s" % (version))

@app.route('/load')
def send_load():
    for x in range(10000):
      for y in range(1000):
        z=x*y-math.sqrt(x)-math.sqrt(y)
    return ("Value: {}.".format(z))

@app.route('/<echo>')
def send_echo(echo):
    return ("{}".format(echo))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
