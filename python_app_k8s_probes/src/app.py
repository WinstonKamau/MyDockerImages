import flask

app = flask.Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/liveness-health-check', methods=['GET'])
def liveness_health_check():
    return "<h1>Liveness Probe</p>"

@app.route('/readiness-health-check', methods=['GET'])
def readiness_health_check():
    return "<h1>Readiness Probe</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8770")