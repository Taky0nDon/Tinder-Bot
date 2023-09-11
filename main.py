import time
import os
import json

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium_stealth
from dotenv import load_dotenv
load_dotenv("env.env")

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  # Supposedly this helps with stealth

selenium_stealth.stealth(driver,
                         user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                         languages=["en","en-US"],
                         platform="web",
                         )

EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")
accept_cookies_xpath = '//*[text()="I accept"]'
next_xpath = '//*[@id="identifierNext"]/div/button/span'

driver.get("https://tinder.com/404")
time.sleep(1)

driver.get("https://tinder.com")
print(driver.current_window_handle)
time.sleep(3)

original_window = driver.current_window_handle

# CLICK LOGIN BUTTON
driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)
# DON'T DECLINE COOKIES
driver.find_element(By.XPATH, accept_cookies_xpath).click()
driver.find_element(By.TAG_NAME, "iframe").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))
# THIS PART SWITCHES FOCUS TO THE GOOGLE AUTH WINDOW
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)

print(driver.current_window_handle)

driver.find_element(By.TAG_NAME, "input").send_keys(EMAIL)
driver.find_element(By.XPATH, next_xpath).click()
time.sleep(5)
password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys(PASS, Keys.ENTER)

time.sleep(2)
keep_going = input("Hit ENTER to continue.")
driver.switch_to.window(original_window)

# ALLOW LOCATION
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Allow"]').click()
#DON'T ALLOW NOTIFICATIONS
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Not interested"]').click()
time.sleep(5)
# START SMASHING THOSE HEARTS
just_before_like_cookies = driver.get_cookies()
for cookie in just_before_like_cookies:
    with open("cookies.json", "a") as file:
        json.dump(cookie, file)
        file.write("\n")
likes = 10
not_interested_clicks = 0
match_found_clicks = 0
for n in range(60):
    print(f"{likes=}, {not_interested_clicks=}, {match_found_clicks=}")
# Add tinder to homescreen popup class: Bgc\(\$c-ds-background-primary\)
    # child = driver.find_element(By.XPATH, '//*[text()="Like"]')
    # parent = child.find_element(By.XPATH, "./..")
    like_button = driver.find_element(By.CLASS_NAME, 'Bdc\(\$c-ds-border-gamepad-like-default\)')
    like_button.click()
    print("Liked!")
    time.sleep(1)
    not_interested = driver.find_elements(By.XPATH, '//*[text()="Not interested"]')
    match_found = driver.find_elements(By.XPATH, '//*[text()="match"]')
    if len(not_interested) > 0:
        # this works
        not_interested[0].click()
        not_interested_clicks += 1
    if len(match_found) > 0:
        # if anybody loved me, I'd know if this worked too.
        match_found[0].click()
        match_found_clicks += 1
    likes += 1


# Need to account for matches!
