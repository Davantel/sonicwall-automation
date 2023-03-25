from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from datetime import date, timedelta
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def abre_navegador(url):
    servico = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument('ignore-certificate-errors')
    #options.add_argument("--start-maximized")
    navegador = webdriver.Chrome(service=servico, chrome_options=options)
    navegador.get(url)
    navegador.implicitly_wait(10)

    return navegador

######Parametros inciais#######
navegador = abre_navegador('https://179.190.54.69:1312/sgms/auth')
data = date.today()
yesterday = data - timedelta(1)

######logar#######
navegador.find_element('xpath', '//*[@id="sw-email-input__input"]').send_keys("admin")
navegador.find_element('xpath', '/html/body/form/div/div[1]/div[1]/div[2]/div[2]/div[4]/button').click()
navegador.find_element('xpath', '/html/body/form/div/div[1]/div[1]/div[2]/div[2]/div[5]/div[2]/input').send_keys("V3us5lr4dX!@#")
navegador.find_element('xpath', '/html/body/form/div/div[1]/div[2]').click()
    
######Extrair pdf######
navegador.switch_to.default_content() 
navegador.switch_to.frame("contents")
navegador.switch_to.frame("imiddle")
WebDriverWait(navegador, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="38545"]')))
navegador.find_element(By.XPATH, '//*[@id="38545"]').click()
navegador.find_element(By.XPATH,'//*[@id="38545"]/li[6]').click()

######Seleciona Calendario######
navegador.switch_to.default_content() 
navegador.switch_to.frame("contents")
navegador.switch_to.frame("icontents")
navegador.switch_to.frame("icontent")
navegador.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/label').click()
navegador.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/input').click()
navegador.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div[1]/label[1]/span[1]').click()
navegador.find_element(By.CSS_SELECTOR, f"span[data-date='{yesterday}']").click()
navegador.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/span[7]/span/span/span').click()

for i in range(1,18):
    navegador.switch_to.default_content() 
    navegador.switch_to.frame("contents")
    navegador.switch_to.frame("itreecontrol")
    navegador.find_element(By.CSS_SELECTOR, f"table[data-recordindex='{i}']").click()
    navegador.switch_to.default_content() 
    navegador.switch_to.frame("contents")
    navegador.switch_to.frame("icontents")
    navegador.switch_to.frame("icontent")
    try:
        navegador.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/div/table/tbody/tr/td[1]/div/div/div')
        navegador.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/span[8]/span/span/span').click()
        navegador.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div/div/div[1]').click()
        sleep(5)
        navegador.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[2]/button').click()
        sleep(20)
    except:
        navegador.switch_to.default_content() 
        navegador.switch_to.frame("contents")
        navegador.switch_to.frame("icontents")
        navegador.switch_to.frame("icaption")
        element = navegador.find_element(By.CLASS_NAME,'breadcrumbPageTitle') 
        print(f"=================\nNão teve virus em {element.text}")


 


