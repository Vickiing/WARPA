import pyautogui as gui
from time import sleep, time
from PIL import Image




arquivo = 'numeros_teste.txt'

start_time = time()
texto = '[Teste de envio de mensagem...]'

gui.hotkey('alt', 'tab')
sleep(2)
gui.click(346,120)
gui.press('backspace', presses=15 ,interval=0.1)
sleep(1)
with open(arquivo, "r") as file:
    for numero in file:
        sleep(1)
        numero = int(numero)
        gui.click(346,120)
        sleep(1)
        gui.press('backspace', presses=15 ,interval=0.1)
        gui.typewrite(str(numero), interval=0.1)
        sleep(4)
        gui.click(187,182)
        sleep(4)
        gui.hotkey('ctrl', 'v')
        sleep(2.5)
        gui.typewrite('oi', interval=0.1)
        gui.hotkey('enter')
        sleep(2.5)
        gui.typewrite(texto, interval=0.1)
        gui.press('enter')
        sleep(2)
        #limpar pesquisa e inicia nova conversa
        gui.click(346,120)
        gui.press('backspace', presses=15 ,interval=0.1)


print('Programa finalizado.')
end_time = time()
execution_time = end_time - start_time
print("Tempo de execução: {:.2f} segundos".format(execution_time))
