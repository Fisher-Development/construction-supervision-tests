import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


@pytest.fixture
def driver():
    """Фикстура для создания Chrome WebDriver"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # Для CI/CD
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для прикрепления скриншотов и логов при падении тестов"""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Прикрепляем скриншот
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Скриншот_при_ошибке_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                attachment_type=allure.attachment_type.PNG,
            )

            # Прикрепляем текущий URL
            allure.attach(
                driver.current_url,
                name="URL при ошибке",
                attachment_type=allure.attachment_type.TEXT,
            )

            # Прикрепляем HTML страницы
            allure.attach(
                driver.page_source,
                name="HTML страницы",
                attachment_type=allure.attachment_type.HTML,
            )
