# UI Тесты для Construction Supervision

Автоматизированные UI тесты для веб-приложения Construction Supervision с использованием Selenium WebDriver и паттерна Page Object Model (POM).

## Структура проекта

```markdown:/Users/sergeymac/dev/PG/construction-supervision-tests/README.md
<code_block_to_apply_changes_from>
construction-supervision-tests/
├── docs/                           # Документация
│   └── login_page_ui_tests_action.md
├── pages/                          # Page Object классы
│   ├── base_page.py               # Базовый класс для всех страниц
│   └── login_page.py              # Page Object для страницы входа
├── tests/                          # Тестовые сценарии
│   └── test_login.py              # Тесты для страницы входа
├── locators.py                     # Локаторы элементов
├── conftest.py                     # Конфигурация pytest
├── requirements.txt                # Зависимости Python
└── README.md                       # Этот файл
```

## Установка и настройка

### 1. Создание виртуального окружения

```bash
# Создать виртуальное окружение
python3 -m venv venv

# Активировать виртуальное окружение
source venv/bin/activate  # для macOS/Linux
# или
venv\Scripts\activate     # для Windows
```

### 2. Установка зависимостей

```bash
pip3 install -r requirements.txt
```

### 3. Установка ChromeDriver

ChromeDriver будет установлен автоматически через webdriver-manager при первом запуске тестов.

## Запуск тестов

### Все тесты
```bash
pytest tests/test_login.py -v
```

### Конкретный тест
```bash
pytest tests/test_login.py::TestLogin::test_successful_login -v
```

### С генерацией HTML отчета
```bash
pytest tests/test_login.py -v --html=reports/report.html --self-contained-html
```

### С Allure отчетами
```bash
# Запуск тестов с генерацией Allure данных
pytest tests/test_login.py --alluredir=reports/allure-results

# Генерация и открытие Allure отчета
allure serve reports/allure-results
```

## Тестовые данные

- **URL приложения:** https://construction-supervision.alex-fisher-dev.ru/
- **Тестовые учетные данные:**
  - Email: `test@example.com`
  - Пароль: `password`

## Покрытие тестами

### Страница входа (`test_login.py`)
- ✅ Успешный вход с валидными данными
- ✅ Неуспешный вход с невалидными данными
- ✅ Вход с пустыми полями
- ✅ Проверка наличия элементов на странице
- ✅ Проверка видимости элементов
- ✅ Вход с пустым email
- ✅ Вход с пустым паролем

## Архитектура

### Page Object Model (POM)
Проект использует паттерн Page Object Model для лучшей организации и поддержки тестов:

- **`BasePage`** - базовый класс с общими методами для всех страниц
- **`LoginPage`** - специализированный класс для страницы входа
- **`locators.py`** - централизованное хранение всех локаторов

### Принципы
- Разделение ответственности между классами
- Переиспользование кода через наследование
- Явные ожидания вместо неявных
- Отсутствие try-except в тестовой логике
- Fluent interface для цепочки вызовов

## Конфигурация

### Браузер
Тесты настроены для работы только с Chrome браузером.

### Тайм-ауты
- Неявное ожидание: 10 секунд
- Явное ожидание: 10 секунд (настраивается в методах)

## Разработка

### Добавление новых тестов
1. Создайте новые локаторы в `locators.py`
2. Добавьте методы в соответствующий Page Object класс
3. Напишите тесты в соответствующем файле в папке `tests/`

### Добавление новых страниц
1. Создайте класс локаторов в `locators.py`
2. Создайте Page Object класс, наследующийся от `BasePage`
3. Создайте файл с тестами для новой страницы

## Отчеты

Отчеты сохраняются в папку `reports/`:
- HTML отчеты pytest
- Allure отчеты
- Логи выполнения

## Требования

- Python 3.8+
- Chrome браузер
- Интернет соединение для доступа к тестируемому приложению
```

Теперь у нас есть полная документация по проекту. Для запуска тестов нужно выполнить:

```bash
# 1. Создать и активировать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 2. Установить зависимости
pip3 install -r requirements.txt

# 3. Запустить тесты
pytest tests/test_login.py -v
```

Структура проекта теперь полностью готова к работе с правильной архитектурой POM, вынесенными локаторами и подробной документацией!
