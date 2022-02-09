import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("C:\\Users\\abokka\\Documents\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.dtdc.in/Support.asp")
driver.maximize_window()

driver.get_screenshot_as_file("sandeep.png")
time.sleep(3)
print(driver.find_element(By.XPATH,"//a[text()='Track Your Shipment']").text)

wait = WebDriverWait(driver,5)
element = wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='Track Your Shipment']")))


parentWindow = driver.current_window_handle
driver.find_element(By.XPATH,"//a[text()='Track Your Shipment']").click()
ac = ActionChains(driver)
ac.key_down(Keys.CONTROL).click(driver.find_element(By.XPATH,"//a[text()='Sitemap']")).perform()

chaildWindows = driver.window_handles

for chaildWindow in chaildWindows:
    if(parentWindow != chaildWindow ):
        driver.switch_to.window(chaildWindow)
        print("window title is : ", driver.title)

driver.switch_to.window(parentWindow)

driver.switch_to.window(chaildWindow)
print("chaild window name is :" , driver.title)
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])