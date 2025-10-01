import allure
from pages.login_page import LoginPage


@allure.epic("Аутентификация")
@allure.feature("Страница входа")
class TestLogin:
    """Тесты для страницы входа"""

    @allure.story("Успешный вход")
    @allure.title("Вход с валидными учетными данными")
    @allure.description("Проверка успешного входа пользователя с корректными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login(self, driver):
        """Тест успешного входа с валидными данными"""
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу входа и выполнить вход"):
            login_page.open().login("test@example.com", "password")

        with allure.step("Проверить успешный вход и переход на страницу проектов"):
            login_page.wait_for_successful_login()
            assert (
                login_page.is_login_successful()
            ), "Переход на страницу проектов не произошел"
            assert login_page.is_on_projects_page(), "Не находимся на странице проектов"

    @allure.story("Успешный вход")
    @allure.title("Проверка URL после успешного входа")
    @allure.description("Проверка корректности URL после успешной аутентификации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_login_url_check(self, driver):
        """Тест проверки URL после успешного входа"""
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу входа и выполнить вход"):
            login_page.open().login_and_wait("test@example.com", "password")

        with allure.step("Проверить корректность URL"):
            current_url = login_page.get_current_url()
            allure.attach(current_url, "Текущий URL", allure.attachment_type.TEXT)
            assert (
                "/lk/projects" in current_url
            ), f"Ожидался URL с '/lk/projects', получен: {current_url}"

    @allure.story("Негативные сценарии")
    @allure.title("Вход с неверными учетными данными")
    @allure.description(
        "Проверка что система не пропускает пользователя с неверными данными"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_with_invalid_credentials(self, driver):
        """Тест входа с неверными данными"""
        login_page = LoginPage(driver)

        with allure.step("Попытка входа с неверными данными"):
            login_page.open().login("wrong@example.com", "wrongpassword")

        with allure.step("Проверить что вход не выполнен"):
            assert (
                login_page.is_on_login_page() or login_page.has_error_message()
            ), "Должны остаться на странице входа или увидеть ошибку"

    @allure.story("Валидация полей")
    @allure.title("Вход с пустыми полями")
    @allure.description("Проверка что система требует заполнения всех полей")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_fields(self, driver):
        """Тест входа с пустыми полями"""
        login_page = LoginPage(driver)

        with allure.step("Попытка входа без заполнения полей"):
            login_page.open().click_login_button()

        with allure.step("Проверить что остались на странице входа"):
            assert (
                login_page.is_on_login_page()
            ), "Должны остаться на странице входа с пустыми полями"

    @allure.story("Проверка элементов интерфейса")
    @allure.title("Наличие элементов на странице входа")
    @allure.description(
        "Проверка что все необходимые элементы присутствуют на странице"
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_page_elements_present(self, driver):
        """Тест наличия элементов на странице входа"""
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу входа"):
            login_page.open()

        with allure.step("Проверить наличие основных элементов"):
            assert (
                login_page.is_email_field_present()
            ), "Поле email не найдено на странице"
            assert (
                login_page.is_password_field_present()
            ), "Поле пароля не найдено на странице"
            assert (
                login_page.is_login_button_present()
            ), "Кнопка входа не найдена на странице"

    @allure.story("Проверка элементов интерфейса")
    @allure.title("Видимость элементов на странице входа")
    @allure.description("Проверка что все элементы видимы пользователю")
    @allure.severity(allure.severity_level.MINOR)
    def test_login_page_elements_visible(self, driver):
        """Тест видимости элементов на странице входа"""
        login_page = LoginPage(driver)

        with allure.step("Открыть страницу входа"):
            login_page.open()

        with allure.step("Проверить видимость всех элементов"):
            assert (
                login_page.are_all_elements_visible()
            ), "Не все элементы страницы видимы"

    @allure.story("Валидация полей")
    @allure.title("Вход с пустым email")
    @allure.description("Проверка валидации при отсутствии email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_email(self, driver):
        """Тест входа с пустым email"""
        login_page = LoginPage(driver)

        with allure.step("Ввести только пароль без email"):
            login_page.open().enter_password("password").click_login_button()

        with allure.step("Проверить что остались на странице входа"):
            assert (
                login_page.is_on_login_page()
            ), "Должны остаться на странице входа с пустым email"

    @allure.story("Валидация полей")
    @allure.title("Вход с пустым паролем")
    @allure.description("Проверка валидации при отсутствии пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_with_empty_password(self, driver):
        """Тест входа с пустым паролем"""
        login_page = LoginPage(driver)

        with allure.step("Ввести только email без пароля"):
            login_page.open().enter_email("test@example.com").click_login_button()

        with allure.step("Проверить что остались на странице входа"):
            assert (
                login_page.is_on_login_page()
            ), "Должны остаться на странице входа с пустым паролем"
