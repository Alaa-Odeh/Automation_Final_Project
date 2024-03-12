import concurrent
import time
from concurrent import futures

from selenium import webdriver
import json

class BrowserWrapper:


    def __init__(self):
        self._driver = None
        config_path = '../../config.json'
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.hub_url = self.config["hub_url"]
        print("Test Start")



    def get_driver(self,caps,user=None):
        self._driver = webdriver.Remote(command_executor=self.hub_url, options=caps)
        self._driver.get(self.config["url"])
        self._driver.maximize_window()

    def build_cap(self):
        self.chrome_cap = webdriver.ChromeOptions()
        self.chrome_cap.capabilities['platformName'] = 'Windows'

        self.firfox_cap=webdriver.FirefoxOptions()
        self.firfox_cap.capabilities['platformName'] = 'Windows'

        self.edge_cap = webdriver.EdgeOptions()
        self.edge_cap.capabilities['platformName'] = 'Windows'
        self.caps_list = [self.chrome_cap,self.edge_cap,self.firfox_cap]

    def test_grid_parallel(self,test_cases,user=None):
        self.test_cases=test_cases
        self.user=user
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.caps_list)) as executor:

            for test_case, cap in [(test_case, cap) for test_case in self.test_cases for cap in self.caps_list]:
                 executor.submit(self.run_test_case, test_case, cap)
                 time.sleep(5)

    def test_grid_serial(self,test_cases,user=None):
        self.user = user
        for caps in self.caps_list:
            for test_case in test_cases:
                self.run_test_case(test_case,caps)

    def run_test_case(self,test_case, caps):
        self.get_driver(caps,self.user)
        test_case(self._driver)


    def run_single_browser(self,test_cases,browser,user=None):
        if browser == "Chrome":
            self._driver = webdriver.Chrome()
        elif browser == "FireFox":
            self._driver = webdriver.Firefox()
        elif browser == "Edge":
            self._driver = webdriver.Edge()
        self._driver.get(self.config["url"])
        self._driver.maximize_window()
        for test_case in test_cases:

                test_case(self._driver)
                self._driver.get(self.config["url"])

    def teardown(self):
        self._driver.quit()
