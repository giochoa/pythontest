from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')


chrome_browser.maximize_window()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

show_message_button = chrome_browser.find_element_by_class_name("btn-default")

print(show_message_button.get_attribute("innerHTML"))

# lightbox_close_x = chrome_browser.find_element_by_class_name("at-cv-lightbox-close")
# lightbox_close_x.click()

chrome_browser.find_element_by_id('user-message').send_keys('初めまして')

show_message_button.click()
