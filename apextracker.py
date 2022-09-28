import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

# r = requests.get(f"https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{gamertag}", headers=authentication);
#
# icon = r.json()['data']['platformInfo']['avatarUrl'];
# print(icon)

load_dotenv('config.env')

token = os.getenv("TRACKER_API_KEY")
url = os.getenv("TRACKER_API_URL")
authentication = {"TRN-Api-Key": token}

app = Flask(__name__)


@app.route("/")
def opening():
    return render_template('OpeningPage.html')


@app.route("/about/")
def about():
    return render_template('about_page.html')


@app.route("/contact/")
def contact():
    return render_template('contact_page.html')


@app.route("/apexTracker/", methods=["GET", "POST"])
def apexTracker():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        platform = request.form.get('platform')
        gamertag = request.form.get('gtag')
        full_url = f'{url}/profile/{platform}/{gamertag}'
        r = requests.get(full_url, headers=authentication)
        bot = r.json()
        if r.status_code == 200:
            bot = r.json()
            return render_template('main.html', bot=bot)
        else:
            return render_template('main.html')


if __name__ == "__main__":
    app.run(debug='True')
