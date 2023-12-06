from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

# PATH = "./chromedriver.exe"

# driver = webdriver.Chrome()
# driver.get("https://www.youtube.com/")
# sleep(10)
# driver.quit()

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(service=service,options=options)

# driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys('pen')
search.send_keys(Keys.RETURN)


print(driver.title)

# driver.find_element('body').send_keys(Keys.COMMAND +'t')
# driver.switch_to.new_window()
# driver.get("http://www.google.com/")