import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO  # usei para baixar a imgem pois por url a imagem nao abre


URL = "https://www.deckofcardsapi.com/api/deck/1jm3vbs518ut/draw/?count=6"

response = requests.get(URL)

if response.status_code == 404:
    print("Não encontrado")


def pegar_carta():
    if response.status_code == 200:
        dados_recebidos = response.json()

        link_imagem1 = dados_recebidos["cards"][0]["image"]
        link_imagem2 = dados_recebidos["cards"][1]["image"]

        imagem_carta1 = Image.open(BytesIO(requests.get(link_imagem1).content))
        foto1 = ImageTk.PhotoImage(imagem_carta1)

        imagem_carta2 = Image.open(BytesIO(requests.get(link_imagem2).content))
        foto2 = ImageTk.PhotoImage(imagem_carta2)

        if label_imagem.config("image")[-1] == str(foto1):
            label_imagem.config(image=foto2)
        else:
            label_imagem.config(image=foto1)

        label_imagem.image = foto1


janela = tk.Tk()
janela.geometry("300x380")
janela.title("BLACKJACK")
tk.Label(text="QUE COMEÇE OS JOGOS").pack()

botao = tk.Button(janela, text="PEDIR CARTA", command=pegar_carta)
botao.pack()
label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
