import time
import unittest

from selenium import webdriver

from infra.infra_web.browser_wrapper import BrowserWrapper
from logic.web_logic.home_page_pathfinder import PathfinderPage
from logic.web_logic.login_page import LoginPage
from logic.web_logic.skills_page import SkillsPage
from selenium.webdriver.chrome.options import Options

from logic.web_logic.welcome_page import WelcomePage


class TestSkillsPage(unittest.TestCase):
    def setUp(self):
        self.test_cases = [self.test_my_skills_in_chart]
        self.browser = BrowserWrapper()

    def test_run(self):
        if self.browser.config["grid"]:
            self.browser.build_cap()
            if self.browser.config["grid type"] == "serial":
                self.browser.test_grid_serial(self.test_cases)
            if self.browser.config["grid type"] == "parallel":
                self.browser.test_grid_parallel(self.test_cases)
        else:
            self.browser.run_single_browser(self.test_cases, self.browser.config["browser"])

    def test_my_skills_in_chart(self,driver):
        self.welcome_page = WelcomePage(driver)
        self.welcome_page.click_log_in()
        self.login_page = LoginPage(driver)
        self.login_page.login_flow("friendola15@gmail.com", "AutomationTester2024")
        time.sleep(8)
        self.pathfinder_page = PathfinderPage(driver)
        self.pathfinder_page.click_skills_button()
        self.my_skills = SkillsPage(driver)
        self.my_skills.get_my_skills()
        self.my_skills.get_chart_ticks()
        self.assertListEqual(self.my_skills.all_my_skills,self.my_skills.all_chart_ticks,"Something is missing")