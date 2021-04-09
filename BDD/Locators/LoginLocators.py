from selenium.webdriver.common.by import By


class LoginLocators(object):

    LOGIN_USERNAME = (By.ID, 'Login_UserName')
    LOGIN_PASSWORD = (By.ID, 'Login_Password')
    LOGIN_USER_SERVICE = (By.ID, 'Login_UserService')
    LOGIN_BTN_LOGIN = (By.ID, 'Login_btnLogin')