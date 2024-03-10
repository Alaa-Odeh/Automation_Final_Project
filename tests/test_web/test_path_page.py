import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from logic.web_logic.home_page_pathfinder import PathfinderPage
from logic.web_logic.path_page import  MyPathPage


class TestMYPathPage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self._driver = webdriver.Chrome(options=chrome_options)
        self._driver.get("https://www.w3schools.com/")
        self._driver.add_cookie({"name": "accessToken", "value": "eyJraWQiOiJQS0tER0N2cFwvdlpVa1NEZDByem9NRTFEbWNDdElFM3o1V2ZmT0RMWWxJTT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJlZjcwOGQxZS0zOTc0LTQzNTctOTkxNy03MGMwOGMyZmNkNWIiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfdUc5U0dYN1dkX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91RzlTR1g3V2QiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiJkMWdycW1sMGVtaDd2b3RrYjBndHJybjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCIsImF1dGhfdGltZSI6MTcwOTQ1MDgyMywiZXhwIjoxNzA5NDk0MDIzLCJpYXQiOjE3MDk0NTA4MjQsImp0aSI6IjczOTFlNDFjLWMwNTMtNGRiYi1iN2MwLTUyMTFmMWU0ZGY1ZSIsInVzZXJuYW1lIjoiR29vZ2xlXzExNTU0MjYzNDE3OTA1OTgwMTk4OSJ9.Faa5Ls4xWeNQxe93WFwPjuAuABqyapt-3p2twSTZ8S3vEBIWPgjvsFc0mDh1UubRaigav-kd2_gwaWjVX5kT36e_Zv-u2GLqvxrUwVjnywDoPn36iDBuq1B8ADCCh6irbRQwlCo507zOyQvEgywdFCup6D3fnVAnu-kxLNTkqZixsKPwIMzAH5-oOeustTXUNnGnrgXFaZ5789vwWaGt7CPwgCkchHVUFxVOQwZGA1pVJrPLfLAQJzAep-NleVfdBt33DnrCs1ikA2N8wsmb-xhJSnvKevkaQb4Ep1fqgfuhNiEx4fa9dFlrwLzSW5aejXTmaUx8xHolgea3bjRoFw", "domain": ".w3schools.com"})
        self._driver.add_cookie({"name": "userSession", "value": "1", "domain": ".w3schools.com"})
        self._driver.add_cookie({"name": "userSessionMeta", "value": "eyJpZCI6IjA1M2VmZDdiLTE4ZDgtNDRiZC1iZTUzLThkMjNlMDRiNzBjYyIsImlzcyI6MTcwOTQ1MDgyNiwiYXRleHAiOjE3MDk0OTM3MjQsInJ0ZXhwIjoxNzEyMDQyNTI2fQ==", "domain": ".w3schools.com"})
        self._driver.get("https://pathfinder.w3schools.com/")
        self._driver.maximize_window()
        self.pathfinder_page = PathfinderPage(self._driver)
        self.pathfinder_page.click_on_resume_learning_button()
        self.my_path_page = MyPathPage(self._driver)


    def test_my_path_page(self):
        self.my_path_page.get_actuall_page_labels_on_both_websites()
        self.actuall_labels=self.my_path_page.actuall_labels
        self.path_labels=self.my_path_page.path_labels
        self.assertListEqual(self.actuall_labels, self.path_labels,"Labels Dont Match")
