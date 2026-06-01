from flask import Flask, request, jsonify
from flask_cors import CORS
import telebot

app = Flask(__name__)
CORS(app)

# --- إعدادات البوت ---
# استبدل هذا التوكن بآخر جديد بعد عمل Revoke
TELEGRAM_TOKEN = '8144607793:AAGwp6n8rbXx5O-rjI3x_tP56A3C2wIN1kw' 
CHAT_ID = '7977532794'
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        user = data.get('name')
        action = data.get('action')
        
        # إرسال الرسالة لتلجرام
        msg = f"🔔 تنبيه أمني:\nالمستهدف: {user}\nالإجراء: {action}"
        bot.send_message(CHAT_ID, msg)
        
        return jsonify({"message": "تم إرسال التنبيه بنجاح!"})
    except Exception as e:
        return jsonify({"message": f"خطأ: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
