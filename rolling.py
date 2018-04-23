from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
import time
import os

def auto_roll():
    browser = webdriver.Chrome("/home/user/chromedriver") # Your webdriver path

    browser.get("https://freebitco.in/")
    browser.find_element_by_class_name("login_menu_button").click()

    elem = browser.find_element_by_id("login_form_btc_address")
    elem.send_keys("YourMail") # Your email or btc address
    elem = browser.find_element_by_id("login_form_password")
    elem.send_keys("YourPassword") # Your password
    # Try to close banner message
    try:
        browser.find_element_by_id("cc_banner").click()
    except:
        pass
    browser.find_element_by_id("login_button").click()

    time.sleep(3) # Wait for page loading
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

auto_roll()
sched = BlockingScheduler()
sched.add_job(auto_roll, 'interval', hours=1)
sched.start()
