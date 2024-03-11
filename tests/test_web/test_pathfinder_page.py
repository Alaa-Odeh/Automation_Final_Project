import time
import unittest
from infra.infra_web.browser_wrapper import BrowserWrapper
from logic.web_logic.home_page_pathfinder import PathfinderPage
from logic.web_logic.login_page import LoginPage
from logic.web_logic.welcome_page import WelcomePage


class TestPathfinderPage(unittest.TestCase):
    def setUp(self):
        #self.test_cases=[self.test_svg_tutorial,self.test_light_mode_toggle]
        self.test_cases=[self.test_pathfinder_page]
        self.browser = BrowserWrapper()

    def test_run(self):
        if self.browser.config["grid"]:
            self.browser.build_cap()
            if self.browser.config["grid type"]=="serial":
                self.browser.test_grid_serial(self.test_cases)
            if self.browser.config["grid type"]=="parallel":
                self.browser.test_grid_parallel(self.test_cases)
        else:
            self.browser.run_single_browser(self.test_cases,self.browser.config["browser"])


    def test_pathfinder_page(self,driver):
        self.welcome_page = WelcomePage(driver)
        self.welcome_page.click_log_in()
        self.login_page = LoginPage(driver)
        self.login_page.login_flow("friendola15@gmail.com", "AutomationTester2024")
        time.sleep(8)
        self.pathfinder_page = PathfinderPage(driver)
        calculated_time=self.pathfinder_page.set_goal_and_calculate_total_estimated_time(10, "HTML", "Professional")
        estimated_time=self.pathfinder_page.set_weekly_hours_slider_and_get_estimated_goal(10)
        self.assertLessEqual(abs(estimated_time-calculated_time),2,"The estimated time is wrong")



    def test_light_mode_toggle(self,driver):
        self.pathfinder_page = PathfinderPage(driver)
        light_mode_before=self.pathfinder_page.get_light_mode_label_before()
        light_mode_after=self.pathfinder_page.get_light_mode_label_after()
        self.assertFalse(light_mode_before==light_mode_after,"Light Mode Did not change")


    def test_svg_tutorial(self,driver):
        self.welcome_page = WelcomePage(driver)
        self.welcome_page.click_log_in()
        self.login_page = LoginPage(driver)
        self.login_page.login_flow("friendola15@gmail.com", "AutomationTester2024")
        time.sleep(10)
        self.pathfinder_page = PathfinderPage(driver)
        page_header=self.pathfinder_page.choose_learn_svg_tutorials()
        self.assertEqual(page_header,"SVG Tutorial","Wrong Tutorial Page")