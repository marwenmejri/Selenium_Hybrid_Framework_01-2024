import time
from pagesObjects.LoginPage import LoginPage
from utilities.readProperties import get_username, get_password, get_url
from utilities.custom_logger import LogGen


class Test001Login:
    base_url = get_url()
    username = get_username()
    password = get_password()
    logger = LogGen.sample_logger()

    def test_login_page_title(self, setup):
        self.logger.info("************** Test001Login started !! *************")
        self.logger.info("************** Verifying Login Page Test started ! *************")
        driver = setup
        driver.get(url=self.base_url)
        title = driver.title
        if title == 'Your store. Login':
            self.logger.info("************** Verifying Login Page Test Passed *************")
            driver.quit()
            assert True
        else:
            self.logger.error("************** Verifying Login Page Test Failed ! *************")
            driver.save_screenshot('Screenshots/test_login_page_title.png')
            driver.quit()
            assert False

    def test_login(self, setup):
        self.logger.info("************** Login Test started ! *************")
        driver = setup
        driver.get(url=self.base_url)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        lp.set_password(password=self.password)
        lp.login()
        title = driver.title
        if title == 'Dashboard / nopCommerce administration':
            self.logger.info("************** Login Test Passed *************")
            assert True
            time.sleep(2)
            lp.logout()
            driver.quit()
        else:
            self.logger.error("************** Login Test Failed ! *************")
            driver.save_screenshot('Screenshots/test_login.png')
            driver.quit()
            assert False

    def test_login_page_title1(self, setup):
        self.logger.info("************** Verifying Login Page Test1 started ! *************")
        driver = setup
        driver.get(url=self.base_url)
        title = driver.title
        if title == 'Your store. Login':
            self.logger.info("************** Verifying Login Page Test1 Passed *************")
            driver.quit()
            assert True
        else:
            self.logger.error("************** Verifying Login Page Test1 Failed ! *************")
            driver.save_screenshot('Screenshots/test_login_page_title1.png')
            driver.quit()
            assert False

    def test_login1(self, setup):
        self.logger.info("************** Login Test1 started ! *************")
        driver = setup
        driver.get(url=self.base_url)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        lp.set_password(password=self.password)
        lp.login()
        title = driver.title
        if title == 'Dashboard / nopCommerce administration':
            self.logger.info("************** Login Test1 Passed *************")
            assert True
            time.sleep(2)
            lp.logout()
            driver.quit()
        else:
            self.logger.error("************** Login Test1 Failed ! *************")
            driver.save_screenshot('Screenshots/test_login1.png')
            driver.quit()
            assert False


