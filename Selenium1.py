from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

chromedriver = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path=chromedriver, options=options)
driver.get("https://www.google.com")
print(driver.title)

search_bar = driver.find_element_by_name("q")
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
