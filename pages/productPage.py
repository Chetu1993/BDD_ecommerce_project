from selenium.webdriver.common.by import By
from pages.checkoutPage import checkoutPage

class productPage:

    def __init__(self,driver):
        self.driver=driver

    product_name="//*[text()='Batterie Externe MagSafe Ultra-Fine 10000mAh']"

    cart_btn="//*[normalize-space(text())='Add to cart']"

    def click_product(self):
        self.driver.find_element(By.XPATH,self.product_name).click()

    def cart_click(self):
        self.driver.find_element(By.XPATH,self.cart_btn).click()

        return checkoutPage(self.driver)




