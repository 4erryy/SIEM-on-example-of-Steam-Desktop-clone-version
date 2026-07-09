import requests
from bot.config import BACKEND_URL

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        welcome_text = (
            f"🤖 SteamLab Bot активен!\n\n"
            f"👤 Ваш Telegram ID: `{message.chat.id}`\n"
            f"(Скопируйте его и вставьте в bot/config.py вместо 123456789, чтобы получать уведомления)\n\n"
            f"Доступные команды:\n/status - Проверить статус системы"
        )
        bot.reply_to(message, welcome_text, parse_mode="Markdown")

    @bot.message_handler(commands=['status'])
    def check_status(message):
        bot.send_message(message.chat.id, "🔄 Запрашиваю статус у бэкенда...")
        try:
            # Делаем GET запрос к нашему обновленному эндпоинту
            response = requests.get(f"{BACKEND_URL}/check", timeout=3)
            if response.status_code == 418 or response.status_code == 401:
                bot.send_message(message.chat.id, "🟢 Бэкенд онлайн, но требует авторизации (JWT работает исправно).")
            elif response.status_code == 200:
                bot.send_message(message.chat.id, "🟢 Бэкенд онлайн. Доступ открыт.")
            else:
                bot.send_message(message.chat.id, f"🟡 Бэкенд ответил кодом: {response.status_code}")
        except requests.exceptions.RequestException:
            bot.send_message(message.chat.id, "🔴 Не удалось связаться с бэкендом. Убедитесь, что Uvicorn запущен.")
