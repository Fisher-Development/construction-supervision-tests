from pages.base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    """Page Object для страницы входа"""

    URL = "https://construction-supervision.alex-fisher-dev.ru/"
    PROJECTS_URL = "https://construction-supervision.alex-fisher-dev.ru/lk/projects"

    def open(self):
        """Открыть страницу входа"""
        super().open(self.URL)
        return self

    def enter_email(self, email):
        """Ввести email"""
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)
        return self

    def enter_password(self, password):
        """Ввести пароль"""
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)
        return self

    def click_login_button(self):
        """Нажать кнопку входа"""
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        return self

    def has_error_message(self):
        """Проверить наличие сообщения об ошибке"""
        return self.is_element_present(LoginPageLocators.ERROR_MESSAGE)

    def get_error_message_text(self):
        """Получить текст сообщения об ошибке"""
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)

    def is_on_login_page(self):
        """Проверить, что мы на странице входа"""
        current_url = self.get_current_url()
        return current_url == self.URL or current_url.rstrip("/") == self.URL.rstrip(
            "/"
        )

    def is_on_projects_page(self):
        """Проверить, что мы на странице проектов (после успешного входа)"""
        current_url = self.get_current_url()
        return self.PROJECTS_URL in current_url or "/lk/projects" in current_url

    def has_redirected_from_login(self):
        """Проверить, что произошел редирект со страницы входа"""
        return not self.is_on_login_page()

    def is_login_successful(self):
        """Проверить успешность входа по URL"""
        return self.is_on_projects_page()

    def wait_for_redirect(self, timeout=10):
        """Ждать редиректа со страницы входа"""
        self.wait_for_url_change(self.URL, timeout)
        return self

    def wait_for_successful_login(self, timeout=10):
        """Ждать успешного входа (перехода на страницу проектов)"""
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait

        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda driver: "/lk/projects" in driver.current_url)
        return self

    def is_email_field_present(self):
        """Проверить наличие поля email"""
        return self.is_element_present(LoginPageLocators.EMAIL_INPUT)

    def is_password_field_present(self):
        """Проверить наличие поля пароля"""
        return self.is_element_present(LoginPageLocators.PASSWORD_INPUT)

    def is_login_button_present(self):
        """Проверить наличие кнопки входа"""
        return self.is_element_present(LoginPageLocators.LOGIN_BUTTON)

    def are_all_elements_visible(self):
        """Проверить видимость всех основных элементов"""
        return (
            self.is_element_visible(LoginPageLocators.EMAIL_INPUT)
            and self.is_element_visible(LoginPageLocators.PASSWORD_INPUT)
            and self.is_element_visible(LoginPageLocators.LOGIN_BUTTON)
        )

    def login(self, email, password):
        """Выполнить полный процесс входа"""
        self.enter_email(email).enter_password(password).click_login_button()
        return self

    def login_and_wait(self, email, password, timeout=10):
        """Выполнить вход и дождаться успешного перехода"""
        self.login(email, password)
        self.wait_for_successful_login(timeout)
        return self
