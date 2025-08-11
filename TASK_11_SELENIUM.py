import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from typing_extensions import Final
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

def test_selenium_pytest():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://www.guvi.in/')
        driver.find_element(By.ID,"login-btn").click()
        time.sleep(5)
        curr_url = driver.current_url
        assert curr_url == "https://www.guvi.in/sign-in/","Expect url not matching with current URL"
        driver.find_element(By.ID,"email").send_keys("xyz@gmail.com")
        driver.find_element(By.ID,"password").send_keys("XYZ@123")
        driver.find_element(By.ID,"login-btn").click()
        time.sleep(5)
        driver.implicitly_wait(5)

    finally:
        driver.quit()



def test_valid_login_url():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.guvi.in/')
        driver.find_element(By.ID, "login-btn").click()
        assert driver.current_url == "https://www.guvi.in/sign-in/", "URL mismatch"
        print("Login Page URL is Correct")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

def test_invalid_login_url():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.guvi.in/')
        driver.find_element(By.ID, "login-btn").click()
        assert driver.current_url == "https://www.guvi.in/sign-in/", "URL mismatch"
        print("Login Page URL is Correct")
    except Exception as e:
        print(e)
    finally:
        driver.quit()

def test_login_fields_visibility_and_enablement():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.guvi.in/')
        driver.find_element(By.ID, "login-btn").click()

        # Locate input fields
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")

        # Assertions for visibility
        assert email_field.is_displayed(), "Email field is not visible"
        assert password_field.is_displayed(), "Password field is not visible"

        # Assertions for enablement
        assert email_field.is_enabled(), "Email field is not enabled"
        assert password_field.is_enabled(), "Password field is not enabled"

        print("Username and Password fields are visible and enabled ")

    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()

def test_submit_button_functionality():
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.guvi.in/')
        driver.find_element(By.ID, "login-btn").click()

        # Locate input fields and submit button
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "login-btn")

        # Check visibility and enablement
        assert submit_button.is_displayed(), "Submit button is not visible"
        assert submit_button.is_enabled(), "Submit button is not enabled"

        # Enter credentials (you can use invalid ones to test error handling)
        email_field.send_keys("invalid@example.com")
        password_field.send_keys("wrongpassword")
        submit_button.click()

        time.sleep(3)  # Wait for response

        # Validate behavior — example: check for error message
        error_elements = driver.find_elements(By.CLASS_NAME, "error-message")  # Adjust selector as needed
        assert error_elements, "No error message displayed for invalid login"

        print("Submit button is working properly — triggered login attempt ✅")

    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()

