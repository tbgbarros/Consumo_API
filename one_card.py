import requests
import tkinter as tk
import pprint
from PIL import Image, ImageTk
from io import BytesIO  # usei para baixar a imgem pois por url a imagem nao abre

#https://www.deckofcardsapi.com/api/deck/new/draw/?count=2

DECK = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(DECK)
dados_recebidos = response.json()
pprint.pprint(dados_recebidos)

#captura do deckid para uso
deck_id = dados_recebidos["deck_id"]
pprint.pprint(deck_id)


URL = f"https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
pprint.pprint(URL)
resp_deck = requests.get(URL)
cartas = resp_deck.json()
pprint.pprint(cartas)


URL2 = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=2"
cartas = requests.get(URL2)
url2 = requests.get(URL2)

if cartas.status_code == 404:
    print("Não encontrado")
    
else:
    def pegar_carta():
        if resp_deck.status_code == 200:           
            link_imagem1 = cartas["cards"][0]["image"]
            link_imagem2 = cartas["cards"][1]["image"]
            pprint.pprint(link_imagem1)
            pprint.pprint(link_imagem2)

            imagem_carta1 = Image.open(BytesIO(resp_deck.get(link_imagem1).content))
            foto1 = ImageTk.PhotoImage(imagem_carta1)

            imagem_carta2 = Image.open(BytesIO(resp_deck.get(link_imagem2).content))
            foto2 = ImageTk.PhotoImage(imagem_carta2)

            if label_imagem.config("image")[-1] == str(foto1):
                label_imagem.config(image=foto2)
            else:
                label_imagem.config(image=foto1)

            label_imagem.image = foto1

janela = tk.Tk()
janela.geometry("300x400")
janela.title("BLACKJACK")
tk.Label(text="BEM VINDO AO BLACKJACK DO PAI").pack()

botao = tk.Button(janela, text="PEDIR CARTA", command=pegar_carta)
botao.pack()

#botao = tk.Button(janela, text="OUTRA CARTA", command=pegar_segunda_carta)
botao.pack()

label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
