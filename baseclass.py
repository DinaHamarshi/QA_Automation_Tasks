import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Exp_Cond
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@pytest.mark.usefixtures("driver_init")
class Basic_Test:

    def go_to_home_page(self):
        self.driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(5) # to make sure it is fully loaded

    def wait_for_element_to_be_visible(self, by, value, timeout=40):
        return WebDriverWait(self.driver, timeout).until(
            Exp_Cond.visibility_of_element_located((by, value))
        ) # presence_of_element_located

    def wait_for_element_to_be_clickable(self, by, value, timeout=40):
        return WebDriverWait(self.driver, timeout).until(
            Exp_Cond.element_to_be_clickable((by, value))  
        )
    
    def check_if_user_logged_in(self): 
        try:
            arrow_button = WebDriverWait(self.driver, 10).until(
            Exp_Cond.visibility_of_element_located((By.XPATH, "(//span[@class='customer-name']//button[@class='action switch' and @data-action='customer-menu-toggle'])[1]"))
            )
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def sign_out(self):
        arrow_button = self.wait_for_element_to_be_clickable(By.XPATH, "(//span[@class='customer-name']//button[@class='action switch' and @data-action='customer-menu-toggle'])[1]").click()
        sign_out_button = self.wait_for_element_to_be_clickable(By.XPATH, "(//a[contains(text(), 'Sign Out')])[1]").click()       


    # Create Account Method
    def create_account_method(self, FirstName, LastName, Email, Password, ConfirmPass):

        if self.check_if_user_logged_in():
            self.sign_out()
        self.go_to_home_page()
        Create_an_Account = self.wait_for_element_to_be_clickable(By.XPATH, "//a[contains(@href,'account/create')]").click()
        First_Name = self.wait_for_element_to_be_visible(By.XPATH, "//*[@id='firstname']").send_keys(FirstName)
        Last_Name = self.wait_for_element_to_be_visible(By.XPATH, "//*[@id='lastname']").send_keys(LastName)
        Email_Address = self.wait_for_element_to_be_visible(By.XPATH, "//*[@id='email_address']").send_keys(Email)
        Pass_word = self.wait_for_element_to_be_visible(By.XPATH, "//*[@id='password']").send_keys(Password)
        Confirm_Pass = self.wait_for_element_to_be_visible(By.XPATH, "//*[@id='password-confirmation']").send_keys(ConfirmPass)
        Create_Button = self.wait_for_element_to_be_clickable(By.XPATH, "//*[@id='form-validate']/div/div[1]/button/span").click()


    # Sign In Method
    def sign_in_method(self, Email, Password):

        if self.check_if_user_logged_in():
            self.sign_out()
        self.go_to_home_page()
        Sign_In = self.wait_for_element_to_be_clickable(By.XPATH, "//a[contains(@href,'account/login')]").click()
        Email_Address = self.wait_for_element_to_be_visible(By.XPATH, "//*[@id='email']").send_keys(Email)
        Pass_word = self.wait_for_element_to_be_visible(By.XPATH, "//*[@id='pass']").send_keys(Password)
        Sign_In_Button = self.wait_for_element_to_be_clickable(By.XPATH, "//*[@id='send2']/span").click()
