import evdev
import datetime
import requests
import settings
import chromedriver_binary
from evdev import InputDevice, categorize, ecodes
from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

ANDROID_EVENT_CODE = 28
dev_path = ""
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

def clock_out():
    auth_kot()
    sleep(1)
    while True:
        if driver.find_element(By.ID, "location_area").text == "位置情報取得済み":
            break
        sleep(1)

    driver.find_element(By.CLASS_NAME, "down-arrow").click()
    requests.post(settings.ATTENDANCE_DEV_URL, json={'text': '満江退勤します'})

def main():
    while(True):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if("Shutter" in device.name):
                dev_path = device.path

        if (dev_path == "") :
            sleep(1)
        else : break

    dev = InputDevice(dev_path)
    is_android = 0
    is_ios = 0
    for event in dev.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            # 1:KEYDOWN
            if event.value == 1:
                if event.code == IOS_EVENT_CODE:
                    is_android=1

            # 0:KEYUP
            if event.value == 0:
                if is_ios == 1 :
                    is_ios = 0
                    continue

                # finished long push
                if old != 0 and time() - old > 0.5:
                    if is_android :
                        is_android = 0
                        is_ios = 1

                    old = 0
                    continue

                if is_android:
                    clock_out()
                    is_android = 0
                    is_ios = 1
                else:
                    clock_in()

            # started long push
            if event.value == 2 and old == 0:
                old = time()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
