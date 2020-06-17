from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver.get("https://www.google.com")
driver.maximize_window()
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("design engineer jobs")
search_bar.send_keys(Keys.RETURN)
post = driver.find_element_by_partial_link_text("Indeed")

post.click()
#print(driver.current_url)

location = driver.find_element_by_xpath('//*[@id="where"]')
time.sleep(2)
location.send_keys("Grand Rapids")
find_button = driver.find_element_by_id("fj")
find_button.click()
time.sleep(5)
driver.find_element_by_id("popover-close-link").click()
driver.switch_to.default_content()

#link = driver.current_url
#print(link)

#source = requests.get(link).text

#soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

csv_file = open('indeed_mech_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Company', 'Summary', 'Link'])

for x in driver.find_elements_by_class_name("jobsearch-SerpJobCard"):

    elem = x.find_element_by_tag_name('h2 a')
    href = elem.get_attribute('href')
    title = elem.text
    company = x.find_element_by_class_name('company').text
    summary = x.find_element_by_class_name('summary').text

    print(title)
    print(company)
    print(summary)
    print(href)
    print()

    csv_writer.writerow([title, company, summary, href])

csv_file.close()




""""""



"""for title in soup.find_all("div", {"class": "title"})):
    headline = title.h2.text
    print(headline)
    
    class="jobsearch-SerpJobCard unifiedRow row result clickcard"
"""