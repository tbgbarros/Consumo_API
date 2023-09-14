import requests
import pprint
import tkinter as tk
from PIL import Image, ImageTk
# funcao para jogar na memoria para manupular
from io import BytesIO

URL = 'https://www.deckofcardsapi.com/api/deck/1jm3vbs518ut/draw/?count=2'


def pegar_carta():
    response = requests.get(URL)
    dados_recebidos = response.json()
    cartas = []
    # for de leitura de conteudo
    for conteudo in dados_recebidos['cards']:
        link_imagem = conteudo['image']
        imagem_carta = Image.open(BytesIO(requests.get(link_imagem).content))
        foto = ImageTk.PhotoImage(imagem_carta)
        cartas.append(foto)
    # cartas.append(foto2)

    # for de exibicao
    carta1.config(image=cartas[0])
    carta1.image = cartas[0]
    carta2.config(image=cartas[1])
    carta2.image = cartas[1]


# janela
janela = tk.Tk()
janela.geometry("300x700")
janela.title("Bem vindo ao Blackjack")
# botao
botao = tk.Button(janela, text="INICIAR JOGO", command=pegar_carta)
botao.pack()
# exibicao
# label_imagem = tk.Label(janela)
# label_imagem.pack()

carta1 = tk.Label(janela)
carta1.pack()
carta2 = tk.Label(janela)
carta2.pack()

# botao
botao = tk.Button(janela, text="PEDIR MAIS UMA CARTA", command=pegar_carta)
botao.pack()

janela.mainloop()
