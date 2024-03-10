from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():
    CONTINUE_WITH_GOOGLE="//button[@class='ButtonV2_button_wrapper__Tb921 ButtonV2_btn_green__UfRit LoginModal_cta_bottom_box_button_google_login__qKvO2']"
    EMAIL_INPUT = '//input[@autocomplete="username"]'
    NEXT_BUTTON='//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]'
    PASSWORD_INPUT='//input[@autocomplete="current-password"]'
    PASSWORD_NEXT_BUTTON='//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]'
    LOG_IN_BUTTON='//button[@class="Button_button__URNp+ Button_primary__d2Jt3 Button_fullwidth__0HLEu"]'


    def __init__(self, driver):
        self._driver =driver
        self.continue_with_google=self._driver.find_element(By.XPATH,self.CONTINUE_WITH_GOOGLE)
        self.log_in_button= self._driver.find_element(By.XPATH,self.LOG_IN_BUTTON)


    def click_continue_with_google_button(self):
        self.continue_with_google.click()

    def fill_email_input_field(self,email):
        self.email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self.email_input.send_keys(email)
    def click_next_button(self,element):
       self.next_button = WebDriverWait(self._driver,20).until(EC.element_to_be_clickable((By.XPATH, element))).click()

    def fill_password_input_field(self,password):
        self.password_input=WebDriverWait(self._driver,15).until(EC.visibility_of_element_located((By.XPATH,self.PASSWORD_INPUT)))
        self.password_input.send_keys(password)


    def login_flow(self,email,password):
        self.click_continue_with_google_button()
        self.fill_email_input_field(email)
        self.click_next_button(self.NEXT_BUTTON)
        self.fill_password_input_field(password)
        self.click_next_button(self.PASSWORD_NEXT_BUTTON)








