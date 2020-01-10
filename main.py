import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'C:\Users\setze\OneDrive\Bureau\chromedriver.exe')
driver.get("https://cas.mon-ent-occitanie.fr/login?selection=TOULO-ENT_parent_eleve&service=https%3A%2F%2Fcite-mendes-france.mon-ent-occitanie.fr%2Fsg.do%3FPROC%3DIDENTIFICATION_FRONT&submit=Valider")
logid = driver.find_element_by_xpath('//*[@id="username"]')
logid.send_keys("ewen.setze")
logpsw = driver.find_element_by_xpath('//*[@id="password"]')
logpsw.send_keys("Shimakaze65")

vali = driver.find_element_by_xpath('//*[@id="button-submit"]')
vali.send_keys(Keys.ENTER)

time.sleep(3)
goliste = driver.find_element_by_xpath('/html/body/main/div/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/p/a')
goliste.click()



