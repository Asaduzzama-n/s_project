from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import constant as const


class Donation(webdriver.Chrome):
    def __init__(self, driver_path=r"E:\Python_project\drivers", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Donation, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL + "/login")

    def login_user(self, email, password):
        email_input = self.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(email)  # Replace with the actual email

        # Find the password input field and enter a password
        password_input = self.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(password)  # Replace with the actual password

        # Find the "LOGIN" button and click it
        login_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

    def view_campaign_card(self):
        a_tag = self.find_element(By.CSS_SELECTOR, "div.card a[href^='/campaign/']")
        a_tag.click()

    def donation_test(self, amount=100):
        # Find the donation amount input field and enter a value
        donation_amount_input = self.find_element(By.CSS_SELECTOR, "input[name='donation_amount']")
        donation_amount_input.clear()  # Clear any existing input
        donation_amount_input.send_keys(amount)  # Enter the desired donation amount
        time.sleep(2)
        # Find the "Keep me anonymous" checkbox and click it
        anonymity_checkbox = self.find_element(By.CSS_SELECTOR, "input[name='anonymity']")
        anonymity_checkbox.click()
        time.sleep(2)
        # Find the "Donate Now" button and click it
        donate_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        donate_button.click()
        time.sleep(2)

        try:
            print("Switching to iframe...")
            WebDriverWait(self, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame']"))
            )

            print("Interacting with card input fields...")
            card_number_input = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='cardnumber']"))
            )
            card_number_input.send_keys("4242424242424242")

            expiration_date_input = self.find_element(By.CSS_SELECTOR, "input[name='exp-date']")
            expiration_date_input.send_keys("1230")

            cvc_input = self.find_element(By.CSS_SELECTOR, "input[name='cvc']")
            cvc_input.send_keys("123")

            postal_input = self.find_element(By.CSS_SELECTOR, "input[name='postal']")
            postal_input.send_keys("12121")

            self.switch_to.default_content()

            print("Clicking 'Pay' button...")
            pay_button = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-sm.mt-4.btn-primary"))
            )
            pay_button.click()

            payment_status_element = WebDriverWait(self, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".text-primary"))
            )
            # Get the text content of the payment status element
            payment_status_text = payment_status_element.text

            if payment_status_text:
                print(payment_status_text)

            textarea_element = self.find_element(By.CSS_SELECTOR, "textarea[name='message']")

            # Clear any existing content and enter the message text
            textarea_element.clear()
            textarea_element.send_keys("TESTING!")

            # Locate and click the "Submit" button
            submit_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_button.click()

            print("Test completed.")
        except Exception as e:
            print("An error occurred:", e)
