import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = os.environ.get("EMAIL")
PASS = os.environ.get("PASS")


url = "https://tinder.com"
decline_cookies_xpath = '//*[@id="u-1238065328"]/main/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]'
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
driver.get("https://tinder.com/404")
time.sleep(1)

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


driver.find_element(By.TAG_NAME, "input").send_keys(EMAIL)
driver.find_element(By.XPATH, next_xpath).click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(PASS, Keys.ENTER)
time.sleep(2)
keep_going = input("Hit ENTER to continue.")
driver.switch_to.window(original_window)
# Allow location
driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]').click()
#Don't allow notifications
driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]').click()
time.sleep(5)
# Start smashing those hearts
for n in range(10):
    driver.find_element(By.XPATH,
                        '//*[@id="u490315748"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button/'
                        'span/span/svg/path')\
        .click()
    time.sleep(1)
