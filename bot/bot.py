import time
import sys


def start_bot():
    print("[ БОТ ]: Инициализация тестовой платформы...")
    print("[ БОТ ]: Платформа успешно запущена на порту 8080 (Mock-режим) и ожидает координатора.")

    # Бесконечный цикл, чтобы процесс не закрывался мгновенно
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[ БОТ ]: Сервер остановлен.")
        sys.exit(0)


if __name__ == "__main__":
    start_bot()