class checkoutPage:

    def __init__(self,driver):
        self.driver=driver

    checkout_btn="//*[text()='Proceed to checkout']"
    proceed_checkout="(//*[text()='Proceed to checkout'])[1]"
    sign_in="//*[normalize-space(text())='Sign in']"
    email="//*[@class='form-fields']//*[@type='email']"
    passwd="//*[@class='form-fields']//*[@type='password']"
    continue_btn="//*[@class='c-form__footer u-flex-column']//button[@name='continue']"
    address_btn="//*[@name='confirm-addresses']"
    delivery_btn="//*[@name='confirmDeliveryOption']"


