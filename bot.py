from flask import Flask, request
import requests

TOKEN = "8518569191:AAExB-GrI5JWXin4Gli-ihgix7riiwnRKrk"
API_URL = f"https://api.telegram.org/bot{TOKEN}"

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text == "/start":
        send_message(chat_id, "✅ البوت شغال على Render")
    else:
        send_message(chat_id, f"📩 وصلت: {text}")

    return "OK"

def send_message(chat_id, text):
    requests.post(f"{API_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })
