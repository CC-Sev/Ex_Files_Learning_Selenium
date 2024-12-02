from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_google_search():
    # Set up ChromeDriver automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open Google and perform a search
        driver.get("https://www.google.com")
        
        search_box = driver.find_element("name", "q")
        search_box.send_keys("Selenium")
        search_box.submit()

        # Wait for user input to quit
        #while True:
        #    user_input = input('Type q to quit: ')
        #    if user_input.lower() == "q":
        #        break
    finally:
        # Close the browser
        driver.quit()
