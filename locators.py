from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы для страницы входа"""

    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'], input[name='email'], #email")
    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "input[type='password'], input[name='password'], #password",
    )
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button[type='submit'], input[type='submit'], .login-btn, #login",
    )
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error, .alert-danger, .error-message")


class BasePageLocators:
    """Общие локаторы для всех страниц"""

    LOADING_SPINNER = (By.CSS_SELECTOR, ".spinner, .loading, .loader")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success, .success-message")
    ALERT_ERROR = (By.CSS_SELECTOR, ".alert-danger, .error-message")
    MODAL_DIALOG = (By.CSS_SELECTOR, ".modal, .dialog")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".close, .btn-close, [aria-label='Close']")


# В будущем можно добавить локаторы для других страниц
class DashboardPageLocators:
    """Локаторы для главной страницы (пример для будущего расширения)"""

    USER_MENU = (By.CSS_SELECTOR, ".user-menu, .profile-dropdown")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".logout, #logout")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, ".welcome, .greeting")


class NavigationLocators:
    """Локаторы для навигации"""

    MAIN_MENU = (By.CSS_SELECTOR, ".main-menu, .navbar")
    HOME_LINK = (By.CSS_SELECTOR, ".home-link, [href='/']")
    PROFILE_LINK = (By.CSS_SELECTOR, ".profile-link, [href*='profile']")
