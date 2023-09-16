import requests
import tkinter as tk
import pprint
from PIL import Image, ImageTk
from io import BytesIO  # usei para baixar a imgem pois por url a imagem nao abre

#https://www.deckofcardsapi.com/api/deck/new/draw/?count=2

DECK = "https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=2"
response = requests.get(DECK)
dados_recebidos = response.json()
pprint.pprint(dados_recebidos)

#captura do deckid para uso
deck_id = dados_recebidos["deck_id"]
pprint.pprint(deck_id)

janela = tk.Tk()
janela.geometry("300x400")
janela.title("BLACKJACK")
tk.Label(text="BEM VINDO AO BLACKJACK DO PAI").pack() 

URL = f"https://www.deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"

def iniciar_game():
    
    resp_deck = requests.get(URL)
    cartas = resp_deck.json()
    if resp_deck.status_code == 200:           
        link_imagem1 = cartas["cards"][0]["image"]
        link_imagem2 = cartas["cards"][1]["image"]

        imagem_carta1 = Image.open(BytesIO(requests.get(link_imagem1).content))
        foto1 = ImageTk.PhotoImage(imagem_carta1)

        imagem_carta2 = Image.open(BytesIO(requests.get(link_imagem2).content))
        foto2 = ImageTk.PhotoImage(imagem_carta2)

        carta1.config(image=foto1)
        carta1.image = foto1

botao = tk.Button(janela, text="INICIAR GAME", command=iniciar_game)
botao.pack()



carta1 = tk.Label(janela)
carta1.pack()



label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
