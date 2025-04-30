from selenium import webdriver
#from selenium.webdriver.safari.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Chrome()
#mendapatkan halaman utama
driver.get("https://app.hive.com/join")

time.sleep(10)

#masukkan semua isian pada halaman
sign_up= driver.find_element(By.XPATH, '//*[@id="mounter-react-root"]/div/div/div/div/div[2]/div/div/div/button').click()

work_email = driver.find_element(By.XPATH, '//*[@id="email"]')
work_email.send_keys('igustiayu010405@gmail.com') #gunakkan email yang berbeda setiap kali akan run 

#klik tombol next
#continue_email= driver.find_element(By.ID, 'mounter-react-root').click()
wait = WebDriverWait(driver, 15)
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//form//button[contains(text(), "Continue")]')))
continue_button.click()

#masukkan semua isian yang ada
first_name = driver.find_element(By.XPATH, '//*[@id="firstName"]')
first_name.send_keys('deyren')

last_name = driver.find_element(By.XPATH, '//*[@id="lastName"]')
last_name.send_keys('nathaniel')

phone_number = driver.find_element(By.XPATH, '//*[@id="phone"]')
phone_number.send_keys('082313457568')

password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('123456')

#klik next
wait = WebDriverWait(driver, 15)
next2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mounter-react-root"]/div/div/div/div/div[3]/div/div/form/button')))
next2.click()

enter_name = wait.until(EC.presence_of_element_located((By.ID, 'organizationName')))
enter_name.send_keys('deyrenathaniel')

wait = WebDriverWait(driver, 15)
next3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mounter-react-root"]/div/div/div/div/div[3]/div/div/form/div[3]/button')))
next3.click()

#pilih salah satu tombol jumlah group
group_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@data-test-id="10"]')))
group_option.click()

#klik next
next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test-id="next-onboarding-stage-button"]')))
next_button.click()

# masukkan semua isian pada halaman "Let's customize your hive"
marketing_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@data-test-id="MARKETING_TEAM_TEMPLATE"]')))
driver.execute_script("arguments[0].scrollIntoView(true);", marketing_label)
marketing_label.click()

# Tunggu sampai tombol "Next" aktif (tidak lagi disabled)
wait.until(lambda d: d.find_element(By.XPATH, '//button[@data-test-id="next-onboarding-stage-button"]').is_enabled())

#klik next
next6 = driver.find_element(By.XPATH, '//button[@data-test-id="next-onboarding-stage-button"]')
next6.click()

# Klik tombol "Skip" 
skip_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test-id="skip-onboarding-stage-button"]')))
skip_button.click()

wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-test-id="messaging-stage"]')))

# klik "Use Hive messaging"
messaging_label = wait.until(EC.presence_of_element_located((By.XPATH, '//label[@data-test-id="hive-messaging"]')))

# Gunakan JavaScript untuk klik
driver.execute_script("arguments[0].click();", messaging_label)

# klik 'Start using Hive' 
wait.until(lambda d: d.find_element(By.XPATH, '//button[@data-test-id="next-onboarding-stage-button"]').is_enabled())
start_button = driver.find_element(By.XPATH, '//button[@data-test-id="next-onboarding-stage-button"]')
start_button.click()


time.sleep(15)
driver.quit