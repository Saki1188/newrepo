from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:\Users\drivers\chromedriver_win32\chromedriver.exe')
#driver = webdriver.chrome("C:\\Users\\drivers\\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.linkedin.com/notifications/")
print(driver.title)   #prints the page title




#NEW FILE
driver.close()   #closes the page