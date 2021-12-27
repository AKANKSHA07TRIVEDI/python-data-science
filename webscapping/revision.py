from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome()

driver.maximize_window()


url='https://www.myntra.com/handbags/forever-glam-by-pantaloons/forever-glam-by-pantaloons-black-mobile-sling-bag/14766630/buy'
home_url ='www.myntra.com/h'


driver.get(home_url)

search_box =driver.find_element(By.NAME,"similar-container")
search_box.send_keys('Black Mobile Sling Bag', Keys.ENTER)
print(driver.title)
row =driver.find_element(By.CLASS_NAME, 'Black Mobile Sling Bag')
for item in rows:
    print(item.text)


driver.close()

driver.close()
