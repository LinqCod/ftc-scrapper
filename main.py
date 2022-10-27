from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://stat.customs.gov.ru/unload")

month_amount = 5
# level_index:
# 1 - 2 chars
# 2 - 4 chars
# 3 - 6 chars
# 4 - 8 chars
# 5 - 10 chars
level_index = 5

# Choosing months to get info
driver.find_element(By.CLASS_NAME, 'css-1wa3eu0-placeholder').click()
months = driver.find_element(By.CLASS_NAME, 'css-26l3qy-menu').find_elements(By.CSS_SELECTOR, '*')[0] \
    .find_elements(By.CSS_SELECTOR, '*')

month_count = 0
for m in months:
    if month_count > month_amount:
        break
    m.click()
    month_count += 1

# Closing drop-list
driver.find_element(By.CLASS_NAME, 'Select__control_active').click()

# Choosing level to get info
driver.find_element(By.CLASS_NAME, 'UnloadForm__tnvedLevel').click()
driver.find_element(By.CLASS_NAME, 'css-26l3qy-menu').find_elements(By.CSS_SELECTOR, '*')[level_index].click()

# Submit button for downloading csv file (1 index for DBF format)
download_button = driver.find_element(By.CLASS_NAME, 'UnloadForm__submit').find_elements(By.CSS_SELECTOR, '*')[2]
download_button.click()
