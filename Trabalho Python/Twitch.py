from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver (Substitua 'your_path' pelo caminho do seu WebDriver)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Função para salvar dados em um arquivo
def salvar_dados(dados, nome_arquivo='dados.txt'):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(dados)


# URL do site Twitch
url = 'https://www.twitch.tv/'

try:
    # Iniciar o navegador e acessar a Twitch
    driver.get(url)
    time.sleep(5)  # Espera para a página carregar completamente

    # Encontrar a barra de pesquisa e digitar 'Baiano'
    search_bar = driver.find_element(By.XPATH,'//input[@type="search"]')
    search_bar.send_keys('Baiano')
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)  # Espera para os resultados da pesquisa carregarem

    # Clicar no canal do Baiano nos resultados da pesquisa
    baiano_channel = driver.find_element(By.XPATH,'//a[@href="/baiano"]')
    baiano_channel.click()
    time.sleep(5)  # Espera para o canal carregar

    # Localizar a seção 'Sobre' do canal
    sobre_baiano = driver.find_element(By.XPATH,'//*[@id="live-channel-about-panel"]/div/div[2]/div/div[1]/div[2]/div')
    texto_sobre_baiano = sobre_baiano.text

    # Salvar o texto da seção 'Sobre'
    salvar_dados(texto_sobre_baiano, 'sobre_baiano.txt')


    # Fechar o navegador após a execução do teste
    driver.quit()

except Exception as e:
    print("Aconteceu um erro: ",e)
finally:
    driver.quit
