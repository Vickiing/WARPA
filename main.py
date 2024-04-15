from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import sys

url_wa = r'https://web.whatsapp.com/'
arquivo = 'numeros.txt'
base_path = r'C:\Users\victo\Documents\python projetos\WARPA\images'

image_names = os.listdir('images/')
lista_de_imagems = [os.path.join(base_path, name) for name in image_names]
print(f'Arquivos prontos para envio:{lista_de_imagems}')


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get(url_wa)

sleep(20)

Iniciar = input('Faça o login como o código QRCODE e Pressione ENTER para iniciar o script.')

sleep(5)


info = input('Deseja anexar mais de uma imagem? S/N: ').upper()

if info == "N":
    image_path = input('Informe o caminho da  imagen: ')
    caminho_formatado = r'' + image_path

sleep(5)

#envio de imagems + texto para cada numero
with open("numeros.txt", "r") as file:

    for numero in file:

        url_wa_number = f'https://web.whatsapp.com/send?phone={numero}'

        print('Iniciando processo de envio  para ' + numero)
        driver.get(url_wa_number)

        element_found = False
        while not element_found:
            try:
                element = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div/div[2]/div[3]')

                if element:
                    element_found = True
                    print("Conversa encontrada.")

            except Exception as e:
                print("Coonversa não encontrada, tentando novamente em 5 segundos...")
                sleep(5)

        sleep(5)

        text_img = 'Teste de envio de imagem automático'

        botao_anexar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
        sleep(3)

        if info == "S":

            primeira_imagem = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(lista_de_imagems[0])
            for imagem in lista_de_imagems[1:]:
                anexar_imagems = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/input').send_keys(imagem)
                sleep(3)

        elif info == "N":
            anexar_imagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input').send_keys(caminho_formatado)

        else:
            sys.exit('Fechando o programa')
        sleep(5)

        texto_imagem = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p').send_keys(text_img, Keys.ENTER)
        sleep(5)
        texto_complementar = 'Automação de envio de texto concluida com sucesso!\n -Tenha um otimo dia :)'
        texto_complemento = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(texto_complementar, Keys.ENTER)

        sleep(15)
driver.quit()
print('Programa finalizado.')