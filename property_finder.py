from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
zillow_web_page = response.text

soup = BeautifulSoup(zillow_web_page, "html.parser")
article_tags = soup.findAll(name="div", class_="StyledPropertyCardDataWrapper")

class Property:
    def __init__(self):
        self.address = None
        self.price = None
        self.link = None

properties = []

for article in article_tags:
    property_instance = Property()  
    property_instance.address = article.find(name="address").get_text()
    property_instance.link = article.find(attrs={"data-test": "property-card-link"}).get('href')
    property_instance.price = article.find(attrs={"data-test": "property-card-price"}).get_text()
    properties.append(property_instance)

for i in properties:
    print(f"\n\naddress: {i.address}")
    print(f"link: {i.link}")
    print(f"price: {i.price}\n")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/rib1qUK43RbQJWMq7")

for property_instance in properties:
    address_form = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    address_form.send_keys(property_instance.address)
    price_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_form.send_keys(property_instance.price)
    link_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_form.send_keys(property_instance.link)
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a'))
    )

    submit_another = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()




driver.close()