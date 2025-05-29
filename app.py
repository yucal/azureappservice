from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/check_google')
def check_google():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            return jsonify(status="Google is reachable", code=200)
        else:
            return jsonify(status="Google responded with error", code=response.status_code)
    except requests.ConnectionError:
        return jsonify(status="Google is unreachable", error="Connection error")
    except requests.Timeout:
        return jsonify(status="Google is unreachable", error="Request timed out")
    except Exception as e:
        return jsonify(status="Google is unreachable", error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
