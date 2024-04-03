from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait=WebDriverWait(driver,10)


driver.get('https://lens.google.com/uploadbyurl?url=https://articlebucketgts.s3.ap-south-1.amazonaws.com/test/W4PHDI_12403.jpg')
wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@class, 'wETe9b jFVN1')]")))
related_images = driver.find_elements(By.XPATH,"//img[contains(@class, 'wETe9b jFVN1')]")
for image in related_images:
    if image.get_attribute('src').startswith('https://'):
        print(image.get_attribute('src'))
