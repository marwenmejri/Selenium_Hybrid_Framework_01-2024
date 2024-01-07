import time
import pytest

from pagesObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logger


class Test001Login:
    baseURL = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = Logger.sample_logger()

    def test_verify_login_page(self, setup):
        self.logger.info("************** Test001Login started !! *************")
        self.logger.info("************** Verifying Login Page Test started !! *************")
        driver = setup
        driver.get(url=self.baseURL)
        # Act
        actual_title = driver.title
        # Assert
        if actual_title == "Your store. Login":
            self.logger.info("************** Verifying Login Page Test Passed *************")
            # Cleanup
            driver.quit()
            assert True
        else:
            self.logger.error("************** Verifying Login Page Test Failed !!! *************")
            driver.save_screenshot(filename='Screenshots/verify_login_page.png')
            # Cleanup
            driver.quit()
            assert False

    def test_login_page(self, setup):
        self.logger.info("************** Login Test started !! *************")
        driver = setup
        driver.get(url=self.baseURL)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)
        if driver.title == "Dashboard / nopCommerce administration":
            self.logger.info("************** Login Test Passed *************")
            assert True
            lp.logout()
            driver.quit()
        else:
            self.logger.error("************** Login Test Failed ! *************")
            driver.save_screenshot(filename='Screenshots/login.png')
            driver.quit()
            assert False

    def test_verify_login_page1(self, setup):
        self.logger.info("************** Verifying Login Page Test 1 started !*************")
        driver = setup
        driver.get(url=self.baseURL)
        # Act
        actual_title = driver.title
        # Assert
        if actual_title == "Your store. Login":
            self.logger.info("************** Verifying Login Page Test 1 Passed *************")
            # Cleanup
            driver.quit()
            assert True
        else:
            self.logger.error("************** Verifying Login Page Test 1 Failed ! *************")
            driver.save_screenshot(filename='Screenshots/verify_login_page.png')
            # Cleanup
            driver.quit()
            assert False

    def test_login_page1(self, setup):
        self.logger.info("************** Login Test 1 started ! *************")
        driver = setup
        driver.get(url=self.baseURL)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(4)
        if driver.title == "Dashboard / nopCommerce administration":
            self.logger.info("************** Login Test 1 Passed *************")
            assert True
            lp.logout()
            driver.quit()
        else:
            self.logger.error("************** Login Test 1 Failed !!! *************")
            driver.save_screenshot(filename='Screenshots/login1.png')
            driver.quit()
            assert False
