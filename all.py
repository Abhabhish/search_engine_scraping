from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait=WebDriverWait(driver,10)

def bing(img_url):
    driver.get(f'https://www.bing.com/images/searchbyimage?cbir=ssbi&imgurl={img_url}')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@alt, 'See related image detail.')]")))
    related_images = driver.find_elements(By.XPATH,"//img[contains(@alt, 'See related image detail.')]")

    related_image_urls = []
    for image in related_images:
        if image.get_attribute('src').startswith('https://'):
            related_image_urls.append(image.get_attribute('src'))
    return related_image_urls

def google_lense(img_url):
    driver.get(f'https://lens.google.com/uploadbyurl?url={img_url}')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@class, 'wETe9b jFVN1')]")))
    related_images = driver.find_elements(By.XPATH,"//img[contains(@class, 'wETe9b jFVN1')]")
    
    related_image_urls = []
    for image in related_images:
        if image.get_attribute('src').startswith('https://'):
            related_image_urls.append(image.get_attribute('src'))
    return related_image_urls

def yandex(img_url):
    driver.get(f'https://yandex.com/images/search?rpt=imageview&url={img_url}')
    similar_btn = driver.find_element(By.XPATH,"//a[contains(@class, 'CbirNavigation-TabsItem CbirNavigation-TabsItem_name_similar-page')]")
    similar_btn.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@class, 'serp-item__thumb justifier__thumb')]")))
    related_images = driver.find_elements(By.XPATH,"//img[contains(@class, 'serp-item__thumb justifier__thumb')]")

    related_image_urls = []
    for image in related_images:
        if image.get_attribute('src').startswith('https://'):
            related_image_urls.append(image.get_attribute('src'))
    return related_image_urls



def naver(img_url):
    driver.get(f'https://s.search.naver.com/p/sbi/search.naver?where=sbi&query=smartlens&orgPath={img_url}')
    wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@alt, '이미지준비중')]")))
    related_images = driver.find_elements(By.XPATH,"//img[contains(@alt, '이미지준비중')]")

    related_image_urls = []
    for image in related_images:
        if image.get_attribute('src').startswith('https://'):
            url = image.get_attribute('src').split('&')[0]
            related_image_urls.append(url)
    return related_image_urls

def all(img_url):
    return {
        'bing':bing(img_url),
        'google_lense':google_lense(img_url),
        'yandex':yandex(img_url),
        'naver':naver(img_url)
    }

img_url = 'https://articlebucketgts.s3.ap-south-1.amazonaws.com/test/W4PHDI_12403.jpg'
response = all(img_url)

with open('response.json','w',encoding='utf-8') as f:
    json.dump(response,f,indent=4,ensure_ascii=False)