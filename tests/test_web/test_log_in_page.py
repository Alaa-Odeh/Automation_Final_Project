import unittest

from infra.infra_web.browser_wrapper import BrowserWrapper
from logic.web_logic.home_page_pathfinder import PathfinderPage
from logic.web_logic.welcome_page import WelcomePage
from logic.web_logic.login_page import LoginPage


class Login_Page_Test(unittest.TestCase):
    def setUp(self):
        self.test_cases = [self.test_invalid_log_in,self.test_log_in]
        self.browser = BrowserWrapper()

    def test_run(self):
        if self.browser.config["grid"]:
            self.browser.build_cap()
            if self.browser.config["grid type"] == "serial":
                self.browser.test_grid_serial(self.test_cases )
            if self.browser.config["grid type"] == "parallel":
                self.browser.test_grid_parallel(self.test_cases )
        else:
            self.browser.run_single_browser(self.test_cases,self.browser.config["browser"] )

    def test_log_in(self,driver):
        self.welcome_page = WelcomePage(driver)
        self.welcome_page.click_log_in()
        self.login_page = LoginPage(driver)
        self.login_page.login_flow("friendola15@gmail.com", "AutomationTester2024")
        self.pathfinder_page = PathfinderPage(driver)
        user_name=self.pathfinder_page.extract_user_name()
        self.assertEqual(user_name,"friend","My W3Scools Account not Logged in")

    def test_invalid_log_in(self,driver):
        self.welcome_page = WelcomePage(driver)
        self.welcome_page.click_log_in()
        self.login_page = LoginPage(driver)
        Wrong_password=self.login_page.login_with_invalid_password("ofriend31@gmail.com","Tester")
        self.assertIn("Wrong password",Wrong_password,"My W3Scools Account not Logged in")







