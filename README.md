Проект представляет собой модульную систему мониторинга и автоматизации, предназначенную для отслеживания системных событий и интеграции с внешними сервисами оповещения.

## 🚀 Особенности системы
* Архитектура: Разделение на серверную часть (API) и клиентский агент.
* Автоматизация: Мониторинг файловой системы в режиме реального времени.
* Интеграция: Автоматическая отправка уведомлений о критических событиях в Telegram.
* Безопасность: Изоляция зависимостей через виртуальное окружение.

Этот проект затрагивает вопросы повышение конфиденциальности, защиты и шифрования данных, их утечек в реальном времени (как SIEM мониторинг системы) на примере десктоп приложения Steam (я создал его клон с названием «SteamLab». Составления макета, архитектуры, тактик и способов защиты и атаки на десктоп систему пользователя. Атакующий работает по принципу внедрения вредоносной программы в систему пользователя в скрытном (stealth mode) режиме и далее формирует и отправляет сначала на сервер, а потом через тг бота mafile, который содержит login, pass, 2FA Code, session authorise. 

## 📂 Структура проекта

### Упрощенная:

```text
SteamLabProject/
├── .venv/                    # Окружение
├── requirements.txt          # Зависимости
├── README.md                 # Описание проекта
├── run_system.py             # Единый запуск всех модулей
│
├── agent/                    # СБОРЩИК (Все файлы из скриншота тут)
│   ├── agent.py              # Главный цикл запуска
│   ├── config.py             # Настройки
│   └── ...                   # (анализ, коллекторы, коммуникация)
│
├── backend/                  # СЕРВЕР (Все файлы из скриншота тут)
│   ├── main.py               # FastAPI сервер (точка входа)
│   ├── routes/               # API роуты (api/events.py)
│   ├── db/                   # База данных (database.py)
│   └── ...                   # (сервисы, модели, безопасность)
│
├── bot/                      # УВЕДОМИТЕЛЬ
│   ├── bot.py                # Запуск бота
│   └── notifier.py           # Функция отправки в ТГ
│
└── ui/                       # ИНТЕРФЕЙС
    ├── app.py                # Entry point
    └── ...                   # (QML, активы)
```    

### Полная:

```text
SteamLabProject/ (ROOT)
├── .env                    # Секреты (API_KEY, DB_URL, TG_TOKEN)
├── .gitignore              # Исключения (.venv, data/*, .env, pycache)
├── requirements.txt        # Все зависимости (pip freeze > requirements.txt)
├── run.py                  # Главный контроллер запуска (Subprocess manager)
│
├── agent/                  # МОДУЛЬ СБОРА (Edge Node)
│   ├── __init__.py
│   ├── agent.py            # Точка входа (Main Loop)
│   ├── config.py           # Конфиг агента
│   ├── analysis/           # Логика детекции
│   │   ├── anomaly.py
│   │   └── risk_scorer.py
│   ├── collectors/         # Драйверы чтения
│   │   └── event_collector.py
│   ├── communication/      # Транспорт данных
│   │   └── bridge.py       # API Клиент (POST к бэкенду)
│   ├── core/               # Ядро системы
│   │   ├── engine.py
│   │   └── lifecycle.py
│   ├── integrations/       # Связь со Steam
│   │   └── backend.py
│   ├── monitoring/         # Мониторинг ресурсов
│   │   ├── process_monitor.py
│   │   └── system_monitor.py
│   ├── rules/              # Бизнес-правила агента
│   │   └── rule_engine.py
│   └── utils/              # Помощники
│       ├── helpers.py
│       └── serializer.py
│
├── backend/                # МОДУЛЬ ОБРАБОТКИ (API Gateway)
│   ├── __init__.py
│   ├── main.py             # Точка входа (FastAPI)
│   ├── config.py
│   ├── agent_integration/  # Коннекторы от агентов
│   │   └── agent_connector.py
│   ├── api/                # Роуты API
│   │   └── routes/
│   │       ├── auth.py
│   │       ├── events.py
│   │       ├── security.py
│   │       └── users.py
│   ├── core/               # Оркестрация событий
│   │   ├── event_bus.py
│   │   ├── event_center.py
│   │   └── orchestrator.py
│   ├── db/                 # Слой БД
│   │   └── database.py     # Инициализация и подключение
│   ├── mafiles/            # Хранилище сессий
│   │   └── ...maFile
│   ├── models/             # Схемы данных (Pydantic/SQLAlchemy)
│   │   ├── event.py
│   │   ├── product.py
│   │   ├── session.py
│   │   └── user.py
│   ├── routes/             # Глобальные маршруты
│   │   └── auth.py
│   ├── security/           # Слой безопасности
│   │   ├── default_rules.py
│   │   ├── rule_engine.py
│   │   ├── security_hook.py
│   │   ├── security_processor.py
│   │   └── threat_analyzer.py
│   ├── services/           # Бизнес-сервисы
│   │   ├── audit_service.py
│   │   ├── auth_service.py
│   │   ├── inventory_service.py
│   │   ├── session_service.py
│   │   └── store_service.py
│   └── utils/
│       ├── helpers.py
│       └── main.py
│
├── bot/                    # МОДУЛЬ УВЕДОМЛЕНИЙ
│   ├── bot.py              # Инициализация бота
│   ├── config.py
│   ├── handlers.py         # Команды (/start и т.д.)
│   └── notifier.py         # Функция отправки алертов
│
├── ui/                     # МОДУЛЬ ИНТЕРФЕЙСА
│   ├── assets/             # QML, иконки
│   ├── components/         # Компоненты интерфейса
│   ├── layout/             # Сетки и структуры
│   ├── pages/              # Страницы (Dashboards)
│   ├── views/              # Отрисовка данных
│   └── main.py             # Запуск GUI (PySide6/Streamlit)
│
└── installer/              # СКРИПТЫ ДЕПЛОЯ
    ├── INSTALLER.ps1
    └── setup.ps1
```
    
🛠 Установка и запуск
1. Подготовка окружения
Клонируйте репозиторий и создайте виртуальное окружение:

Bash
python -m venv .venv
# Активация
.venv\Scripts\activate
# Установка зависимостей
pip install -r requirements.txt
2. Запуск Бэкенда
Запустите сервер обработки событий:

Bash
.venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8090
3. Запуск Агента
В отдельном окне терминала запустите скрипт мониторинга:

Bash
.venv\Scripts\python.exe agent/agent.py
⚙️ Конфигурация
Для работы уведомлений в файле agent/agent.py или agent/utils.py необходимо указать ваши данные:

TOKEN: Токен вашего бота (получен у @BotFather).

CHAT_ID: Ваш числовой идентификатор (получен у @userinfobot).

📄 Лицензия
Проект предназначен исключительно для образовательных целей и изучения взаимодействия микросервисов на Python.