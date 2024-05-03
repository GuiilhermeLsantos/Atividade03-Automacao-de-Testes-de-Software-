from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_consulta_cep(driver):
    driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

    cep_input = driver.find_element(By.NAME, "endereco")
    cep_input.send_keys("02323410")

    buscar_button = driver.find_element(By.XPATH, "//button[text()='Buscar']")
    buscar_button.click()

    time.sleep(3)

    table = driver.find_element(By.ID, "resultado-DNEC")

    endereco = table.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
    bairro = table.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text
    cidade_uf = table.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text

    assert endereco == "Alameda das Roseiras"
    assert bairro == "Jardim Joana D'Arc"
    assert cidade_uf == "São Paulo/SP"