import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\Users\\abokka\\Documents\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
phoneNames= driver.find_elements(By.XPATH,"//app-card-list[@class='row']/app-card/div/div[1]/h4/a")

products = driver.find_elements(By.XPATH,"//app-card-list[@class='row']/app-card/div")
for product in products:
    name = product.find_element(By.XPATH,"div[1]/h4/a")
    if (name.text == "Blackberry"):
        product.find_element(By.XPATH,"div[2]/button").click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
# wait.until(expected_conditions.presence_of_element_located()

driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)
print(driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text)

successMsg = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in successMsg

driver.get_screenshot_as_file("ss.png")