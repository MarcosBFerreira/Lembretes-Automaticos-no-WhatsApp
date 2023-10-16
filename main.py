# Importando as Bibliotecas

#   Controlar o navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#   Encontrar objetos na página
from selenium.webdriver.common.by import By

#   Enviar comandos das teclas na página
from selenium.webdriver.common.keys import Keys

#   Temporizador
from time import sleep

# Obter informações do sistema
import os

# Obtendo a pasta atual que estamos
pasta_atual = os.getcwd()

# Informações de contato e a mensagem que vamos enviar
contato = 'Anotações'
mensagem = 'Tô testando uma parada para aula'

# Criando uma variável para controlar erros
ERROR = True

# Configurando o navegador da nossa automação
options = webdriver.ChromeOptions()

#   Sinalizando a pasta onde ficará nosso perfil do navegador para salvar as informações
options.add_argument(rf'--user-data-dir={pasta_atual}\configuration')

#   Sinalizando qual navegador iremos utilizar
navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Abrindo a página do Whatsapp
navegador.get("https://web.whatsapp.com")

# Controlando o erro de clicar num objeto que não existe
while ERROR:
    
    try:

        # Clicando na barra de pesquisa do Whatsapp
        navegador.find_element(By.XPATH,
                               '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/div[2]'
                               '/div/div[1]/p').click()
        ERROR = False
    
    except:

        pass

# Escrevendo o nome do contato na barra de pesquisa e dando ENTER para abrir a conversa
navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/div[1]/div/div[2]/div[2]/'
                               'div/div[1]/p').send_keys(f'{contato}', Keys.ENTER)

# Enviando infinitas mensagens para o contato
while True:

    navegador.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]'
                                             '/div/div[2]/div[1]').send_keys(f'{mensagem}', Keys.ENTER)
    print(f'Mensagem: {mensagem}\nEnviada para: {contato}')

    sleep(300)
