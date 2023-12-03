import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_argument("C:\\Users\\Webhouse\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
service = Service(executable_path="D:\\chromedriver-win32\\chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()


def selector_by_name(d, name, text):
    wait = WebDriverWait(d, 10)
    wait.until(EC.element_to_be_clickable((By.NAME, name))).send_keys(text)


def button_click_by_xpath(d, xpath):
    element = d.find_element(By.XPATH, xpath)
    ActionChains(d).click(element).perform()


def play_video(d, xpath):
    video = d.find_element(By.XPATH, xpath)
    video.click()


def exit_platform(d):
    while True:
        try:
            time.sleep(3)
            button_click_by_xpath(d, f'/html/body/div/div[1]/main/div/div[2]/div[2]/button')
        except NoSuchElementException:
            return ''
        except Exception as e:
            print(e)
            continue


def click_by_link_text(d, text):
    d.find_element(By.LINK_TEXT, text).click()


driver.get('https://app.filimo.school/auth')

selector_by_name(driver, 'phone', '09191581676')
button_click_by_xpath(driver, '''/html/body/div[1]/div[1]/div/form/div[2]/button''')

selector_by_name(driver, 'password', 'Moh2921031')
button_click_by_xpath(driver, '''/html/body/div[1]/div[1]/div/form/div[2]/button''')

exit_platform(driver)


def get_video_duration_element(d, xpath):
    try:
        return d.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return None


def click_buttons_loop(d):
    while True:
        try:
            button_click_by_xpath(d, '/html/body/div/div[1]/div/div[2]/button')
            time.sleep(3)
            button_click_by_xpath(d, '/html/body/div/div[2]/div/div/div/div[3]/button')
            time.sleep(3)
            button_click_by_xpath(d, '/html/body/div/div[1]/div[2]/div/div/div/div[3]/div/div[1]/button[1]')
            time.sleep(float(get_video_duration_element) / 60 + 10)
            print(get_video_duration_element)
        except Exception as e:
            print(e)


while True:
    try:
        driver.get('https://app.filimo.school/course/8vzqp/chapter/p1ol6/path')
        time.sleep(5)
        play_video(driver, '/html/body/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div[3]/video')
        time.sleep(100)
        click_buttons_loop(driver)
    except Exception as e:
        print(e)
