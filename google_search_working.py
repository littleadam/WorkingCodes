from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# Navigate to the Google website
driver.get("https://www.google.com")

# Find the search input field by its name attribute ("q" for Google search)
#search_input = driver.find_element_by_name("q")

# Find the search input element by name (assuming it has the name "q" in Google)
search_input = driver.find_element(By.NAME, "q")

# Enter the search query
search_input.send_keys("sl vs eng")

# Simulate pressing the "Enter" key to initiate the search
search_input.send_keys(Keys.RETURN)

# Wait for a few seconds to allow the search results to load (you can adjust the duration as needed)
driver.implicitly_wait(5)

# Retrieve and print the search results
search_results = driver.find_elements(By.CLASS_NAME, "tF2Cxc")
for result in search_results:
    print(result.text)

# Close the browser window
driver.quit()

