import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# define css selectors and other variables
wait_time = 10
home_url = 'https://bbs.yamibo.com/'
login_url = 'https://bbs.yamibo.com/member.php?mod=logging&action=login'
username_css_selector = "input[name='username']"
password_css_selector = "input[name='password']"
login_button_css_selector = "button[name='loginsubmit']"
sign_button_css_selector = "#wp > div.ct2.cl > div.sd > div.bm.signbtn.cl > a"

# set chrome options and start chrome
service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options, service=service)
print('Chrome started.')
# print Chrome version
print('Chrome version: ' + driver.capabilities['browserVersion'])
# print Chrome driver version
print('Chrome driver version: ' + driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0])

# login
# username and password are stored in GitHub secrets
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
driver.get(login_url)
driver.find_element(By.CSS_SELECTOR, username_css_selector).send_keys(username)
driver.find_element(By.CSS_SELECTOR, password_css_selector).send_keys(password)
driver.find_element(By.CSS_SELECTOR, login_button_css_selector).click()


# wait for login success
print('Waiting for login...')
# wait for ten seconds

try:
    WebDriverWait(driver, wait_time).until(
        EC.url_to_be(home_url)
    )
    print('Login success!')
except Exception as e:
    print('Login failed!')
    print(e)


# sign
driver.get('https://bbs.yamibo.com/plugin.php?id=zqlj_sign')
sign_button = driver.find_element(By.CSS_SELECTOR, sign_button_css_selector)
if sign_button.text != '今日已打卡':
    sign_button.click()
    print('Signed!')
else:
    print('Already signed!')

# quit
driver.quit()
