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
        if user is None:
            pass
        else:
            if user == "first_user":
                self._driver.add_cookie({"name": "accessToken",
                                         "value": "eyJraWQiOiJQS0tER0N2cFwvdlpVa1NEZDByem9NRTFEbWNDdElFM3o1V2ZmT0RMWWxJTT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4NDg4OWNiNy0xMjdkLTQ0YjAtYWU0MS1hODNlYzc5Y2FmZDgiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfdUc5U0dYN1dkX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91RzlTR1g3V2QiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiJkMWdycW1sMGVtaDd2b3RrYjBndHJybjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCIsImF1dGhfdGltZSI6MTcwOTQ2MzUyMCwiZXhwIjoxNzA5NTA2NzIwLCJpYXQiOjE3MDk0NjM1MjEsImp0aSI6ImMwMTYwYzEwLTNjY2ItNDdkNC1hYzhmLTk5NjA1Nzc3MmYzZCIsInVzZXJuYW1lIjoiR29vZ2xlXzEwODg5OTA1MjIxNTM1MTExMzg4MiJ9.lwwtvy5t05SL7GHPFKtL6e_wI435gZPd7ZCdmacc-p6Vw_1T443MOLIYbFQ1IK6pIyMqG5hYH8C0DVIyliRSJGIoiS1UZ8_lSnOg2X88gihNtowKbnh1chdJGjYxsouLLWJ-FegdOKDyoaWBfmR5hKgHlublG3ciQyS8qfton4M1HDd-IT8_pzo-toj0wVasC57t7YpFR_NDbE2u4jO50ggYK3QI1FC064HbwUZnJ9dzdt3vsQ5Cu20JivVECLLiya6-zg-r7wVFj0An0pdLzdegcM-MVXZpCokVD3gJfAVp_x0bZiTFIYI5q52MLdSaagZlhrQ7QptkTyP7oFHzUg", "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSession", "value": "1", "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSessionMeta",
                                         "value": "eyJpZCI6ImZiZDEyMWNiLTY3NGEtNDcxNS1iNGU1LTU3OGI5MTI5YjYyMCIsImlzcyI6MTcwOTU0NTA3MywiYXRleHAiOjE3MDk1ODc5NzEsInJ0ZXhwIjoxNzEyMTM2NzczfQ==",
                                         "domain": ".w3schools.com"})
            elif user=="second_user":
                self._driver.add_cookie({"name": "accessToken",
                                         "value": "eyJraWQiOiJQS0tER0N2cFwvdlpVa1NEZDByem9NRTFEbWNDdElFM3o1V2ZmT0RMWWxJTT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4NDg4OWNiNy0xMjdkLTQ0YjAtYWU0MS1hODNlYzc5Y2FmZDgiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfdUc5U0dYN1dkX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91RzlTR1g3V2QiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiJkMWdycW1sMGVtaDd2b3RrYjBndHJybjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCIsImF1dGhfdGltZSI6MTcwOTQ5NjkxNSwiZXhwIjoxNzA5NTQwMTE1LCJpYXQiOjE3MDk0OTY5MTUsImp0aSI6ImE5NDY1YjJjLTkyZWYtNDVlZC05YjIyLWQ2OWY4NWZmOTE3MiIsInVzZXJuYW1lIjoiR29vZ2xlXzEwODg5OTA1MjIxNTM1MTExMzg4MiJ9.KTQPUGMRzUAkkAw15EpHie2-hutGaX1zCSwz70sn4tnrCj51-UHez6w-8_X5sQz-AvO6sVUf3CDgvIaTJB79L3iEfFVQ7QgX9EzDn1gf8D734HFapbKycs6fbd231QQQ5zN8zxPpBafUOWrwaSqzvNdfxKrYe4YUMnHipIlKc_Jjq49JRgezXor9MAr0QnTL2kZ8fFhFwi9eckSAoLIRZj2ObQ7_tqn7hdx5pdjT5jn8W0S1LYwJzyNhVxfXkVIbks78PLQKyJMsW6DxXrjvjMUyhEevTqutIjjKEhvSbeOoU5CnII17OLhLj7IZhkpTgBMKda8kFR-jKdakNTWw3A",
                                         "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSession", "value": "1", "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSessionMeta",
                                         "value": "eyJpZCI6IjQ4N2IxMjZhLTIwMjktNDhhNC05NmQyLWIwNTdkNDJkMTNiOCIsImlzcyI6MTcwOTU0NTYwOSwiYXRleHAiOjE3MDk1ODg1MDMsInJ0ZXhwIjoxNzEyMTM3MzA5fQ=="
                                                  ,"domain": ".w3schools.com"})

            self._driver.get("https://pathfinder.w3schools.com/")
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
        self.test_cases = test_cases
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.caps_list)) as executor:
            futures = []
            for test_case, cap in [(test_case, cap) for test_case in self.test_cases for cap in self.caps_list]:
                # Submit the test case and cap to the executor
                future = executor.submit(self.run_test_case, test_case, cap)
                futures.append(future)
                # Delay the submission of the next test case and cap
                time.sleep(8)
            # Wait for all futures to complete
            for future in concurrent.futures.as_completed(futures):
                future.result()
    def test_grid_serial(self,test_cases,user=None):
        self.user = user
        for caps in self.caps_list:
            for test_case in test_cases:
                self.run_test_case(test_case,caps)

    def run_test_case(self,test_case, caps):
        self.get_driver(caps,self.user)
        self.driver = self._driver
        test_case(self.driver)


    def run_single_browser(self,test_cases,browser,user=None):
        if browser == "Chrome":
            self._driver = webdriver.Chrome()
        elif browser == "FireFox":
            self._driver = webdriver.Firefox()
        elif browser == "Edge":
            self._driver = webdriver.Edge()
        self._driver.get(self.config["url"])
        self._driver.maximize_window()
        if user is None:
            pass
        else:
            if user == "first_user":
                self._driver.add_cookie({"name": "accessToken",
                                         "value": "eyJraWQiOiJQS0tER0N2cFwvdlpVa1NEZDByem9NRTFEbWNDdElFM3o1V2ZmT0RMWWxJTT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4NDg4OWNiNy0xMjdkLTQ0YjAtYWU0MS1hODNlYzc5Y2FmZDgiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfdUc5U0dYN1dkX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91RzlTR1g3V2QiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiJkMWdycW1sMGVtaDd2b3RrYjBndHJybjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCIsImF1dGhfdGltZSI6MTcwOTQ2MzUyMCwiZXhwIjoxNzA5NTA2NzIwLCJpYXQiOjE3MDk0NjM1MjEsImp0aSI6ImMwMTYwYzEwLTNjY2ItNDdkNC1hYzhmLTk5NjA1Nzc3MmYzZCIsInVzZXJuYW1lIjoiR29vZ2xlXzEwODg5OTA1MjIxNTM1MTExMzg4MiJ9.lwwtvy5t05SL7GHPFKtL6e_wI435gZPd7ZCdmacc-p6Vw_1T443MOLIYbFQ1IK6pIyMqG5hYH8C0DVIyliRSJGIoiS1UZ8_lSnOg2X88gihNtowKbnh1chdJGjYxsouLLWJ-FegdOKDyoaWBfmR5hKgHlublG3ciQyS8qfton4M1HDd-IT8_pzo-toj0wVasC57t7YpFR_NDbE2u4jO50ggYK3QI1FC064HbwUZnJ9dzdt3vsQ5Cu20JivVECLLiya6-zg-r7wVFj0An0pdLzdegcM-MVXZpCokVD3gJfAVp_x0bZiTFIYI5q52MLdSaagZlhrQ7QptkTyP7oFHzUg",
                                         "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSession", "value": "1", "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSessionMeta",
                                         "value": "eyJpZCI6ImZiZDEyMWNiLTY3NGEtNDcxNS1iNGU1LTU3OGI5MTI5YjYyMCIsImlzcyI6MTcwOTU0NTA3MywiYXRleHAiOjE3MDk1ODc5NzEsInJ0ZXhwIjoxNzEyMTM2NzczfQ==",
                                         "domain": ".w3schools.com"})
            elif user == "second_user":
                self._driver.add_cookie({"name": "accessToken",
                                         "value": "eyJraWQiOiJQS0tER0N2cFwvdlpVa1NEZDByem9NRTFEbWNDdElFM3o1V2ZmT0RMWWxJTT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4NDg4OWNiNy0xMjdkLTQ0YjAtYWU0MS1hODNlYzc5Y2FmZDgiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfdUc5U0dYN1dkX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91RzlTR1g3V2QiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiJkMWdycW1sMGVtaDd2b3RrYjBndHJybjAiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCIsImF1dGhfdGltZSI6MTcwOTU0MTAwNCwiZXhwIjoxNzA5NTg0MjA0LCJpYXQiOjE3MDk1NDEwMDUsImp0aSI6Ijg3ZTQ0MmVjLWU4ZWYtNGQwNy1iZGZlLTc4ODgwOTYyOWNkNyIsInVzZXJuYW1lIjoiR29vZ2xlXzEwODg5OTA1MjIxNTM1MTExMzg4MiJ9.Bw9cSAjCc8DZGBEdiLE61yJ8p4WrpWp6t1tYTE6od2kwZtq0FB-q6F-PmtNcKal0tdp5_ElxXiJ3_P8FA_kSfRwmBQaAPzEOfR4x9UJOB0GwXRmA-GeDsUTxZItaRVRmRduK1jfLjeTk4dOOH5Rxo0UfQ-x-Y-CGOklf3y7-CKiU_b2nrzRbGhcozj9cfV1VPAQHbLZCJkt8LK570T-938ix_Ulv-vqfF0txmDK9faxDVkQmSBghQy8dqHN5RNOJiitl4_wfDMvgIwG0ofWLPQaK87uWjScQlXa7qEnO7EVcSoTwBTVxHk03dauv7Pd_mQoj_M0TktJyYcTCWzGTpQ",
                                         "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSession", "value": "1", "domain": ".w3schools.com"})
                self._driver.add_cookie({"name": "userSessionMeta",
                                         "value": "eyJpZCI6IjQ4N2IxMjZhLTIwMjktNDhhNC05NmQyLWIwNTdkNDJkMTNiOCIsImlzcyI6MTcwOTU0NTYwOSwiYXRleHAiOjE3MDk1ODg1MDMsInJ0ZXhwIjoxNzEyMTM3MzA5fQ=="
                                                  ,"domain": ".w3schools.com"})

            self._driver.get("https://pathfinder.w3schools.com/")
        for test_case in test_cases:
            test_case(self._driver)

    def teardown(self):
        self._driver.quit()