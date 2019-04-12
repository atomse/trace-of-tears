#!/usr/bin/env python3
import os
import time
import random
import logging

from selenium import webdriver;
from selenium.webdriver.common.by import By;
from selenium.webdriver.support.wait import WebDriverWait;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

fireFoxOptions = webdriver.FirefoxOptions();
# fireFoxOptions.set_preference("network.proxy.type", 0);
fireFoxOptions.set_headless(); # headless

browser = webdriver.Firefox(firefox_options=fireFoxOptions);
# browser = webdriver.Remote("http://127.0.0.1:4444",desired_capabilities=webdriver.DesiredCapabilities.FIREFOX, options=fireFoxOptions)

wait = WebDriverWait(browser,10)
# browser.set_page_load_timeout(5)
# browser.set_script_timeout(5)

def dashangleihen():
    browser.get('http://tianya.cn')
    
    # normal login
    browser.find_element_by_class_name('normal-login-tab').click()
    username = browser.find_element_by_id('vwriter')
    username.send_keys('474029625')
    password = browser.find_element_by_id('vpassword')
    password.send_keys('zyx474029625')
    login = browser.find_element_by_class_name('loginWin-submit-btn')
    login.click()
    
    # switch to Leihenchunyu
    browser.get('http://www.tianya.cn/12310752')
    browser.find_element_by_xpath('//span[@class="subtitle"]/a[1]').click()
    browser.switch_to.window(browser.window_handles[-1])
    browser.find_element_by_xpath('//td[@class="p-title"]/a[1]').click()
    browser.switch_to.window(browser.window_handles[-1])
    
    # dashang frame
    browser.find_element_by_id('dashang_btn').click()

    # dashang button
    browser.switch_to.frame('iframeArea')
    dsbtn = browser.find_element_by_class_name('dsBtnSubmit')
    
    if not dsbtn.text == '立即打赏(1贝)':
        print('Error: text: {0}'.format(dsbtn.text))
    # dsbtn.click()
    return browser


if __name__ == '__main__':
    dashangleihen()
