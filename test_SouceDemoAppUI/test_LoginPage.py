import pytest
import requests

from PageObjects.LoginPage import LoginPage


class Test_001_Login:

    @pytest.mark.smoke
    def test_checkPageTitle(self, invokeBrowser):
        driver = invokeBrowser
        login = LoginPage(driver)
        login.goto_url("https://www.saucedemo.com/")
        pageTitle = login.get_title()
        assert  "Swag Labs" == pageTitle

    @pytest.mark.smoke
    def test_loginFunctionality(self, invokeBrowser):
        driver =invokeBrowser
        login = LoginPage(driver)
        login.goto_url("https://www.saucedemo.com/")
        pageTitle = login.loginPageFn("standard_user", "secret_sauce")
        if "Products" == pageTitle:
            assert True

        else:
            #driver.get_screenshot_as_file("..\\Reports\\Screenshots\\test_loginFunctionality.png")
            assert False, "user unsuccessfully login"


    def test_loginWithInvalidCred(self, invokeBrowser):
        driver =invokeBrowser
        login = LoginPage(driver)
        login.goto_url("https://www.saucedemo.com/")
        login.loginPageFn1("standard_", "secret_")
        if "Products" == "Prnboducts":
            assert True

        else:
            #driver.get_screenshot_as_file("..\\Reports\\Screenshots\\loginWithInvalidCred.png")

            assert False, "Invalid User Credentials"


    def test_apiValidation(self):
        response = requests.get("https://automationexercise.com/api/productsList")
        assert response.status_code == 200


    def test_logout(self):
        print("logout")
        print("Syed")
        print("check for auto-trigger jenkins job 2 times")
