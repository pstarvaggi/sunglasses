from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import re
import time

driver = webdriver.Chrome()

driver.get("https://www.sunglasshut.com/us/Sunglasses-Brands")

csv_file = open('urls.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)


for i in range(3):
	try:
		wait_button = WebDriverWait(driver, 10)
		more_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,
									'//*[@id="skip-nav-contents"]/div[4]/button')))
		more_button.click()

	except Exception as e:
		print(e)
		break

	time.sleep(2)



wait_url = WebDriverWait(driver, 10)
urls = wait_url.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="sgh-col sm:w-1/3 w-full"]')))

for url in urls:
	# url_dict = {}
	# driver.execute_script("arguments[0].scrollIntoView();", url)

	# title = url.find_element_by_xpath('./article/a').get_attribute('data-description')
	# text = url.find_element_by_xpath('./article/a').get_attribute('href')

	# url_dict['title'] = title
	# url_dict['text'] = text

	# writer.writerow(url_dict.values())
	url.find_element_by_xpath('./article/a').click()

csv_file.close()
driver.close()