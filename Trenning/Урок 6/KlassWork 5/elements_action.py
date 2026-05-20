#from time import sleep
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.support.expected_conditions import element_located_to_be_selected
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get('https://ya.ru')

element = browser.find_element(By.CSS_SELECTOR, '#text')
element.clear()
element.send_keys("test skypro")

browser.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

sleep(5)

browser.find_element(By.CSS_SELECTOR, ".DistributionButtonClose").click()

sleep(5)

browser.quit()
