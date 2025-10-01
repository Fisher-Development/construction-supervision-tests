from pages.login_page import LoginPage


class TestLogin:
    """Тесты для страницы входа"""

    def test_successful_login(self, driver):
        """Тест успешного входа с валидными данными"""
        login_page = LoginPage(driver)

        # Открываем страницу входа и выполняем вход
        login_page.open().login("test@example.com", "password")

        # Ждем успешного входа и проверяем переход на страницу проектов
        login_page.wait_for_successful_login()
        assert (
            login_page.is_login_successful()
        ), "Переход на страницу проектов не произошел"
        assert login_page.is_on_projects_page(), "Не находимся на странице проектов"

    def test_successful_login_url_check(self, driver):
        """Тест проверки URL после успешного входа"""
        login_page = LoginPage(driver)

        # Открываем страницу входа и выполняем вход
        login_page.open().login_and_wait("test@example.com", "password")

        # Проверяем конкретный URL
        current_url = login_page.get_current_url()
        assert (
            "/lk/projects" in current_url
        ), f"Ожидался URL с '/lk/projects', получен: {current_url}"

    def test_login_with_invalid_credentials(self, driver):
        """Тест входа с неверными данными"""
        login_page = LoginPage(driver)

        # Открываем страницу входа и пытаемся войти с неверными данными
        login_page.open().login("wrong@example.com", "wrongpassword")

        # Проверяем, что остались на странице входа или появилась ошибка
        assert (
            login_page.is_on_login_page() or login_page.has_error_message()
        ), "Должны остаться на странице входа или увидеть ошибку"

    def test_login_with_empty_fields(self, driver):
        """Тест входа с пустыми полями"""
        login_page = LoginPage(driver)

        # Открываем страницу входа и пытаемся войти без данных
        login_page.open().click_login_button()

        # Проверяем, что остались на странице входа
        assert (
            login_page.is_on_login_page()
        ), "Должны остаться на странице входа с пустыми полями"

    def test_login_page_elements_present(self, driver):
        """Тест наличия элементов на странице входа"""
        login_page = LoginPage(driver)

        # Открываем страницу входа
        login_page.open()

        # Проверяем наличие основных элементов
        assert login_page.is_email_field_present(), "Поле email не найдено на странице"
        assert (
            login_page.is_password_field_present()
        ), "Поле пароля не найдено на странице"
        assert (
            login_page.is_login_button_present()
        ), "Кнопка входа не найдена на странице"

    def test_login_page_elements_visible(self, driver):
        """Тест видимости элементов на странице входа"""
        login_page = LoginPage(driver)

        # Открываем страницу входа
        login_page.open()

        # Проверяем видимость всех элементов
        assert login_page.are_all_elements_visible(), "Не все элементы страницы видимы"

    def test_login_with_empty_email(self, driver):
        """Тест входа с пустым email"""
        login_page = LoginPage(driver)

        # Открываем страницу входа и вводим только пароль
        login_page.open().enter_password("password").click_login_button()

        # Проверяем, что остались на странице входа
        assert (
            login_page.is_on_login_page()
        ), "Должны остаться на странице входа с пустым email"

    def test_login_with_empty_password(self, driver):
        """Тест входа с пустым паролем"""
        login_page = LoginPage(driver)

        # Открываем страницу входа и вводим только email
        login_page.open().enter_email("test@example.com").click_login_button()

        # Проверяем, что остались на странице входа
        assert (
            login_page.is_on_login_page()
        ), "Должны остаться на странице входа с пустым паролем"
