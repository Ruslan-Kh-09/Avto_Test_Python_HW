#from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver.maximize_window()


driver.get('https://yandex.ru')
#driver.get('https://www.tbank.ru/invest/portfolio/')

#driver.save_screenshot('./11.png')

#driver.set_window_size(700, 700)
#
# for x in range(1, 10):
#     driver.back()
#     driver.forward()


#sleep(10)