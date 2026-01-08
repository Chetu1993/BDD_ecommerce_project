from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import productPage
class homePage:

    def __init__(self, driver):
        self.driver=driver

    click_men_coats_icon="(//li[@class='htmlcontent-item-2 col-xs-4'])[2]"
    all_store_exp_btn="//div[@class='btns']//a[@class='cta']"
    dealy_btn="(//*[@class='col-md-6'])[4]"

    def click_men_coats(self):
        return self.driver.find_element(By.XPATH,self.click_men_coats_icon)

    def all_store_btn(self):
        element = self.driver.find_element(By.XPATH, self.all_store_exp_btn)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
        return element

    def click_dealy_btn(self):
        self.driver.find_element(By.XPATH,self.dealy_btn).click()

        return productPage(self.driver)





