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

EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")


url = "https://tinder.com"
decline_cookies_xpath = '//*[@id="t223514671"]/main/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]'
next_xpath = '//*[@id="identifierNext"]/div/button/span'


options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# stay_open.add_argument("--headless=new")
# stay_open.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# driver.maximize_window()
selenium_stealth.stealth(driver,
                         user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                         languages=["en","en-US"],
                         platform="web",
                         )
driver.get("https://tinder.com/404")
time.sleep(1)
### ADDING COOKIES
with open("cookies.json") as file:
# Check if the file is empty. Only continue if it's not.
    if len(file.read()) > 0:
        lines = file.readlines()
        cookie_list = []
        for line in lines:
            print(line)
            cookie_list.append(json.loads(line))
        for cookie in cookie_list:
            driver.add_cookie(cookie)



print("here")
driver.get(url)
print(driver.current_window_handle)
time.sleep(3)

original_window = driver.current_window_handle


driver.find_element(By.LINK_TEXT, "Log in").click()
time.sleep(2)
driver.find_element(By.XPATH, decline_cookies_xpath).click()
driver.find_element(By.TAG_NAME, "iframe").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))

for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
print(driver.current_window_handle)
# with open("googlecookies.txt") as file:
#     cookies = file.readlines()
#     for cookie in cookies:
#         stripped_cookie = cookie.strip()
#         cookie_dict = json.loads(stripped_cookie)
#         driver.add_cookie(cookie_dict)
# selenium.common.exceptions.UnableToSetCookieException: Message: unable to set cookie

driver.find_element(By.TAG_NAME, "input").send_keys(EMAIL)
driver.find_element(By.XPATH, next_xpath).click()
time.sleep(5)
# wait.until(EC.presence_of_element_located(locator=(By.ID, "password")))
password_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
password_input.send_keys(PASS, Keys.ENTER)


current_page = driver.find_element(By.TAG_NAME, "html")
# with open("2fapage.html", "w") as file:
#     page_source = driver.page_source
#     for char in page_source:
#         if char in "\u200b":
#             file.write("ZWSP")
#         elif char == "\u202a":
#             file.write("LTRE")
#         else:
#             file.write(char) f
print(driver.current_window_handle)
time.sleep(2)
keep_going = input("Hit ENTER to continue.")


driver.switch_to.window(original_window)

# Allow location
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Allow"]').click()
#Don't allow notifications
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Not interested"]').click()
time.sleep(5)
# Start smashing those hearts
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
