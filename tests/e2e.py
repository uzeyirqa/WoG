import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_scores_service(app_url):
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
    driver.get(app_url)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "score"))
    )
    score = int(element.text)
    if 1 <= score <= 1000:
        driver.quit()
        return True
    else:
        driver.quit()
        return False


def main_function():
    app_url = "http://172.25.0.5:5000"
    if test_scores_service(app_url):
        print("Test passed!")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)


main_function()
