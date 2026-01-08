from behave import *
# from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.logger import get_logger
# from selenium.webdriver.chrome.service import Service
import time
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.homePage import homePage
from pages.productPage import productPage
from pages.checkoutPage import checkoutPage
# service=Service(r"C:\Users\cks_1\OneDrive\Documents\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
logger=get_logger(__name__)
@given(u'launch the Ecommerce application')
def step_impl(context):
    logger.info("user logged in")
    # context.driver = webdriver.Chrome(service=service)
    context.driver.get("http://www.automationpractice.pl/index.php")
    context.driver.maximize_window()
    time.sleep(5)
    # context.wait = WebDriverWait(context.driver, 10)
    context.a=homePage(context.driver)
    context.a.click_men_coats().click()


    # context.wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@class='htmlcontent-item-2 col-xs-4'])[2]"))).click()


@when(u'select the specific item and add product to cart')
def step_impl(context):
    logger.info("user in cart page")
    context.wait.until(
        EC.element_to_be_clickable((By.XPATH, context.a.all_store_exp_btn))
    )
    time.sleep(4)
    context.a.all_store_btn().click()

    dealy_btn=context.wait.until(EC.element_to_be_clickable((By.XPATH, context.a.dealy_btn)))
    dealy_btn.click()

    parent_window = context.driver.current_window_handle
    windows = context.driver.window_handles
    for window in windows:
        if window != parent_window:
            context.driver.switch_to.window(window)
            break
    print("child window title:", context.driver.title)
    context.productPage=productPage(context.driver)
    context.wait.until(EC.element_to_be_clickable((By.XPATH,context.productPage.product_name))).click()
    # context.wait.until(
        # EC.element_to_be_clickable((By.XPATH, "//*[text()='Batterie Externe MagSafe Ultra-Fine 10000mAh']"))).click()

    context.wait.until(EC.element_to_be_clickable((By.XPATH, context.productPage.cart_btn))).click()

@when(u'go to checkout page')
def step_impl(context):
    logger.info("user in checkout page")
    context.checkoutPage=checkoutPage(context.driver)
    context.wait.until(EC.element_to_be_clickable((By.XPATH, context.checkoutPage.checkout_btn))).click()

    context.wait.until(EC.element_to_be_clickable((By.XPATH, context.checkoutPage.proceed_checkout))).click()

@when(u'signin to place an order')
def step_impl(context):
    logger.info("user in payment page")
    context.wait.until(EC.element_to_be_clickable((By.XPATH, context.checkoutPage.sign_in))).click()

    context.wait.until(EC.visibility_of_element_located((By.XPATH, context.checkoutPage.email))).send_keys(
        "schetankumar123@gmail.com")
    context.wait.until(
        EC.visibility_of_element_located((By.XPATH, context.checkoutPage.passwd))).send_keys(
        "test@123")

    context.driver.find_element(By.XPATH,context.checkoutPage.continue_btn).click()
    context.wait.until(EC.element_to_be_clickable((By.XPATH, context.checkoutPage.address_btn))).click()
    context.wait.until(EC.element_to_be_clickable((By.XPATH, context.checkoutPage.delivery_btn))).click()

    time.sleep(4)
    context.driver.close()