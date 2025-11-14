from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # open Chrome, a web browser

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get("https://www.google.com") # requests.get("https://www.google.com")


title = driver.title
"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Google</title> # get title from here
    ...
  </head>
  <body>
    ...
  </body>
</html>
"""
print(title)

url = driver.current_url # the same as the url for the usage of driver.get
print(url)

driver.back() # go back to the previous page
print(driver.back())

driver.forward() # go to the next page
print(driver.forward())

driver.refresh() # refresh the current page
print(driver.refresh())

# driver.implicitly_wait(0.5)
#
# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
# text_box.send_keys("Selenium")
# submit_button.click()
#
# message = driver.find_element(by=By.ID, value="message")
# text = message.text
#
# driver.quit()

