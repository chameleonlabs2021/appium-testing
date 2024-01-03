#!/usr/bin/env python3.9
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# Create an instance of AppiumOptions
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "rahulemulator"
options.automation_name = "UiAutomator2"
options.app = "/Users/rahulpoolanchalil/AndroidStudioProjects/SimpleApp/app/build/outputs/apk/androidTest/debug/app-debug-androidTest.apk"
options.app_package = "com.example.loginapp"
options.app_activity = "MainActivity"

# Connect to Appium server
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

try:
    # Add an implicit wait
    driver.implicitly_wait(10)
    
    # Locate the button and click it
    # Since the XML doesn't show a unique resource-id for the button, you can use other locators like text
    button = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Click Me']")
    button.click()
    print("Clicked the button")
    # Optionally, add a small delay to see the result
    import time
    time.sleep(10)

finally:
    # Always quit the driver to close the app
    driver.quit()
