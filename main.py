from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# set chrome options and start chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

# login
driver.get('https://bbs.yamibo.com/member.php?mod=logging&action=login')
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys('ArtemisK')
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys('D5YPgaMCd.VA9nQ')
driver.find_element(By.CSS_SELECTOR, "button[name='loginsubmit']").click()

# wait for login
print('Waiting for login...')
while True:
    if driver.current_url == 'https://bbs.yamibo.com/':
        break
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
