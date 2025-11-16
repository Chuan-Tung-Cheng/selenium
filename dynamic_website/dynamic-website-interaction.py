from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

TARGET_URL = "https://www.birmingham.ac.uk/" # Birmingham University Official Website homepage

def set_up():
    """
    set up selenium webdriver
    :return: driver instance
    """
    try:
        driver = webdriver.Chrome()
        driver.get(TARGET_URL)
        return driver
    except Exception as e:
        print(f"Error : {e}, return None")
        return None

def maximize_window(driver):
    driver.maximize_window()
    print(f"Successfully connect to the target website: {driver.title}")

def process_cookies(wait):
    """
    :param wait: wait instance, consisting of driver
    will wait for 10 seconds to find ID that is including cookie
    """
    try:
        cookie_button = wait.until(
            ec.element_to_be_clickable((By.ID, "ccc-notify-accept"))
        )
        cookie_button.click()
        print("Successfully clicked cookie (id = ccc-notify-accept)")
    except TimeoutException as e:
        print(f"Can't find cookie, {e}")

def perform_search(wait, keyword):
    """
    At Birmingham University's homepage, perform search
    :param wait: wait instance, consisting of driver
    :param keyword: keyword that users want to search for
    """
    try:
        # IMPORTANT
        # step 1: look for search icon
        search_button_txt = "text-button text-button--hollow theme-uobmain"
        print(f"searching for the search icon (class : {search_button_txt}) ...")
        search_button = wait.until(
            ec.element_to_be_clickable((By.CLASS_NAME, search_button_txt))
        )
        search_button.click()
        # step 2: enter the keyword into the search blank
        search_blank_txt = "form-input__input"
        print(f"searching for the search blank (class : {search_blank_txt}) ...")

        search_blank = wait.until(
            ec.visibility_of_element_located((By.CLASS_NAME, search_blank_txt))
        )
        search_blank.send_keys(keyword)
        print(f"Has entered keyword into search blank, keyword : {keyword}")

        # step 3: post
        print("Processing posting ...")
        search_blank.send_keys(Keys.ENTER)

        print("Post has been done!")
    except Exception as e:
        print(f"Error : {e}")


def main():
    driver = set_up()
    if driver is None:
        print("Failed to set up driver")
        return
    try:
        wait = WebDriverWait(driver, 10) # wait for cookie
        """
        WebDriverWait(driver, 10) vs driver.implicitly_wait(10)
        """

        # process cookie
        process_cookies(wait)

        # handle search block
        keyword = "Data Science"
        perform_search(wait, keyword)

    except Exception as e:
        print(f"Error : {e}")
    finally:
        input("Press [ENTER] to exit...]")
        if driver:
            driver.quit()
        print("This program has been done")



if __name__ == "__main__":
    main()
