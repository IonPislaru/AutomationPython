import os
import unittest
from selenium import webdriver
import page
import HtmlTestRunner

os.environ['PATH'] += r"D:/SeleniumDrivers"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class Testing(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.saucedemo.com/")

    def test_log_in(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matching()
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        new_page = page.is_element_present(self.driver)
        assert new_page.new_page()

    def test_add_backpack(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_backpack()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is True

    def test_remove_backpack(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_backpack()
        productPage.remove_backpack()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is False

    def test_add_bike_light(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_bike_light()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is True

    def test_remove_bike_light(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_bike_light()
        productPage.remove_bike_light()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is False

    def test_add_t_shirt(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is True

    def test_remove_t_shirt(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.remove_t_shirt()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is False

    def test_add_fleece_jacket(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_fleece_jacket()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is True

    def test_remove_fleece_jacket(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_fleece_jacket()
        productPage.remove_fleece_jacket()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is False

    def test_add_onesie(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_onesie()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is True

    def test_remove_onesie(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_onesie()
        productPage.remove_onesie()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is False

    def test_add_red_t_shirt(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_red_t_shirt()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is True

    def test_remove_red_t_shirt(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_red_t_shirt()
        productPage.remove_red_t_shirt()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.is_shopping_cart_badge_present() is False

    def test_open_bike_light_text(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_bike_light_text()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_open_bike_light_image(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_bike_light_image()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_open_backpack_text(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_backpack_text()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_open_backpack_image(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_backpack_image()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_open_t_shirt_text(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_t_shirt_text()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_open_t_shirt_image(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_t_shirt_image()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_open_onesie_text(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_onesie_text()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_open_onesie_image(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_onesie_image()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_fleece_jacket_text(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_fleece_jacket_text()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_fleece_jacket_image(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_fleece_jacket_image()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_red_t_shirt_text(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_red_t_shirt_text()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_red_t_shirt_image(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_red_t_shirt_image()
        back_to = page.is_element_present(self.driver)
        assert back_to.back_to()

    def test_back_to_products(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_bike_light_image()
        productPage.back_to_products()
        products = page.is_element_present(self.driver)
        assert products.products()

    def test_logout(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.press_lines_menu()
        productPage.press_logout()
        login_button = page.is_element_present(self.driver)
        assert login_button.login_button()

    def test_shop_badge_present_after_relog(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_backpack()
        productPage = page.ProductsPage(self.driver)
        productPage.press_lines_menu()
        productPage.press_logout()
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        shop_badge = page.is_element_present(self.driver)
        assert shop_badge.shop_badge()

    def test_arrange_items_low_high(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.press_sort_button()
        productPage.press_low_high()
        verify = page.is_sort_correct(self.driver)
        assert verify.product_price() == sorted(verify.product_price())

    def test_arrange_items_high_low(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.press_sort_button()
        productPage.press_high_low()
        verify = page.is_sort_correct(self.driver)
        assert verify.product_price() == sorted(verify.product_price(), reverse = True)

    def test_arrange_items_a_z(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.press_sort_button()
        productPage.press_a_z()
        verify = page.is_sort_correct(self.driver)
        assert verify.product_name() == sorted(verify.product_name())

    def test_arrange_items_z_a(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.press_sort_button()
        productPage.press_z_a()
        verify = page.is_sort_correct(self.driver)
        assert verify.product_name() == sorted(verify.product_name(), reverse = True)

    def test_open_shopping_cart(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        check = page.is_element_present(self.driver)
        assert check.continue_shopping()

    def test_cancel_checkout_at_your_information(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.click_cancel_checkout()
        check = page.is_element_present(self.driver)
        assert check.your_cart_text()

    def test_cancel_checkout_at_overview(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_first_name = "Ion"
        productPage.search_last_name = "Pislaru"
        productPage.search_zip_code = "MD-6801"
        productPage.click_continue()
        productPage.click_cancel_checkout()
        check = page.is_element_present(self.driver)
        assert check.products_list()

    def test_check_out(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_first_name = "Ion"
        productPage.search_last_name = "Pislaru"
        productPage.search_zip_code = "MD-6801"
        productPage.click_continue()
        productPage.click_finish()
        verify = page.is_element_present(self.driver)
        assert verify.checkout_complete_text()

    def test_back_home_after_check_out(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_first_name = "Ion"
        productPage.search_last_name = "Pislaru"
        productPage.search_zip_code = "MD-6801"
        productPage.click_continue()
        productPage.click_finish()
        productPage.click_back_home()
        check = page.is_element_present(self.driver)
        assert check.products_list()

    def test_fail_log_in(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_login_button()
        check = page.error_message(self.driver)
        assert mainPage.border_color_user_name() == "#e2231a"
        assert mainPage.border_color_password() == "#e2231a"
        assert mainPage.error_message_container_log_in() == "#e2231a"
        assert 'Epic sadface: Username is required' in check.error_message_log_in()

    def test_resset_error_log_in(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_login_button()
        mainPage.click_error_button_log_in()
        assert mainPage.border_color_user_name() == "#ededed"
        assert mainPage.border_color_password() == "#ededed"
        assert mainPage.error_message_container_log_in() == "#ffffff"

    def test_log_in_only_user_name(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.click_login_button()
        check = page.error_message(self.driver)
        assert mainPage.border_color_user_name() == "#e2231a"
        assert mainPage.border_color_password() == "#e2231a"
        assert mainPage.error_message_container_log_in() == "#e2231a"
        assert 'Epic sadface: Password is required' in check.error_message_log_in()

    def test_log_in_only_password(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        check = page.error_message(self.driver)
        assert mainPage.border_color_user_name() == "#e2231a"
        assert mainPage.border_color_password() == "#e2231a"
        assert mainPage.error_message_container_log_in() == "#e2231a"
        assert 'Epic sadface: Username is required' in check.error_message_log_in()

    def test_check_out_fail(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.click_continue()
        check = page.error_message(self.driver)
        assert productPage.border_color_first_name() == "#e2231a"
        assert productPage.border_color_last_name() == "#e2231a"
        assert productPage.border_color_postal_code() == "#e2231a"
        assert productPage.error_message_container_check_out() == "#e2231a"
        assert 'Error: First Name is required' in check.error_message_check_out()

    def test_reset_error_check_out(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.click_continue()
        productPage.click_error_button_check_out()
        assert productPage.border_color_first_name() == "#ededed"
        assert productPage.border_color_last_name() == "#ededed"
        assert productPage.border_color_postal_code() == "#ededed"
        assert productPage.error_message_container_check_out() == "#ffffff"

    def test_check_out_only_firstname(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_first_name = "Ion"
        productPage.click_continue()
        check = page.error_message(self.driver)
        assert productPage.border_color_first_name() == "#e2231a"
        assert productPage.border_color_last_name() == "#e2231a"
        assert productPage.border_color_postal_code() == "#e2231a"
        assert productPage.error_message_container_check_out() == "#e2231a"
        assert 'Error: Last Name is required' in check.error_message_check_out()

    def test_check_out_first_and_last_name(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_first_name = "Ion"
        productPage.search_last_name = "Pislaru"
        productPage.click_continue()
        check = page.error_message(self.driver)
        assert productPage.border_color_first_name() == "#e2231a"
        assert productPage.border_color_last_name() == "#e2231a"
        assert productPage.border_color_postal_code() == "#e2231a"
        assert productPage.error_message_container_check_out() == "#e2231a"
        assert 'Error: Postal Code is required' in check.error_message_check_out()

    def test_check_out_firstname_and_postalcode(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_first_name = "Ion"
        productPage.search_zip_code = "MD-6801"
        productPage.click_continue()
        check = page.error_message(self.driver)
        assert productPage.border_color_first_name() == "#e2231a"
        assert productPage.border_color_last_name() == "#e2231a"
        assert productPage.border_color_postal_code() == "#e2231a"
        assert productPage.error_message_container_check_out() == "#e2231a"
        assert 'Error: Last Name is required' in check.error_message_check_out()

    def test_check_out_only_lastname(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_last_name = "Pislaru"
        productPage.click_continue()
        check = page.error_message(self.driver)
        assert productPage.border_color_first_name() == "#e2231a"
        assert productPage.border_color_last_name() == "#e2231a"
        assert productPage.border_color_postal_code() == "#e2231a"
        assert productPage.error_message_container_check_out() == "#e2231a"
        assert 'Error: First Name is required' in check.error_message_check_out()

    def test_check_out_lastname_and_postalcode(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_last_name = "Pislaru"
        productPage.search_zip_code = "MD-6801"
        productPage.click_continue()
        check = page.error_message(self.driver)
        assert productPage.border_color_first_name() == "#e2231a"
        assert productPage.border_color_last_name() == "#e2231a"
        assert productPage.border_color_postal_code() == "#e2231a"
        assert productPage.error_message_container_check_out() == "#e2231a"
        assert 'Error: First Name is required' in check.error_message_check_out()

    def test_check_out_only_postal_code(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_t_shirt()
        productPage.click_shopping_cart()
        productPage.click_checkout()
        productPage.search_zip_code = "MD-6801"
        productPage.click_continue()
        check = page.error_message(self.driver)
        assert productPage.border_color_first_name() == "#e2231a"
        assert productPage.border_color_last_name() == "#e2231a"
        assert productPage.border_color_postal_code() == "#e2231a"
        assert productPage.error_message_container_check_out() == "#e2231a"
        assert 'Error: First Name is required' in check.error_message_check_out()

    def test_reset_app_state(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.add_onesie()
        productPage.press_lines_menu()
        productPage.press_reset_app_state()
        check = page.is_element_present(self.driver)
        assert check.is_shopping_cart_badge_present() is False

    def test_close_side_menu(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.press_lines_menu()
        productPage.press_close_lines_menu()
        check = page.is_element_present(self.driver)
        assert check.is_side_menu_closed() == "true"

    def test_all_items(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.open_fleece_jacket()
        productPage.press_lines_menu()
        productPage.press_all_items()
        check = page.is_element_present(self.driver)
        assert check.products_list()

    def test_about_redirect(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        productPage = page.ProductsPage(self.driver)
        productPage.press_lines_menu()
        productPage.press_about()
        assert mainPage.get_url() == "https://saucelabs.com/"

    def test_twitter_link(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        mainPage.press_twitter_logo()
        # obtain window handle of browser in focus
        p = self.driver.current_window_handle
        # obtain parent window handle
        parent = self.driver.window_handles[0]
        # obtain browser tab window
        chld = self.driver.window_handles[1]
        # switch to browser tab
        self.driver.switch_to.window(chld)
        assert mainPage.get_url() == "https://twitter.com/saucelabs"

    def test_facebook_link(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        mainPage.press_facebook_logo()
        # obtain window handle of browser in focus
        p = self.driver.current_window_handle
        # obtain parent window handle
        parent = self.driver.window_handles[0]
        # obtain browser tab window
        chld = self.driver.window_handles[1]
        # switch to browser tab
        self.driver.switch_to.window(chld)
        assert mainPage.get_url() == "https://www.facebook.com/saucelabs"

    def test_linkedin_link(self):
        mainPage = page.MainPage(self.driver)
        mainPage.search_user_element = "standard_user"
        mainPage.search_pass_element = "secret_sauce"
        mainPage.click_login_button()
        mainPage.press_linkedin_logo()
        # obtain window handle of browser in focus
        p = self.driver.current_window_handle
        # obtain parent window handle
        parent = self.driver.window_handles[0]
        # obtain browser tab window
        chld = self.driver.window_handles[1]
        # switch to browser tab
        self.driver.switch_to.window(chld)
        assert mainPage.linkedin_title()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/try_swag_labs/reports'))
