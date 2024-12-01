from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_youtube_search():
    # Set up ChromeDriver automatically
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open YouTube homepage
        driver.get("https://www.youtube.com")

        # Find the search bar element and enter a search term
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("Selenium WebDriver tutorial")
        search_box.submit()

        # Wait for results to load
        time.sleep(5)

        # Verify that the results contain the search term
        first_video_title = driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string').text
        assert "Selenium" in first_video_title, f"Expected 'Selenium' in the video title but got {first_video_title}"

    finally:
        # Close the browser
        driver.quit()
# automated test