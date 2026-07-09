import requests
try:
    response = requests.post("http://127.0.0.1:8090/event", json={"test": "data"}, timeout=5)
    print(f"Статус ответа: {response.status_code}")
except Exception as e:
    print(f"Ошибка: {e}")