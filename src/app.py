from flask import Flask, jsonify , render_template
import socket

app= Flask(__name__)

def fetchDeatils():
    host_name=socket.gethostname()
    host_ip=socker.gethostbyname(host_name)
    return host_name, host_ip

@app.route("/")
def hello_world():
    return "<p>Hey , how you doin</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
