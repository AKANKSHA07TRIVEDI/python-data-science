from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome()

driver.maximize_window()


url="https://www.amazon.in/HP-PC-21-5-Inch-Desktop-22-df0202in/dp/B09HRXTGGJ"
home_url ="https://www.amazon.in"


driver.get(home_url)

search_box =driver.find_element(By.NAME,'field-keywords')
search_box.send_keys('Aser Laptop', Keys.ENTER)
print(driver.title)
row =driver.find_element(By.CLASS_NAME, 'a-size-mini','a-size-mini')
for item in rows:
    print(item.text)
#rows =driver.find_element(By.XPATH, "//H2[@ID='a-size-mini']'")

#try:
    #ele = driver.find_element(By.TAG_NAME,'h1')
    #print(ele.text)

driver.close()

driver.close()
