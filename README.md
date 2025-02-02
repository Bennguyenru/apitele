# Telegram Notification API 🚀

## Mô tả
API gửi thông báo Telegram khi có tin nhắn hoặc sự kiện.

## Cài đặt
```bash
pip install -r requirements.txt
python app.py
```

## Gửi yêu cầu
```bash
curl -X POST http://127.0.0.1:5000/send_telegram      -H "Content-Type: application/json"      -d '{"message": "Test thông báo!"}'
```

## Deploy trên Render
- Kết nối GitHub
- Chọn runtime **Python 3.x**
- Cấu hình Start Command: `gunicorn -b 0.0.0.0:10000 app:app`
