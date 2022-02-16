from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')


chrome_browser.maximize_window()

chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

show_message_button = chrome_browser.find_element_by_class_name("btn-default")
#underneath is the selector using the css to select all the children button of the specified id
# user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')

print(show_message_button.get_attribute("innerHTML"))

# lightbox_close_x = chrome_browser.find_element_by_class_name("at-cv-lightbox-close")
# lightbox_close_x.click()

chrome_browser.find_element_by_id('user-message').send_keys('初めまして')

show_message_button.click()

chrome_browser.close()
# chrome_browser.close()
# chrome_browser.quit()