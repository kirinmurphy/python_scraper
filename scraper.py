import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set path to chromedriver as per your configuration
webdriver_service = Service('/Users/KirinMurphy/Downloads/chromedriver_mac_arm64/chromedriver')

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

url = "https://hotels.cloudbeds.com/en/reservation/xTs17c#checkin=2023-10-21&checkout=2023-11-04"
text_to_search = "Viajero Oaxaca is not operating yet."

driver.get(url)
time.sleep(5)

# Parse HTML of the page with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Search for the text
if text_to_search in soup.text:
    print("Text found!")
else:
    print("Text not found!")

# Close the driver
driver.quit()
