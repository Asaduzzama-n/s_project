import string
import time
from random import random

from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import constant as const


# from utility.utility import run_test_case


class Registration(webdriver.Chrome):
    def __init__(self, driver_path=r"E:\Python_project\drivers", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Registration, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_registration_page(self):
        self.get(const.BASE_URL + "/signup")

    def check_successful_registration(self, name, email, password):
        try:
            print("Name:", name)
            name_field = self.find_element(By.CSS_SELECTOR, 'input[name="name"]')
            name_field.send_keys(name)

            print("Email:", email)

            email_field = self.find_element(By.CSS_SELECTOR, 'input[name="email"]')
            email_field.send_keys(email)

            print("password:", password)

            pass_field = self.find_element(By.CSS_SELECTOR, 'input[name="password"]')
            pass_field.send_keys(password)

            print("Clicking submit button")
            sign_up_btn = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
            sign_up_btn.click()
            time.sleep(2)
            message_element = self.find_element(By.ID, "reg_msg")

            if message_element.text == "":
                print("Successful!")
            else:
                print(message_element.text)

        except Exception as e:
            print("Error from card info:", e)

    # -------------------------------------------------------------------------------------

    def check_password(self):

        name_field = self.find_element(By.CSS_SELECTOR, 'input[name="name"]')
        name_field.send_keys("Asad")

        email_field = self.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email_field.send_keys("as232aaa4@gmailc.com")

        pass_field = self.find_element(By.CSS_SELECTOR, "input[name='password']")

        test_passwords = [
            ("", "Password is required"),  # Null input
            ("12345", "Password must be 6 characters long"),
            ("abcd", "Password must be 6 characters long"),
            ("WeakPassword", "Password must have uppercase, number and special characters"),
            ("lowercase123!", "Password must have uppercase, number and special characters"),  # Missing uppercase
            ("MixedCASE123", "Password must have uppercase, number and special characters"),
            ("StrongP@ss123", ""),  # Valid password
        ]

        submit_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")

        for password,expected_error_message in test_passwords:

            pass_field.clear()
            pass_field.send_keys(password)

            submit_button.click()

            time.sleep(1)

            error_message = self.find_element(By.ID, "pass_error").text

            if error_message == expected_error_message:
                print(f"Test for '{password}' passed --> {error_message}")
            else:
                print(f"Test for '{password}' failed. Expected: '{expected_error_message}', Actual: '{error_message}'")