import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BasePageLocators


class BasePage:
    """Базовый класс для всех Page Object"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        """Открыть указанную страницу"""
        self.driver.get(url)
        return self

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        """Найти элемент с ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Найти все элементы по локатору"""
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу")
    def click_element(self, locator):
        """Кликнуть по элементу с ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    @allure.step("Ввести текст в поле")
    def enter_text(self, locator, text):
        """Ввести текст в поле с предварительной очисткой"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        """Проверить наличие элемента на странице"""
        elements = self.find_elements(locator)
        return len(elements) > 0

    def is_element_visible(self, locator):
        """Проверить видимость элемента"""
        element = self.find_element(locator)
        return element.is_displayed()

    @allure.step("Ждать появления элемента")
    def wait_for_element_visible(self, locator, timeout=10):
        """Ждать появления видимого элемента"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=10):
        """Ждать, пока элемент станет кликабельным"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ждать изменения URL")
    def wait_for_url_change(self, current_url, timeout=10):
        """Ждать изменения URL"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: driver.current_url != current_url)
        return self

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def get_page_title(self):
        """Получить заголовок страницы"""
        return self.driver.title

    # Методы для работы с общими элементами
    def has_loading_spinner(self):
        """Проверить наличие спиннера загрузки"""
        return self.is_element_present(BasePageLocators.LOADING_SPINNER)

    @allure.step("Ждать завершения загрузки")
    def wait_for_loading_complete(self, timeout=10):
        """Ждать завершения загрузки (исчезновения спиннера)"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until_not(EC.presence_of_element_located(BasePageLocators.LOADING_SPINNER))
        return self

    def has_success_alert(self):
        """Проверить наличие сообщения об успехе"""
        return self.is_element_present(BasePageLocators.ALERT_SUCCESS)

    def has_error_alert(self):
        """Проверить наличие сообщения об ошибке"""
        return self.is_element_present(BasePageLocators.ALERT_ERROR)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрыть модальное окно"""
        if self.is_element_present(BasePageLocators.MODAL_DIALOG):
            self.click_element(BasePageLocators.CLOSE_BUTTON)
        return self
