import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('C:\\Users\\jmak2\\Desktop\\ChromeDriver.exe')
driver.maximize_window()
'''
module for google login
can't get password to work
'''
driver.get('http://google.com')

click_login = driver.find_element_by_id('gb_70')
click_login.click()

sign_in = driver.find_element_by_id('identifierId')
sign_in.send_keys('jmak209@gmail.com')
sign_in.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

enter_pass = driver.find_element_by_xpath("//div[containts(@class, 'Xb9hP')]")
enter_pass.send_keys('testestest')
enter_pass.send_keys(Keys.RETURN)






# module for netflix login
# driver.get('http://www.netflix.com\login')


# sign_in = driver.find_element_by_id('lbl-email')
# sign_in.send_keys('jmak209@gmail.com')

# enter_pass = driver.find_element_by_id('lbl-password')
# enter_pass.send_keys('')#enter password here
# enter_pass.send_keys(Keys.RETURN)




#simple search module for google in chrome
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()