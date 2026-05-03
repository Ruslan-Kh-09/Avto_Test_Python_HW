from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

wedsite = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wedsite.get('https://ya.ru')

url = wedsite.current_url

print(url)

wedsite.quit()