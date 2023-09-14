

################################################
import pprint
import requests
import tkinter as tk
from PIL import Image, ImageTk

URL = 'https://www.deckofcardsapi.com/api/deck/1jm3vbs518ut/draw/?count=2'

req = requests.get(URL)
dados_recebidos = req.json()
pprint.pprint(dados_recebidos)
pprint.pprint(dados_recebidos['cards'][0]['image'])
print(dados_recebidos['cards'][1]['image'])
# Função para atualizar a imagem da carta
def pegar_carta():
    link_imagem1 = dados_recebidos['cards'][0]['image']
    imagem_carta1 = Image.open(link_imagem1)
    pprint.pprint(imagem_carta1)
    foto1 = ImageTk.PhotoImage(imagem_carta1)
    
    link_imagem2 = dados_recebidos['cards'][1]['image']
    imagem_carta2 = Image.open(link_imagem2)
    foto2 = ImageTk.PhotoImage(imagem_carta2)

    # Alterne entre as duas imagens ao pressionar o botão
    if label_imagem.config('image')[-1] == str(foto1):
        label_imagem.config(image=foto2)
    else:
        label_imagem.config(image=foto1)

    label_imagem.image = foto1  # Mantém uma referência à imagem para evitar que seja coletada pelo garbage collector

# Cria uma janela
janela = tk.Tk()
janela.title("Carta de Baralho")

# Botão para pegar a carta
botao = tk.Button(janela, text="Pegar Carta", command=pegar_carta)
botao.pack()

# Label para exibir a imagem da carta
label_imagem = tk.Label(janela)
label_imagem.pack()

# Inicia a interface gráfica
janela.mainloop()










# pprint.pprint(dados_recebidos.keys())
# pprint.pprint(dados_recebidos['deck_id'])
# pprint.pprint(dados_recebidos['remaining'])
# pprint.pprint(dados_recebidos['shuffled'])
# pprint.pprint(dados_recebidos['success'])
# #pprint.pprint(dados_recebidos['piles'])

#print(req.status_code)
#print(dados_recebidos)
#requests.models.Response

#if req.status_code == 200:
#    print('Requisição bem sucedida')
#print('-----------------------')
#for pokemon in dados_recebidos['pokemon_species']:
#     print(pokemon['name'])
# print('-----------------------')
# for pokemon in dados_recebidos['types']:
#     print(pokemon['name'])     
# print('-----------------------')

