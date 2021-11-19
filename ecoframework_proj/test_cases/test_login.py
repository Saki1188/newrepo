import pytest
from selenium import webdriver
from page_objects.login_page import login

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin@yourstore.com"

    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Your store. Login":
            assert true
        else:
            assert false

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)#created an object for login_page to access methods
        self.lp.setUserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        self.driver.close
        if act_title=="Your store. Login":
            assert true
        else:
            assert false


