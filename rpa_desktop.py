import pyautogui as gui
from time import sleep, time
import win32clipboard
from PIL import Image
from io import BytesIO
import os

def enviar_texto_para_area_de_transferencia(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()

    try:
        win32clipboard.SetClipboardText(texto, win32clipboard.CF_UNICODETEXT)

    except Exception as e:
        print(f"Erro ao enviar texto para a área de transferência: {e}")

    win32clipboard.CloseClipboard()


def lista_de_imagens():
    base_path = os.path.abspath(os.path.dirname(__file__))
    images_path = os.path.join(base_path, 'images')
    image_names = os.listdir(images_path)
    lista_de_imagems = [os.path.join(images_path, name) for name in image_names]
    return lista_de_imagems


def captura_imagem(imagem):

    image = Image.open(imagem)
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def click_relative(x_ratio, y_ratio):
    screen_width, screen_height = gui.size()
    x_pos = int(screen_width * x_ratio)
    y_pos = int(screen_height * y_ratio)
    gui.click(x_pos, y_pos)


largura, altura = gui.size()

click_position1 = (346 / largura, 120 / altura)
click_position2 = (187 / largura, 182 / altura)


arquivo = 'numeros_teste.txt'
arquivo_texto = r'mensagem_convidativa.txt'

start_time = time()

#troca tela e inicio dos envios
gui.hotkey('alt', 'tab')
sleep(2)

pesquisa_numero = click_relative(*click_position1)
gui.click(pesquisa_numero)

gui.press('backspace', presses=15 ,interval=0.1)
sleep(1)
with open(arquivo, "r") as file:
    for numero in file:
        sleep(1)
        numero = int(numero)
        gui.click(pesquisa_numero)
        sleep(1)
        gui.press('backspace', presses=15 ,interval=0.1)
        gui.typewrite(str(numero), interval=0.1)
        sleep(2.5)
        clica_numero = click_relative(*click_position2)
        gui.click(clica_numero)
        sleep(4)

        #envio das imagens no diretorio images
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        lista = lista_de_imagens()
        for image_path in lista:

            captura_imagem(image_path)
            gui.hotkey('ctrl', 'v')
            sleep(1.5)
        
        sleep(2.5)
        gui.typewrite('oi', interval=0.1)
        gui.hotkey('enter')
        sleep(2.5)

        enviar_texto_para_area_de_transferencia(arquivo_texto)
        gui.hotkey('ctrl', 'v')
        sleep(2.5)
        gui.press('enter')
        sleep(2)
        
        #limpar pesquisa e inicia nova conversa
        pesquisa_numero = click_relative(*click_position1)
        gui.click(pesquisa_numero)
        gui.press('backspace', presses=15 ,interval=0.1)


print('Programa finalizado.')
end_time = time()
execution_time = end_time - start_time
print("Tempo de execução: {:.2f} segundos".format(execution_time))
