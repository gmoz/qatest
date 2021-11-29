import os
import time
import random

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml


@allure.epic('ACY Register Testing')
@allure.feature('TCS01-S07')
class TestACY:
    param = None

    def init_param(self):
        with open('params_tcs.yaml', 'r') as f:
            self.param = yaml.load(f, Loader=yaml.FullLoader)

    def get_otp_code(self, phone):
        # suppose there is an API can get the correct otp code
        return "1234"

    def get_random_email(self):
        base = ['i', 'a', 'm', 'h', 'a', 'n', 'd', 's', 'o', 'm', 'e']
        mail = []
        for i in range(0, 5):
            n = random.randint(1, 10)
            mail.append(base[n])

        mail.append(str(time.time_ns())[-6:-1])
        mail.append("@test.com")
        return "".join(mail)

    @allure.title('TCS01')
    @allure.description('Step 01-You are just 6 easy steps away from placing your first trade with us.')
    def TCS01(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1280, 1080)

        # bypass the i18n
        driver.get(self.param['TargetUrl'])
        i18n_btn = driver.find_element(By.CSS_SELECTOR, "[class='redirect-modal-bottom']") \
            .find_element(By.CSS_SELECTOR, '[class="button"]')
        if i18n_btn:
            i18n_btn.click()
        driver.get(self.param['TargetUrl'])

        account_type_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=entity]")
        country_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=country]")
        title_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=title]")
        first_name_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=firstname]")
        last_name_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=lastname]")
        email_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=email]")
        phone_area_field = driver.find_element(By.CSS_SELECTOR,
                                               "[class='MuiBox-root jss124 jss32 jss122']").find_element(
            By.CSS_SELECTOR, "[class='jss31']")
        phone = driver.find_element(By.CSS_SELECTOR, "[data-testid=phone]")
        code = driver.find_element(By.CSS_SELECTOR, "[data-testid=code]")
        get_code_btn = driver.find_element(By.CSS_SELECTOR, "[class='jss136 jss137']")

        next_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid=submit]")

        with allure.step("Test Case S01-01"):
            pass
        assert next_btn.get_attribute("disabled") is not None

        driver.execute_script("document.querySelector('[data-testid=entity0]').click();")
        driver.execute_script("document.querySelector('[data-testid=country7]').click();")
        driver.execute_script("document.querySelector('[data-testid=title0]').click();")

        first_name_field.send_keys(self.param['FormValue_S01']['FirstName'])
        last_name_field.send_keys(self.param['FormValue_S01']['LastName'])
        email_field.send_keys(self.get_random_email())

        driver.execute_script("document.querySelector('[data-testid=undefined0]').click();")
        phone.send_keys(self.param['FormValue_S01']['Phone'])
        code.send_keys(self.get_otp_code(self.param['FormValue_S01']['Phone']))
        time.sleep(1)

        with allure.step("Test Case S01-06 PASSED"):
            pass
        assert next_btn.get_attribute("disabled") is None

        # next_btn.click()
        driver.execute_script("$(arguments[0]).click()", next_btn)
        time.sleep(5)
        # Test Case S01-07 TBD
        self.TCS02(driver)

    @allure.title('TCS02')
    @allure.description('Step 02 - Tell us more about yourself.')
    def TCS02(self, driver):
        id_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=idNo]")
        address_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=street]")
        city_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=city]")
        state_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=state]")
        zipcode_field = driver.find_element(By.CSS_SELECTOR, "[data-testid=zip]")
        next_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid=submit2]")

        with allure.step("Test Case S02-01"):
            pass
        assert next_btn.get_attribute("disabled") is not None

        driver.execute_script("document.querySelector('[data-testid=gender0]').click();")
        driver.execute_script("document.querySelector('[data-testid=birthday5]').click();")
        driver.execute_script("document.querySelector('[data-testid=birthmonth5]').click();")
        driver.execute_script("document.querySelector('[data-testid=birthyear27]').click();")

        id_field.send_keys(self.param['FormValue_S02']['PhotoIDNumber'])
        address_field.send_keys(self.param['FormValue_S02']['ResidentialAddress'])
        city_field.send_keys(self.param['FormValue_S02']['City'])
        state_field.send_keys(self.param['FormValue_S02']['State'])
        zipcode_field.send_keys(self.param['FormValue_S02']['ZipCode'])

        time.sleep(1)
        with allure.step("Test Case S02-03"):
            pass
        assert next_btn.get_attribute("disabled") is None

        # next_btn.click()
        driver.execute_script("$(arguments[0]).click()", next_btn)
        # Test Case S02-04 TBD
        time.sleep(5)

        self.TCS03(driver)

    @allure.title('TCS03')
    @allure.description('Step 03 - Tell us your trading preferences.')
    def TCS03(self, driver):
        next_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid=submitTradingPreferences]")
        with allure.step("Test Case S03-01"):
            pass
        assert next_btn.get_attribute("disabled") is not None

        driver.execute_script("document.querySelector('[data-testid=employment0]').click();")
        driver.execute_script("document.querySelector('[data-testid=occupation0]').click();")
        driver.execute_script("document.querySelector('[data-testid=industry3]').click();")
        driver.execute_script("document.querySelector('[data-testid=annualIncome1]').click();")
        driver.execute_script("document.querySelector('[data-testid=totalInvestmentsSavings1]').click();")
        driver.execute_script("document.querySelector('[data-testid=platform0]').click();")
        driver.execute_script("document.querySelector('[data-testid=fundingCurrency0]').click();")
        driver.execute_script("document.querySelector('[data-testid=accountType0]').click();")
        driver.execute_script("document.querySelector('[data-testid=leverage2]').click();")

        time.sleep(1)
        with allure.step("Test Case S03-04"):
            pass
        assert next_btn.get_attribute("disabled") is None

        # next_btn.click()
        driver.execute_script("$(arguments[0]).click()", next_btn)
        # Test Case S03-05 TBD
        time.sleep(5)

        self.TCS04(driver)

    @allure.title('TCS04')
    @allure.description('Step 04 - (1/2)We have created some practice questions for you')
    def TCS04(self, driver):
        next_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid=goNext]")
        with allure.step("Test Case S04-01"):
            pass
        assert next_btn.get_attribute("disabled") is not None

        # radio
        # can not test, TBD
        radios = driver.find_elements(By.CSS_SELECTOR, "[type=radio]")
        radios[0].click()
        radios[4].click()
        radios[8].click()
        radios[11].click()
        radios[15].click()
        radios[16].click()

        time.sleep(1)
        with allure.step("Test Case S04-03"):
            pass
        assert next_btn.get_attribute("disabled") is None

        time.sleep(1)
        # next_btn.click()
        driver.execute_script("$(arguments[0]).click()", next_btn)
        # Test Case S04-04 TBD
        time.sleep(3)
        self.TCS04_2(driver)

    @allure.title('TCS04_2')
    @allure.description('Step 04 - (2/2)We have created some practice questions for you')
    def TCS04_2(self, driver):
        next_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid=submitExperiences]")
        with allure.step("Test Case S04_2-01"):
            pass
        assert next_btn.get_attribute("disabled") is not None

        # radio
        # can not test, TBD
        radios = driver.find_elements(By.CSS_SELECTOR, "[type=radio]")
        radios[18].click()
        radios[23].click()
        radios[26].click()
        radios[29].click()
        radios[34].click()

        with allure.step("Test Case S04_2-02"):
            pass
        assert next_btn.get_attribute("disabled") is None

        time.sleep(1)
        # next_btn.click()
        driver.execute_script("$(arguments[0]).click()", next_btn)

        # Test Case S05-03 TBD
        time.sleep(3)
        self.TCS05(driver)

    @allure.title('TCS05')
    @allure.description('Step 05 - Please confirm you have read our Terms')
    def TCS05(self, driver):
        next_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid=submitTerms]")
        with allure.step("Test Case S05-01"):
            pass
        assert next_btn.get_attribute("disabled") is not None

        # radio
        # can not test, TBD
        radios = driver.find_elements(By.CSS_SELECTOR, "[type=checkbox]")
        for r in radios:
            r.click()

        time.sleep(1)
        with allure.step("Test Case S05-02"):
            pass
        assert next_btn.get_attribute("disabled") is None

        # next_btn.click()
        driver.execute_script("$(arguments[0]).click()", next_btn)
        # Test Case S05-03 TBD
        time.sleep(5)
        self.TCS06(driver)

    @allure.title('TCS06')
    @allure.description('Step 06 - Confirm your ID')
    def TCS06(self, driver):
        next_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid=submitconfirmIdPersonal]")
        with allure.step("Test Case S06-01"):
            pass
        assert next_btn.get_attribute("disabled") is not None

        upload_id_front = driver.find_element(By.CSS_SELECTOR, "[data-testid=pid]")
        upload_id_back = driver.find_element(By.CSS_SELECTOR, "[data-testid=poa]")
        upload_id_address = driver.find_element(By.CSS_SELECTOR, "[data-testid=extend1]")
        upload_id_others = driver.find_element(By.CSS_SELECTOR, "[data-testid=extend2]")

        file_path = os.getcwd() + "\\test.png"
        upload_id_front.send_keys(file_path)
        time.sleep(1)
        upload_id_back.send_keys(file_path)
        time.sleep(1)
        upload_id_address.send_keys(file_path)
        time.sleep(1)
        upload_id_others.send_keys(file_path)

        time.sleep(1)
        with allure.step("Test Case S06-02"):
            pass
        assert next_btn.get_attribute("disabled") is None

        try:
            driver.execute_script("document.querySelectorAll('[data-garden-id=\"buttons.icon_button\"]')[1].click();")
        except Exception as ex:
            print("chat room no show")

        time.sleep(1)
        next_btn.click()
        # self.TCS07(driver)

    @allure.title('TCS07')
    @allure.description('Thank you')
    def TCS07(self, driver):

        time.sleep(10)
        tku = driver.find_elements(By.ID, "thankYouCard")

        with allure.step("Test Case S07-01"):
            pass
        assert tku is not None


def test_main():
    test = TestACY()
    test.init_param()
    test.TCS01()
