from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    status = "Unknown"
    details = ""

    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            status = "✅ Google is reachable"
        else:
            status = "⚠️ Google responded with error"
            details = f"Status code: {response.status_code}"
    except requests.ConnectionError:
        status = "❌ Google is unreachable"
        details = "Connection error"
    except requests.Timeout:
        status = "❌ Google is unreachable"
        details = "Request timed out"
    except Exception as e:
        status = "❌ Google is unreachable"
        details = str(e)

    return render_template("index.html", status=status, details=details)

if __name__ == '__main__':
    app.run(debug=True)
