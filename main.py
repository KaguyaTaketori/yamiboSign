import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
# username and password are stored in environment variables in .env file
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
print('Username: ' + username)
print('Password: ' + password)
driver.get('https://bbs.yamibo.com/member.php?mod=logging&action=login')
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys(username)
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
driver.find_element(By.CSS_SELECTOR, "button[name='loginsubmit']").click()


# wait for login success
print('Waiting for login...')
# wait for ten seconds
driver.implicitly_wait(10)
# check whether login success
if driver.current_url != 'https://bbs.yamibo.com/':
    print('Login failed!')
    driver.quit()
    exit(1)
else:
    print('Login success!')

# sign
driver.get('https://bbs.yamibo.com/plugin.php?id=zqlj_sign')
sign_button = driver.find_element(By.CSS_SELECTOR, "#wp > div.ct2.cl > div.sd > div.bm.signbtn.cl > a")
if sign_button.text != '今日已打卡':
    sign_button.click()
    print('Signed!')
else:
    print('Already signed!')

# quit
driver.quit()
