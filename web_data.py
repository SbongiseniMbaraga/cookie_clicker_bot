from selenium import webdriver

website = "http://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "C:\Sbos Programs\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(website)
