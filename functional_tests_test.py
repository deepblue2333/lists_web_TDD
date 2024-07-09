import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service


browser = webdriver.Edge()
browser.get("http://localhost:8000")
assert 'The install worked successfully! Congratulations!' in browser.title
time.sleep(10)

