import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def before_scenario(context, scenario):
    print(f"\nSTARTING SCENARIO: {scenario.name}")

    browser = context.config.userdata.get("browser", "chrome").lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

        service = ChromeService(
            r"C:\Users\cks_1\OneDrive\Documents\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"
        )
        context.driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        service = FirefoxService(
            r"C:\Users\cks_1\OneDrive\Documents\Drivers\geckodriver-v0.36.0-win32\geckodriver.exe"
        )

        context.driver = webdriver.Firefox(service=service, options=options)


    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")

        service = EdgeService(
            r"C:\Users\cks_1\OneDrive\Documents\Drivers\edgedriver_win64 (1)\msedgedriver.exe"
        )
        context.driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    context.wait = WebDriverWait(context.driver, 15)


def after_scenario(context, scenario):
    print(f"ENDING SCENARIO: {scenario.name}")

    if scenario.status == "failed":
        context.driver.save_screenshot(
            f"reports/{scenario.name}.png"
        )

    if context.driver:
        context.driver.quit()
