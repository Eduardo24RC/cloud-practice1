from flask import Flask,jsonify
import datetime

app = Flask(_name_)

@app.route('/status')
def status():
    return jsonify({
        "service": "demo-cloud",
        "version": "1.0"
        "timestamp":datetime.datetime.utcnow().isoformat() +"z"
    })

    if _name_ == "_main_":
        app.run(host="0.0.0.0", port=8080)