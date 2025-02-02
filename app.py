from flask import Flask, request, jsonify
import requests
import threading
import time

app = Flask(__name__)

# Thay thế bằng token bot của bạn
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
# Cập nhật Chat ID
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# Biến lưu trữ số liệu giao dịch
transaction_stats = {
    "total_deposits": 0,
    "total_withdrawals": 0,
    "processing_time": [],
    "balance": 0  # Giả lập số dư hệ thống
}

@app.route('/send_telegram', methods=['POST'])
def send_telegram():
    data = request.get_json()
    message = data.get("message", "No message provided")
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)
    return jsonify({"status": "success", "message": "Notification sent"}), 200

@app.route('/transaction', methods=['POST'])
def record_transaction():
    data = request.get_json()
    transaction_type = data.get("type")
    amount = data.get("amount", 0)
    processing_time = data.get("processing_time", 0)

    if transaction_type == "deposit":
        transaction_stats["total_deposits"] += 1
        transaction_stats["balance"] += amount
    elif transaction_type == "withdrawal":
        transaction_stats["total_withdrawals"] += 1
        transaction_stats["balance"] -= amount

    transaction_stats["processing_time"].append(processing_time)
    return jsonify({"status": "success", "message": "Transaction recorded"}), 200

if __name__ == '__main__':
    app.run(debug=True)
