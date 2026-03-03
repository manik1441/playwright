from pages.login_page import LoginPage


def test_user_login(page):
    # 1. UI Interaction
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
