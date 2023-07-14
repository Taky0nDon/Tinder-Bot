# D A Y F I F T Y

## IFRAMES
### 3 WAYS OF WORKING WITH IFRAMES:
1. Using a Web Element:
```python
    # Store iframe web element
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

    # switch to selected iframe
driver.switch_to.frame(iframe)

    # Now click on button
driver.find_element(By.TAG_NAME, 'button').click()
 ```
2. With a name or ID:
```python
    # Switch frame by id
driver.switch_to.frame('buttonframe')

    # Now, Click on the button
driver.find_element(By.TAG_NAME, 'button').click()
  
```
3. With an index:
```python
    # Switch frame by id
driver.switch_to.frame('buttonframe')

    # Now, Click on the button
driver.find_element(By.TAG_NAME, 'button').click()
  
```

## LEAVING THE FRAME:
```python
    # switch back to default content
driver.switch_to.default_content()
  
```

## WINDOWS
1. Get the current window ID:
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    driver.find_element(By.LINK_TEXT, "new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))
    
```

## DISABLE WEBDRIVER FLAGS INDICATING AUTOMATION

```python
from selenium import webdriver 
import chromedriver_autoinstaller 
 
chromedriver_autoinstaller.install() 
 
# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
 
# Setting the driver path and requesting a page 
driver = webdriver.Chrome(options=options) 
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
 
driver.get("https://www.website.com")

```

## EXPECTED CONDITIONS
* locator is a tuple: `By, Path` (`By.ID, "some_id"`)

## Finding an element by attribute value:
By.CSS_SELECTOR, tag_name[attribute="value"]

## ANALYZE THE BROWSER FINGERPRINT
* [Cover Your Tracks](https://wwww.coveryourtracks.eff)

* [Common Bot Detection Techniques](https://github.com/0xInfection/Awesome-WAF)

* [A Great Stack Overflow Question About Selenium Detection](https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver)

## CLICK INTERCEPTED

selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element `<div class="Pos(a) P(.1em) Pe(n) Fw($semibold) Tt(u) Bdrs(4px) Bdw(4px) Bds(s) Wc($opacity) Op(0) Trsp($opacity) Trsdu($fast) Fz(4rem) Lh(3.5rem) Rotate(-20deg) T(10%) Start(10%) C($c-like-green) Bdc($c-like-green)" style="opacity: 0;">...</div>` 
is not clickable at point (584, 118). Other element would receive the click: `<div role="img" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" aria-labelledby="2d3d3044-d1fe-4744-ae8b-1ea9ef9ff81b" style="background-image: url(&quot;https://images-ssl.gotinder.com/u/9ijXcQmgQ2sPcDBVciq2Uf/uJBrjz668CpL7XN7dxbFQz.webp?Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6IiovdS85aWpYY1FtZ1Eyc1BjREJWY2lxMlVmLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2ODk1NDIzOTh9fX1dfQ__&amp;Signature=i7PWHVREyFPnA-E8V4uaa8YgA7X7RkhBO5eKneICx8oc0AGbLU3~tl4u127KuOrAQ2~jdbOpnWUdT0Wjnbqlg9GtEqDYfkonG56EF49RmqyY6fqN373TiyFFXUo5ML~RJw8pdz6VCZqIjiaYNKWisIqJ0QB-IzgbYUixg7Ln9K~k6H9xAG1iAk9f4uHoXpKbYxA13kny~mtVnvjDWPUEim9-xLUW48n6IN-8XK25k8lXmlhXbsliAOq9p0ewrGEIps2ms5G-mRPVI1-8mj1KFPTsPprN7FjJIvcVxdy1bD50Vxvt0HpwS7zz20f4RpElsHD4vFCSRbRJJKvfgkx0bA__&amp;Key-Pair-Id=K368TLDEUPA6OI&quot;); background-position: 50% 0%; background-size: 110.256%;"></div>`


## ADD APP TO HOMESCREEN POP UP
* first_layer = find_elements(By.CLASS_NAME, "App")
* desired div = first_layer.find_element(By.CLASS_NAME, "Expand")
* not_interested = desired_div.find_elements(By.TAG_NAME, "button")
* not_interested[-1].click()

## Finding an element by its inner text:
`child = driver.find_element(By.XPATH, '//*[text()="Like"]`

## Get page source:
`source_html = driver.page_source`

* `\U200b` = Zero Width SPace
* `\U202a` = Left-to-Right Embedding
* `\u202c` = Pop Directional Formatting