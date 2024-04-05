# https://dlp.hashtagtreinamentos.com/python/intensivao/login -> SISTEMA código da aula: python2024

# passo a passo
import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.5

# passo 1: Entrar no sistema
# pyautogui.click -> clicar na tela
# pyautogui.write -> escrever texto
# pyautogui.press -> apertar tecla
# pyautogui.hotkey("ctrl","c")

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=947, y=624)
pyautogui.hotkey("ctrl", "t")
# print(pyautogui.size())
# print(pyautogui.position())  # Point(x=947, y=624)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# passo 2: Fazer login
time.sleep(3)
print("Caixa do Email:", str(pyautogui.position()))
pyautogui.click(x=907, y=522)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("backspace")
mail = "email@mail.com"
pyautogui.write(mail)
pyautogui.press("tab")
pyautogui.press("backspace")
passw = "senhadoemail"
pyautogui.write(passw)
print("Logar:", str(pyautogui.position()))
pyautogui.click(x=927, y=707)

# passo 3: Importar base de dados
tabela = pd.read_csv("produtos.csv")
print(tabela)

# passo 4: Cadastrar produtos 1 a 1
for linha in tabela.index:

    time.sleep(2)
    print("Caixa 1:", str(pyautogui.position()))
    pyautogui.click(x=816, y=363)

    ##
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    ##
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    ##
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    ##
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    ##
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    ##
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    ##
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
