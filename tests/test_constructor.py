import logging
from selenium.webdriver.common.by import By


class TestConstructor:

    # булочки
    def test_rolls(self, driver, locators_data):
        # Нажмите кнопку "Соусы" в конструкторе
        sauces_button = driver.find_element(By.XPATH, locators_data.constructor_path().get('sauces'))
        sauces_button.click()

        rolls_button = driver.find_element(By.XPATH, locators_data.constructor_path().get('rolls'))
        rolls_button.click()

        try:
            driver.find_element(By.XPATH, locators_data.constructor_path().get('rolls_selected'))
        except:
            raise Exception("Переход на раздел булок в конструкторе не работает")
        logging.info("Переход на раздел булок в конструкторе работает")

        driver.quit()

    # соусы
    def test_sauces(self, driver, locators_data):
        # Нажмите кнопку "Соусы" в конструкторе
        sauces_button = driver.find_element(By.XPATH, locators_data.constructor_path().get('sauces'))
        sauces_button.click()

        try:
            driver.find_element(By.XPATH, locators_data.constructor_path().get('sauces_selected'))
        except:
            raise Exception("Переход на раздел соусов в конструкторе не работает")
        logging.info("Переход на раздел соусов в конструкторе работает")

        driver.quit()

    # начинки
    def test_fillings(self, driver, locators_data):
        # Нажмите кнопку "Начинки" в конструкторе
        fillings_button = driver.find_element(By.XPATH, locators_data.constructor_path().get('fillings'))
        fillings_button.click()

        try:
            driver.find_element(By.XPATH, locators_data.constructor_path().get('fillings_selected'))
        except:
            raise Exception("Переход на раздел начинок в конструкторе не работает")
        logging.info("Переход на раздел начинок в конструкторе работает")

        driver.quit()
