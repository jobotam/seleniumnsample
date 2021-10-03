from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
chrome_options.add_argument("--no-sandbox")
executable_path = '/usr/local/bin/chromedriver'
path ="https://forms.office.com/Pages/ResponsePage.aspx?id=jEDbJMinOk-P-RCGCkjSNfK_5HUi3ylNtnMcsso5a2NUM1VROFlHVlo0WktCSlJNRk5UTEE4T0RDNy4u"
# driver = webdriver.Chrome(".\chromedriver_win32\chromedriver.exe") # chromedriver version
driver = webdriver.Chrome(executable_path=executable_path, options=chrome_options) # Headless version
driver.get(path)
time.sleep(2)
email_input = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "i0116")))
# email_input =  driver.find_element_by_id('i0116')
# email_input = driver.find_elements_by_name("loginfmt")
email_input.send_keys("jobo.tam@ecloudvalley.com")
time.sleep(1)
driver.find_element_by_id('idSIButton9').click()
# print(email_input)
pwd_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "i0118")))
# pwd_input = driver.find_element_by_id('i0118')
pwd_input.send_keys("EfE%+xACW+U5") 
driver.find_element_by_id('idSIButton9').submit()
time.sleep(1)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "idSIButton9"))).click()
# driver.find_element_by_id('idSIButton9').click()
time.sleep(2)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "FormTitleId_titleAriaId")))
health_click = driver.find_element_by_name("r8c6542cab318414b90ac1f5b7a3edc4d")
actions_for_hc = ActionChains(driver)
actions_for_hc.click(health_click).perform()
time.sleep(1)
worksite_click = driver.find_element_by_name("rb91b02260ee14b37998b9b0d20d04649")
actions_for_ws = ActionChains(driver)
actions_for_ws.click(worksite_click).perform()
submit_button = driver.find_element_by_xpath("//button[@class='office-form-theme-primary-background office-form-theme-button office-form-bottom-button button-control light-background-button __submit-button__']")
actions_submit = ActionChains(driver)
actions_submit.click(submit_button).perform()
time.sleep(2)
print("done")
driver.quit()
