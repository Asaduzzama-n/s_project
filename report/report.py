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


class Report(webdriver.Chrome):
    def __init__(self, driver_path=r"E:\Python_project\drivers", teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Report, self).__init__()
        self.implicitly_wait(20)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_login_page(self):
        self.get(const.BASE_URL + "/login")

    def login_user(self, email, password):
        email_input = self.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(email)

        password_input = self.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(password)

        login_button = self.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

    def redirect_to_report_generation_page(self):
        # time.sleep(4)
        # # Find the Dashboard link by its ID
        # dashboard_link = self.find_element(By.ID, "dashboard_id")
        #
        # # Perform the click action
        # dashboard_link.click()
        self.get(const.BASE_URL + "/dashboard")
        self.get(const.BASE_URL + "/dashboard/my-campaign")

        time.sleep(2)
        print("Selecting campaign to view...")
        dashboard_link = self.find_element(By.ID, "644da1fce7d17265e5ac52a5")
        dashboard_link.click()
        time.sleep(2)
        print("Clicking generate report")
        generate_report_btn = self.find_element(By.ID, "generate_report")
        generate_report_btn.click()
        time.sleep(2)
        print("Selecting last month")
        last_month_button = self.find_element(By.XPATH, "//button/span[text()='Last Month']")
        last_month_button.click()

        # print("Selecting This month")
        # this_month_button = self.find_element(By.XPATH, "//button/span[text()='This Month']")
        # this_month_button.click()

        # print("Selecting last week")
        # last_week_button = self.find_element(By.XPATH, "//button/span[text()='Last Week']")
        # last_week_button.click()

        display_report = self.find_element(By.ID, "show_report")
        display_report.click()
        time.sleep(2)

        print("Test Successful")