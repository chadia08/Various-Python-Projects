from selenium import webdriver
from operator import contains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

option = webdriver.ChromeOptions()
option.add_argument("user-data-dir=C:/Users/chadia/AppData/Local/Google/Chrome/User Data")
# Instancier un navigateur web (assurez-vous d'avoir installé le pilote du navigateur, par exemple, chromedriver)
service = Service("driver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=option)

# Ouvrir WhatsApp Web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,100)

target = 'Mamy' 
contact_path ='//span[contains(text(), "{target}")]'
sleep(100)

contact = wait.until(EC.presence_of_element_located((By.XPATH,contact_path)))
contact.click()
message_box_path ='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
message_box = wait.until(EC.presence_of_element_located((By.XPATH,message_box_path)))
text = "i love you my mom"
message_box.send_keys(text+Keys.ENTER)















# # Fermer le navigateur
# driver.quit()
