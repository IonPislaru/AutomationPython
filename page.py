from locator import *
from element import BasePageElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color


class SearchUserElement(BasePageElement):
    locator = "user-name"


class SearchPassElement(BasePageElement):
    locator = "password"


class FirstName(BasePageElement):
    locator = "firstName"


class LastName(BasePageElement):
    locator = "lastName"


class ZipCode(BasePageElement):
    locator = "postalCode"

class BasePage(object):
        def __init__(self, driver):
            self.driver = driver


class MainPage(BasePage):

    search_user_element = SearchUserElement()
    search_pass_element = SearchPassElement()

    def is_title_matching(self):
        return "Swag Labs" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def click_error_button_log_in(self):
        element = self.driver.find_element(*MainPageLocators.ERROR_BUTTON)
        element.click()

    def border_color_user_name(self):
        element = self.driver.find_element(*MainPageLocators.USER_NAME)
        border_color = (element.value_of_css_property('border-bottom-color'))
        hex_border_color = Color.from_string(border_color).hex
        return hex_border_color

    def border_color_password(self):
        element = self.driver.find_element(*MainPageLocators.PASSWORD)
        border_color = (element.value_of_css_property('border-bottom-color'))
        hex_border_color = Color.from_string(border_color).hex
        return hex_border_color

    def error_message_container_log_in(self):
        element = self.driver.find_element(*MainPageLocators.ERROR_MESSAGE_CONTAINER)
        background_color = (element.value_of_css_property('background-color'))
        hex_background_color = Color.from_string(background_color).hex
        return hex_background_color

    def get_url(self):
        element = self.driver.current_url
        return element

    def press_twitter_logo(self):
        element = self.driver.find_element(*MainPageLocators.TWITTER)
        element.click()

    def press_facebook_logo(self):
        element = self.driver.find_element(*MainPageLocators.FACEBOOK)
        element.click()

    def press_linkedin_logo(self):
        element = self.driver.find_element(*MainPageLocators.LINKEDIN)
        element.click()

    def linkedin_title(self):
        return "LinkedIn" in self.driver.title

class ProductsPage(BasePage):

    search_first_name = FirstName()
    search_last_name = LastName()
    search_zip_code = ZipCode()

    def add_backpack(self):
        element = self.driver.find_element(*MainPageLocators.ADD_BACKPACK)
        element.click()

    def remove_backpack(self):
        element = self.driver.find_element(*MainPageLocators.REMOVE_BACKPACK)
        element.click()

    def add_bike_light(self):
        element = self.driver.find_element(*MainPageLocators.ADD_BIKE_LIGHT)
        element.click()

    def remove_bike_light(self):
        element = self.driver.find_element(*MainPageLocators.REMOVE_BIKE_LIGHT)
        element.click()

    def add_t_shirt(self):
        element = self.driver.find_element(*MainPageLocators.ADD_T_SHIRT)
        element.click()

    def remove_t_shirt(self):
        element = self.driver.find_element(*MainPageLocators.REMOVE_T_SHIRT)
        element.click()

    def add_fleece_jacket(self):
        element = self.driver.find_element(*MainPageLocators.ADD_FLEECE_JACKET)
        element.click()

    def remove_fleece_jacket(self):
        element = self.driver.find_element(*MainPageLocators.REMOVE_FLEECE_JACKET)
        element.click()

    def add_onesie(self):
        element = self.driver.find_element(*MainPageLocators.ADD_ONESIE)
        element.click()

    def remove_onesie(self):
        element = self.driver.find_element(*MainPageLocators.REMOVE_ONESIE)
        element.click()

    def add_red_t_shirt(self):
        element = self.driver.find_element(*MainPageLocators.ADD_RED_T_SHIRT)
        element.click()

    def remove_red_t_shirt(self):
        element = self.driver.find_element(*MainPageLocators.REMOVE_RED_T_SHIRT)
        element.click()

    def open_bike_light_text(self):
        element = self.driver.find_element(*MainPageLocators.BIKE_LIGHT_TEXT)
        element.click()

    def open_bike_light_image(self):
        element = self.driver.find_element(*MainPageLocators.BIKE_LIGHT_IMAGE)
        element.click()

    def open_backpack_text(self):
        element = self.driver.find_element(*MainPageLocators.BACKPACK_TEXT)
        element.click()

    def open_backpack_image(self):
        element = self.driver.find_element(*MainPageLocators.BACKPACK_IMAGE)
        element.click()

    def open_t_shirt_text(self):
        element = self.driver.find_element(*MainPageLocators.T_SHIRT_TEXT)
        element.click()

    def open_t_shirt_image(self):
        element = self.driver.find_element(*MainPageLocators.T_SHIRT_IMAGE)
        element.click()

    def open_onesie_text(self):
        element = self.driver.find_element(*MainPageLocators.ONESIE_TEXT)
        element.click()

    def open_onesie_image(self):
        element = self.driver.find_element(*MainPageLocators.ONESIE_IMAGE)
        element.click()

    def open_fleece_jacket_text(self):
        element = self.driver.find_element(*MainPageLocators.FLEECE_JACKET_TEXT)
        element.click()

    def open_fleece_jacket_image(self):
        element = self.driver.find_element(*MainPageLocators.FLEECE_JACKET_IMAGE)
        element.click()

    def open_red_t_shirt_text(self):
        element = self.driver.find_element(*MainPageLocators.RED_T_SHIRT_TEXT)
        element.click()

    def open_red_t_shirt_image(self):
        element = self.driver.find_element(*MainPageLocators.RED_T_SHIRT_IMAGE)
        element.click()

    def back_to_products(self):
        element = self.driver.find_element(*MainPageLocators.BACK_TO_PRODUCTS)
        element.click()

    def press_lines_menu(self):
        element = self.driver.find_element(*MainPageLocators.LINES_MENU)
        element.click()

    def press_logout(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((MainPageLocators.LOGOUT))
            )
        finally:
            element.click()

    def press_sort_button(self):
        element = self.driver.find_element(*MainPageLocators.SORT_BUTTON)
        element.click()

    def press_high_low(self):
        element = self.driver.find_element(*MainPageLocators.HIGH_LOW)
        element.click()

    def press_low_high(self):
        element = self.driver.find_element(*MainPageLocators.LOW_HIGH)
        element.click()

    def press_a_z(self):
        element = self.driver.find_element(*MainPageLocators.A_Z)
        element.click()

    def press_z_a(self):
        element = self.driver.find_element(*MainPageLocators.Z_A)
        element.click()

    def click_shopping_cart(self):
        element = self.driver.find_element(*MainPageLocators.SHOPPING_CART)
        element.click()

    def click_checkout(self):
        element = self.driver.find_element(*MainPageLocators.CHECKOUT)
        element.click()

    def click_continue(self):
        element = self.driver.find_element(*MainPageLocators.CONTINUE_CHECKOUT)
        element.click()

    def click_finish(self):
        element = self.driver.find_element(*MainPageLocators.FINISH_CHECKOUT)
        element.click()

    def click_cancel_checkout(self):
        element = self.driver.find_element(*MainPageLocators.CANCEL_CHECKOUT)
        element.click()

    def border_color_first_name(self):
        element = self.driver.find_element(*MainPageLocators.FIRST_NAME)
        border_color = (element.value_of_css_property('border-bottom-color'))
        hex_border_color = Color.from_string(border_color).hex
        return hex_border_color

    def border_color_last_name(self):
        element = self.driver.find_element(*MainPageLocators.LAST_NAME)
        border_color = (element.value_of_css_property('border-bottom-color'))
        hex_border_color = Color.from_string(border_color).hex
        return hex_border_color

    def border_color_postal_code(self):
        element = self.driver.find_element(*MainPageLocators.POSTAL_CODE)
        border_color = (element.value_of_css_property('border-bottom-color'))
        hex_border_color = Color.from_string(border_color).hex
        return hex_border_color

    def click_error_button_check_out(self):
        element = self.driver.find_element(*MainPageLocators.ERROR_BUTTON)
        element.click()

    def error_message_container_check_out(self):
        element = self.driver.find_element(*MainPageLocators.ERROR_MESSAGE_CONTAINER)
        background_color = (element.value_of_css_property('background-color'))
        hex_background_color = Color.from_string(background_color).hex
        return hex_background_color

    def click_back_home(self):
        element = self.driver.find_element(*MainPageLocators.BACK_HOME)
        element.click()

    def press_reset_app_state(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((MainPageLocators.RESET_APP_STATE))
            )
        finally:
            element.click()

    def press_close_lines_menu(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((MainPageLocators.CLOSE_LINES_MENU))
            )
        finally:
            element.click()

    def press_all_items(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((MainPageLocators.ALL_ITEMS))
            )
        finally:
            element.click()

    def open_fleece_jacket(self):
        element = self.driver.find_element(*MainPageLocators.FLEECE_JACKET_IMAGE)
        element.click()

    def press_about(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((MainPageLocators.ABOUT))
            )
        finally:
            element.click()

class is_element_present(BasePage):

    def shop_badge(self):
        return self.driver.find_element(*MainPageLocators.SHOP_BADGE) is not None

    def back_to(self):
        return self.driver.find_element(*MainPageLocators.BACK_TO_PRODUCTS) is not None

    def new_page(self):
        return self.driver.find_element(*MainPageLocators.LINES_MENU) is not None

    def products(self):
        return self.driver.find_element(*MainPageLocators.PRODUCTS) is not None

    def login_button(self):
        return self.driver.find_element(*MainPageLocators.LOGIN_BUTTON) is not None

    def continue_shopping(self):
        return self.driver.find_element(*MainPageLocators.CONTINUE_SHOPPING) is not None

    def checkout_complete_text(self):
        return self.driver.find_element(*MainPageLocators.CHECKOUT_COMPLETE) is not None

    def your_cart_text(self):
        return self.driver.find_element(*MainPageLocators.YOUR_CART) is not None

    def error_button(self):
        return self.driver.find_element(*MainPageLocators.ERROR_BUTTON) is not None

    def products_list(self):
        return self.driver.find_element(*MainPageLocators.PRODUCTS_LIST) is not None

    def is_shopping_cart_badge_present(self):
        element = self.driver.find_element(*MainPageLocators.SHOPPING_CART)

        if element.text == "":
            return False
        else:
            return True

    def is_side_menu_closed(self):
        element = self.driver.find_element(*MainPageLocators.SIDE_MENU)
        s = element.get_attribute("aria-hidden")
        return s

class is_sort_correct(BasePage):

    def product_price(self):
        x = self.driver.find_elements(*MainPageLocators.PRODUCT_PRICE)
        list1 = []
        for i in x:
            list1.append(float(i.text.strip("$")))
        return list1

    def product_name(self):
        x = self.driver.find_elements(*MainPageLocators.PRODUCT_NAME)
        list1 = []
        for i in x:
            list1.append(i.text)
        return list1

class error_message(BasePage):

    def error_message_log_in(self):
        msg = self.driver.find_elements(*MainPageLocators.ERROR_MESSAGE_LOG_IN)

        list1 = []
        for i in msg:
            list1.append(i.text)
        return list1

    def error_message_check_out(self):
        msg = self.driver.find_elements(*MainPageLocators.ERROR_MESSAGE_CHECK_OUT)

        list1 = []
        for i in msg:
            list1.append(i.text)
        return list1