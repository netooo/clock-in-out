import datetime
import requests
import settings
import chromedriver_binary
from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def auth_kot():
    driver.get(settings.KOT_TOP_URL)
    driver.find_element(By.ID, "id").send_keys(settings.KOT_ID)
    driver.find_element(By.ID, "password").send_keys(settings.KOT_PASS)
    sleep(1)
    driver.find_element(By.CLASS_NAME, "btn-control-message").click()


def clock_in():
    auth_kot()
    sleep(1)
    while True:
        if driver.find_element(By.ID, "location_area").text == "位置情報取得済み":
            break
        sleep(1)

    driver.find_element(By.CLASS_NAME, "up-arrow").click()
    requests.post(settings.ATTENDANCE_DEV_URL, json={'text': '満江業務開始します'})


def main():
    clock_in()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
