from selenium import webdriver
from selenium.webdriver.common.by import By

class TestConstructor:

    # булочки
    def test_rolls(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Соусы" в конструкторе
            sauces_button = driver_entrance.find_element(By.XPATH, "//span[text()='Соусы']")
            sauces_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(1)

            rolls_button = driver_entrance.find_element(By.XPATH, "//span[text()='Булки']")
            rolls_button.click()

            try:
                driver_entrance.find_element(By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
            except:
                raise Exception("Переход на раздел булок в конструкторе не работает")
            print("Переход на раздел булок в конструкторе работает")
        finally:
            driver_entrance.quit()

    # соусы
    def test_sauces(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Соусы" в конструкторе
            sauces_button = driver_entrance.find_element(By.XPATH, "//span[text()='Соусы']")
            sauces_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(1)

            try:
                driver_entrance.find_element(By.XPATH, "//p[text()='Соус с шипами Антарианского плоскоходца']")
            except:
                raise Exception("Переход на раздел соусов в конструкторе не работает")
            print("Переход на раздел соусов в конструкторе работает")
        finally:
            driver_entrance.quit()

    # начинки
    def test_fillings(self, entrance_input_value, entrance_input_path, main_menu, driver_entrance):
        try:
            # Нажмите кнопку "Начинки" в конструкторе
            fillings_button = driver_entrance.find_element(By.XPATH, "//span[text()='Начинки']")
            fillings_button.click()

            # Небольшая задержка для ожидания результата
            driver_entrance.implicitly_wait(1)

            try:
                driver_entrance.find_element(By.XPATH, "//p[text()='Биокотлета из марсианской Магнолии']")
            except:
                raise Exception("Переход на раздел начинок в конструкторе не работает")
            print("Переход на раздел начинок в конструкторе работает")
        finally:
            driver_entrance.quit()