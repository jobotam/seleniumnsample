from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=chrome_options)

driver.get('https://www.mrmiles.hk/mco/')
print(driver.title)
driver.quit()