from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def auto_roll():

    browser = webdriver.Chrome("Your Webdriver Path") # Your webdriver path
    browser.get("https://freebitco.in/")

    #wait page and alert loading
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='allow_button pushpad_allow_button'])[1]")))
    # Try to close allow alert
    try:
        allow_btn = "(//div[@class='allow_button pushpad_allow_button'])[1]"
        browser.find_element_by_xpath(allow_btn).click()
    except:
        pass

    browser.find_element_by_class_name("login_menu_button").click()

    elem = browser.find_element_by_id("login_form_btc_address")
    elem.send_keys("Your Mail") # Your email or btc address
    elem = browser.find_element_by_id("login_form_password")
    elem.send_keys("Your Password") # Your password

    # Try to close banner message
    try:
        browser.find_element_by_id("cc_banner").click()
    except:
        pass

    browser.find_element_by_id("login_button").click()
    time.sleep(3) # Wait for page loading

    #wait page and alert loading
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='allow_button pushpad_allow_button'])[1]")))
    # Try to close allow alert
    try:
        allow_btn = "(//div[@class='allow_button pushpad_allow_button'])[1]"
        browser.find_element_by_xpath(allow_btn).click()
    except:
        pass

    # Try to close message
    try:
        browser.find_element_by_class_name("cc_btn").click()
    except:
        pass

    # Scroll to buttom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    try:
        browser.find_element_by_id("free_play_form_button").click()
        print("Clicked!")
    except:
        browser.find_element_by_id("time_remaining")
        print("Need to wait.")

    time.sleep(2)
    browser.close()

    sched = BlockingScheduler()
    sched.add_job(auto_roll, 'interval', hours=1)
    sched.start()

auto_roll()
