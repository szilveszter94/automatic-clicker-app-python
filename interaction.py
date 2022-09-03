from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# set time cycle variable
time_cycle = 5
# give the chrome driver location (you can download it from "https://chromedriver.chromium.org/")
chrome_driver_path = "YOUR CHROMEDRIVER LOCATION PATH"
# use Chrome driver
service_path = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service_path)
# get the cookie clicker page
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# find the cookie element
cookie_element = driver.find_element(By.ID, "cookie")

# get all upgrade ids
upgrade_id = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrade_ids = [i.get_attribute("id") for i in upgrade_id]

# set a time cycle
timeout = time.time() + time_cycle
# set the timer for 5 minutes
five_min = time.time() + 60 * 5

while True:
    # start the clicker
    cookie_element.click()
    if time.time() > timeout:
        # every cicle the driver checks the upgrade price
        upgrade_price = driver.find_elements(By.CSS_SELECTOR, "#store b")

        # formatting upgrade price and insert into an array
        upgrade_cost = []
        for i in upgrade_price:
            costs = i.text.split("-")
            if "" not in costs:
                cost = int(costs[1].replace(",", ""))
                upgrade_cost.append(cost)

        # create a dict with upgrade prices and the corresponding ids
        upgrade_element = {}
        for i in range(len(upgrade_cost)):
            upgrade_element[upgrade_cost[i]] = upgrade_ids[i]

        # get the actual amount of money
        cookie_amount = driver.find_element(By.ID, "money")
        if "" in cookie_amount.text:
            cookie_amount = cookie_amount.text.replace(",", "")
        cookie_count = int(cookie_amount)

        # get the affordable upgrades
        affordable_upgrade = {}
        for cost, ids in upgrade_element.items():
            if cookie_count > cost:
                affordable_upgrade[cost] = ids
        try:
            # try to buy the most valuable and affordable upgrade
            highest_affordable = max(affordable_upgrade)
            purchase_id = affordable_upgrade[highest_affordable]
            driver.find_element(By.ID, purchase_id).click()
        except ValueError:
            pass
        # restart time cycle
        timeout = time.time() + time_cycle
