from .base_page import BasePage
class LoginPage(BasePage):
    EMAIL = "input[type=email]"
    PASSWORD = "input[type=password]"
    SUBMIT = "button[type=submit]"
