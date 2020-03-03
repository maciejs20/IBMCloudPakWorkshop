from flask import Flask
app = Flask(__name__)

version = "1.0"
print ("SimpleWebApp {} ready.".format(version))


@app.route('/')
def hello():
    return ("Hello World!")


@app.route('/alive')
def alive():
    return ("Yes, I'm v.{} and alive.".format(version))


@app.route('/version')
def show_version():
    return ("Ver: %s" % (version))


@app.route('/<echo>')
def send_echo(echo):
    return ("{}".format(echo))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
