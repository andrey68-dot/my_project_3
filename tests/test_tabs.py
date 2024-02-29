from selenium.webdriver.common.by import By

def test_tabs(browser):
    browser.get('https://magento.softwaretestingboard.com/what-is-new.html')
    women_button = browser.find_element(By.ID, 'ui-id-4').click()
    men_button = browser.find_element(By.ID, 'ui-id-5').click()
    gear_button = browser.find_element(By.ID, 'ui-id-6').click()

