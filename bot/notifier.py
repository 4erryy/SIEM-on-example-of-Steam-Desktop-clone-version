import telebot
from bot.config import TOKEN, ADMIN_CHAT_ID

bot = telebot.TeleBot(TOKEN)

class Notifier:
    @staticmethod
    def send_alert(message_text: str):
        """Отправка экстренного уведомления админу в Telegram"""
        try:
            bot.send_message(ADMIN_CHAT_ID, f"⚠️ [ALERT] {message_text}")
            print("[BOT NOTIFIER] Alert sent successfully.")
        except Exception as e:
            print(f"[BOT NOTIFIER] Failed to send alert: {e}")
