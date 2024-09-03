from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element(By.ID, value='money')

money_value = 0
start = time.time()

def most_expensive_item(money_val):
    cursor_price = int(driver.find_element(By.CSS_SELECTOR, value='#buyCursor b').text.split()[2])
    print(f"cursor_price: {cursor_price}")
    grandma_price = int(driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b').text.split()[2])
    print(f"grandma_price: {grandma_price}")
    factory_price = int(driver.find_element(By.CSS_SELECTOR, value='#buyFactory b').text.split()[2])
    print(f"factory_price: {factory_price}")
    mine_price = int((driver.find_element(By.CSS_SELECTOR, value='#buyMine b').text.split()[2]).replace(",", ""))
    print(f"mine_price: {mine_price}")
    shipment_price = int((driver.find_element(By.CSS_SELECTOR, value='#buyShipment b').text.split()[2]).replace(",", ""))
    print(f"shipment_price: {shipment_price}")
    alchemyLab_price = int((driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b').text.split()[3]).replace(",", ""))
    print(f"alchemy_price: {alchemyLab_price}")
    portal_price = int((driver.find_element(By.CSS_SELECTOR, value='#buyPortal b').text.split()[2]).replace(",", ""))
    print(f"portal_price: {portal_price}")
    timeMachine_price = int((driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b').text.split()[3]).replace(",", ""))
    print(f"timemachine_price: {timeMachine_price}")

    if money_val >= timeMachine_price:
        return "#buyTime machine b"
    if money_val >= portal_price:
        return "#buyPortal b"
    if money_val >= alchemyLab_price:
        return "buyAlchemy lab b"
    if money_val >= shipment_price:
        return "#buyShipment b"
    if money_val >= mine_price:
        return "#buyMine b"
    if money_val >= factory_price:
        return "#buyFactory b"
    if money_val >= grandma_price:
        return "#buyGrandma b"
    if money_val >= cursor_price:
        return "#buyCursor b"

cookie = driver.find_element(By.ID, value='cookie')

while True:
    cookie.click()
    end = time.time()
    if int(end - start) == 5:
        start = end
        money_value = int(money.text.replace(',', ''))
        print(money_value)
        id = most_expensive_item(money_value)
        print(id)
        item = driver.find_element(By.CSS_SELECTOR, value=id)
        item.click()


driver.close()