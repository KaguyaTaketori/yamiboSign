import os
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

wait_time = 10

# Read configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

url = {
    'home_url': config.get('URL', 'home_url'),
    'login_url': config.get('URL', 'login_url'),
    'sign_url': config.get('URL', 'sign_url')
}

css_selector = {
    'username_css_selector': config.get('CSS_SELECTOR', 'username_css_selector'),
    'password_css_selector': config.get('CSS_SELECTOR', 'password_css_selector'),
    'login_button_css_selector': config.get('CSS_SELECTOR', 'login_button_css_selector'),
    'sign_button_css_selector': config.get('CSS_SELECTOR', 'sign_button_css_selector')
}

def set_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=service)
    print('Chrome options and service set.')
    print('Chrome version: ' + driver.capabilities['browserVersion'])
    print('Chrome driver version: ' + driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])
    return driver

def find_element_and_send_keys(driver, css_selector, keys):
    try:
        driver.find_element(By.CSS_SELECTOR, css_selector).send_keys(keys)
    except Exception as e:
        print(f"Failed to find element with CSS selector {css_selector}")
        print(e)

def login(driver, username, password):
    driver.get(url['login_url'])
    find_element_and_send_keys(driver, css_selector['username_css_selector'], username)
    find_element_and_send_keys(driver, css_selector['password_css_selector'], password)
    driver.find_element(By.CSS_SELECTOR, css_selector['login_button_css_selector']).click()
    print('Waiting for login...')
    try:
        WebDriverWait(driver, wait_time).until(EC.url_to_be(url['home_url']))
        print('Login success!')
    except Exception as e:
        print('Login failed!')
        print(e)
        return False
    return True

def sign(driver):
    driver.get(url['sign_url'])
    sign_button = driver.find_element(By.CSS_SELECTOR, css_selector['sign_button_css_selector'])
    if sign_button.text != '今日已打卡':
        sign_button.click()
        print('Signed!')
    else:
        print('Already signed!')

if __name__ == '__main__':
    username = os.getenv('USERNAME', '')
    password = os.getenv('PASSWORD', '')
    if not username or not password:
        print('Username or password not set in environment variables.')
        exit(1)
    driver = set_chrome_driver()
    if login(driver, username, password):
        sign(driver)
    driver.quit()