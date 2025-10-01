# UI Тесты Страницы Входа - План Реализации

## Требования

### Цель
Создать автоматизированные UI тесты для страницы входа веб-приложения https://construction-supervision.alex-fisher-dev.ru/ с использованием паттерна Page Object Model (POM).

### Функциональные требования
1. **Тестирование элементов страницы входа:**
   - Поле ввода логина
   - Поле ввода пароля  
   - Кнопка входа
   - Проверка валидации полей
   - Сообщения об ошибках

2. **Сценарии тестирования:**
   - Успешная авторизация с валидными данными
   - Неуспешная авторизация с невалидными данными
   - Проверка обязательности заполнения полей
   - Проверка отображения ошибок валидации
   - Проверка редиректа после успешного входа

### Технические требования
- Использование Selenium WebDriver
- Паттерн Page Object Model (POM)
- Фреймворк pytest для тестов
- Allure для отчетности
- **Поддержка только Chrome браузера**
- Конфигурация через переменные окружения

### Тестовые данные
- **Валидные учетные данные:**
  - Email: `test@example.com`
  - Пароль: `password`

## План Реализации

### Этап 1: Структура проекта
```
construction-supervision-tests/
├── docs/
│   └── login_page_ui_tests_action.md
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── ui/
│       ├── __init__.py
│       ├── pages/
│       │   ├── __init__.py
│       │   ├── base_page.py
│       │   └── login_page.py
│       └── test_login.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── utils/
│   ├── __init__.py
│   └── driver_factory.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### Этап 2: Базовые компоненты

#### 2.1 Базовый класс страницы (base_page.py)
- Общие методы для всех страниц
- Ожидания элементов
- Базовые действия (клик, ввод текста, получение текста)

#### 2.2 Фабрика драйверов (driver_factory.py)
- Создание Chrome WebDriver
- Настройка опций Chrome браузера
- Управление жизненным циклом драйвера

#### 2.3 Конфигурация (settings.py)
- URL приложения: `https://construction-supervision.alex-fisher-dev.ru/`
- Настройки Chrome браузера
- Тайм-ауты
- Тестовые данные

### Этап 3: Page Object для страницы входа

#### 3.1 Класс LoginPage
- Локаторы элементов страницы входа
- Методы взаимодействия с элементами:
  - `open()` - открытие страницы
  - `enter_username(username)` - ввод логина
  - `enter_password(password)` - ввод пароля
  - `click_login_button()` - нажатие кнопки входа
  - `get_error_message()` - получение сообщения об ошибке
  - `is_login_successful()` - проверка успешного входа

### Этап 4: Тестовые сценарии

#### 4.1 Позитивные тесты
- `test_successful_login_with_valid_credentials` - тест с `test@example.com` / `password`
- `test_login_page_elements_visibility`

#### 4.2 Негативные тесты
- `test_login_with_invalid_credentials`
- `test_login_with_empty_username`
- `test_login_with_empty_password`
- `test_login_with_empty_fields`

#### 4.3 Тесты валидации
- `test_username_field_validation`
- `test_password_field_validation`
- `test_error_messages_display`

### Этап 5: Конфигурация тестов

#### 5.1 Conftest.py
- Фикстуры для Chrome WebDriver
- Настройка Chrome браузера
- Скриншоты при падении тестов
- Allure attachments

#### 5.2 Переменные окружения
- BASE_URL=https://construction-supervision.alex-fisher-dev.ru/
- BROWSER_TYPE=chrome
- IMPLICIT_WAIT=10
- EXPLICIT_WAIT=20
- TEST_USERNAME=test@example.com
- TEST_PASSWORD=password

### Этап 6: Отчетность
- Настройка Allure отчетов
- Интеграция с pytest-html
- Скриншоты при падении тестов

## Ожидаемые результаты

1. **Готовая структура проекта** с разделением на логические компоненты
2. **Page Object класс** для страницы входа с полным покрытием элементов
3. **Набор автоматизированных тестов** покрывающих основные сценарии
4. **Конфигурация** для запуска тестов только в Chrome
5. **Отчеты** с детальной информацией о результатах тестирования

## Следующие шаги

После реализации тестов для страницы входа, можно будет расширить покрытие на другие страницы приложения, используя созданную архитектуру как основу.

## УТВЕРЖДЕНО

✅ **Браузер:** Только Chrome  
✅ **Тестовые данные:** test@example.com / password  
✅ **URL:** https://construction-supervision.alex-fisher-dev.ru/  

**ГОТОВ К РЕАЛИЗАЦИИ**

Отлично! План обновлен с учетом ваших требований:

- **Браузер:** Только Chrome
- **Тестовые данные:** test@example.com / password
- **Фокус:** Страница входа с полным покрытием сценариев

План готов к реализации. Можно приступать к созданию структуры проекта и написанию кода?

**ОДОБРЯЕТЕ ПЛАН ДЛЯ ПЕРЕХОДА К РЕАЛИЗАЦИИ?**
