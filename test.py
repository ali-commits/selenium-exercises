from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the ChromeDriver service
service = Service()  # If chromedriver is in PATH

# Create a new Chrome driver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to the search engine
    driver.get("https://www.google.com")

    # Wait for the search box to be visible
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Enter a search query
    search_query = "Selenium WebDriver"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    # Print the title of the first search result
    first_result = driver.find_element(By.CSS_SELECTOR, "#search .g")
    print(f"First result title: {first_result.find_element(By.TAG_NAME, 'h3').text}")

    # Count and print the number of search results on the first page
    results = driver.find_elements(By.CSS_SELECTOR, "#search .g")
    print(f"Number of results on the first page: {len(results)}")

    # Wait for user input before closing the browser
    input("Press Enter to close the browser...")

finally:
    # Close the browser
    driver.quit()
