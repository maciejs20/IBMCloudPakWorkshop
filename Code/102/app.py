import socket
import math  
from flask import Flask
app = Flask(__name__)

version = "1.02.0"
host = str(socket.gethostname())

print ("SimpleWebApp {} ready.".format(version))
print ("Hostname: "+host)


@app.route('/')
def hello():
    return ("<H1>Hello my dear Salesman.</H1> <br><p>I'm, Your simple app working on the cluster in the POD named "+str(host)+"</p><p>It's nice that You have installed me!</p><p>I'd appreciate if You won't kill me!")

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
