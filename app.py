from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def check_google():
    try:
        response = requests.get('https://healthchecks-aag9emhhg3efadcy.germanywestcentral-01.azurewebsites.net', timeout=5)
        if response.status_code == 200:
            return 'Google is up!', 200
        else:
            return f'Google returned status code {response.status_code}', 503
    except requests.RequestException as e:
        return f'Google is not reachable: {e}', 503

if __name__ == '__main__':
    app.run()
