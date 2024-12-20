from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    # Set up ChromeDriver automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open YouTube homepage
        driver.get("https://www.google.com")

        # Find the search bar element and enter a search term
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Selenium WebDriver tutorial")
        search_box.submit()

        
    finally:
        # Close the browser
        driver.quit()
