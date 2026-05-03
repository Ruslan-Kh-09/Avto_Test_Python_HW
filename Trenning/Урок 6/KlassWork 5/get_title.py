from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

wedsite = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wedsite.get('https://rzd.ru')

current_title = wedsite.title

print(current_title)

wedsite.quit()