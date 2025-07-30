import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random
import os

# Banco de palavras para compor as frases
BANCO_DE_PALAVRAS = {
    "adjetivos": [
        "vermelha", "lindo", "zangada", "branco", "verde-escuro", "amarelo-canário",
        "franco-brasileiro", "mal-educado", "feliz", "bom", "azul", "triste",
        "grande", "magrelo", "avermelhado", "apaixonado", "bonito", "alta",
        "rápido", "amarelas", "simpática", "competente", "fácil", "verdes",
        "veloz", "comum", "paulista", "cearense", "brasileiro", "italiano", "romeno"
    ],
    "adverbios": [
        "aqui", "ali", "atrás", "longe", "perto", "embaixo", "hoje", "amanhã",
        "nunca", "cedo", "tarde", "antes", "bem", "mal", "rapidamente", "devagar",
        "calmamente", "pior", "sim", "certamente", "certo", "decididamente", "não",
        "nunca", "jamais", "nem", "tampouco", "talvez", "quiçá", "possivelmente",
        "provavelmente", "porventura", "muito", "pouco", "tão", "bastante", "menos",
        "quanto", "salvo", "senão", "somente", "só", "unicamente", "apenas",
        "inclusivamente", "também", "mesmo", "ainda", "primeiramente", "ultimamente", "depois"
    ],
    "artigos": [
        "o", "a", "os", "as", "um", "uma", "uns", "umas"
    ],
    "conjucoes": [
        "e", "nem", "também", "bem como", "não só", "mas também", "mas", "porém",
        "contudo", "todavia", "entretanto", "no entanto", "não obstante", "ou", "já",
        "ora", "quer", "seja", "logo", "pois", "portanto", "assim", "por isso",
        "por consequência", "por conseguinte", "que", "porque", "porquanto", "pois",
        "isto é", "se", "visto que", "uma vez que", "já que", "pois que", "como",
        "embora", "conquanto", "ainda que", "mesmo que", "se bem que", "posto que",
        "caso", "desde", "salvo se", "desde que", "exceto se", "contando que",
        "conforme", "consoante", "segundo", "a fim de que", "para que",
        "à proporção que", "à medida que", "ao passo que", "quanto mais", "quando",
        "enquanto", "agora que", "logo que", "assim que", "tanto que", "apenas",
        "assim como", "tal", "qual", "tanto como", "tão que", "tal que", "tamanho que",
        "de forma que", "de modo que", "de sorte que", "de tal forma que"
    ],
    "interjeicoes": [
        "Oh!", "Ah!", "Oba!", "Viva!", "Opa!", "Vamos!", "Força!", "Coragem!", "Ânimo!",
        "Adiante!", "Apoiado!", "Boa!", "Bravo!", "Tomara!", "Oxalá!", "Ai!", "Ui!",
        "Nossa!", "Cruz!", "Caramba!", "Vixe!", "Diabo!", "Puxa!", "Pô!", "Raios!", "Ora!",
        "Psiu!", "Silêncio!", "Uf!", "Ufa!", "Credo!", "Cruzes!", "Uh!", "Cuidado!",
        "Atenção!", "Olha!", "Alerta!", "Sentido!", "Claro!", "Tá!", "Hã-hã!",
        "Francamente!", "Xi!", "Chega!", "Basta!", "Hum!", "Epa!", "Qual!", "Socorro!",
        "Aqui!", "Piedade!", "Ajuda!", "Olá!", "Alô!", "Ei!", "Tchau!", "Adeus!", "Rua!",
        "Xô!", "Fora!", "Passa!"
    ],
    "numerais": [
        "um", "sete", "vinte e oito", "cento e noventa", "mil", "primeiro",
        "vigésimo segundo", "nonagésimo", "milésimo", "duplo", "triplo", "quádruplo",
        "quíntuplo", "um meio", "um terço", "três décimos", "dúzia", "cento", "dezena", "quinzena"
    ],
    "preposicoes": [
        "a", "após", "até", "com", "de", "em", "entre", "para", "sobre", "como",
        "conforme", "consoante", "durante", "exceto", "fora", "mediante", "salvo",
        "segundo", "senão", "acima de", "a fim de", "apesar de", "através de",
        "de acordo com", "depois de", "em vez de", "graças a", "perto de", "por causa de"
    ],
    "pronomes": [
        "eu", "tu", "ele", "nós", "vós", "eles", "me", "mim", "comigo", "o", "a", "se",
        "conosco", "vos", "você", "senhor", "Vossa Excelência", "Vossa Eminência", "meu",
        "tua", "seus", "nossas", "vosso", "sua", "este", "essa", "aquilo", "tal", "que",
        "quem", "qual", "quanto", "onde", "a qual", "cujo", "quantas", "algum",
        "nenhuma", "todos", "muitas", "nada", "algo"
    ],
    "substantivos": [
        "casa", "amor", "roupa", "livro", "felicidade", "passatempo", "arco-íris",
        "beija-flor", "segunda-feira", "malmequer", "folha", "chuva", "algodão",
        "pedra", "quilo", "território", "chuvada", "jardinagem", "açucareiro",
        "livraria", "Flávia", "Alice Miguel", "Sophia Arthur", "Helena Bernardo",
        "Valentina Heitor", "Laura Davi", "Isabella Lorenzo", "Manuela Théo",
        "Júlia Pedro", "Brasil", "Carnaval", "Nilo", "Serra da Mantiqueira", "mãe",
        "computador", "papagaio", "uva", "planeta", "rebanho", "cardume", "pomar",
        "arquipélago", "constelação", "mesa", "cachorro", "samambaia", "Felipe",
        "beleza", "pobreza", "crescimento", "calor", "estudante", "jovem", "artista",
        "vítima", "pessoa", "criança", "gênio", "indivíduo", "formiga", "crocodilo",
        "mosca", "baleia", "besouro", "lápis", "tórax", "práxis"
    ],
    "verbos": [
        "cantar", "amar", "vender", "prender", "partir", "abrir", "medir", "fazer",
        "ouvir", "haver", "poder", "crer", "ser", "ir", "comer", "dançar", "saltar",
        "escorregar", "sorrir", "rir", "estar", "ter", "parecer", "ficar",
        "tornar-se", "continuar", "andar", "permanecer", "falir", "banir", "reaver",
        "colorir", "demolir", "adequar", "chover", "nevar", "ventar", "anoitecer",
        "escurecer", "latir", "miar", "cacarejar", "mugir", "convir", "custar",
        "acontecer", "aceitado", "aceito", "ganhado", "ganho", "pagado", "pago",
        "arrepender-se", "suicidar-se", "zangar-se", "queixar-se", "abster-se",
        "dignar-se", "pentear", "pentear-se", "sentar", "sentar-se", "enganar",
        "enganar-se", "debater", "debater-se"
    ]
}

# Gera uma frase aleatória combinando palavras do banco de palavras
def gerar_frase():
    
    # Seleciona uma palavra aleatória de cada classe
    palavras = {nome: random.choice(lista) for nome, lista in BANCO_DE_PALAVRAS.items()}

    # Estrutura da frase
    frase_partes = []
    
    # Primeira parte da frase
    i = random.randint(1, 3)
    if i == 1:
        frase_partes.append(palavras["artigos"].capitalize())
    elif i == 2:
        frase_partes.append(palavras["artigos"].capitalize())
        frase_partes.append(palavras["pronomes"])
    else: # i == 3
        frase_partes.append(palavras["pronomes"].capitalize())

    frase_partes.append(palavras["substantivos"])

    # Segunda parte da frase
    test = False
    i = random.randint(1, 6)
    if i == 1:
        frase_partes.append(palavras["verbos"])
    elif i == 2:
        frase_partes.append(palavras["adverbios"])
    elif i == 3:
        frase_partes.append(palavras["adjetivos"])
    elif i == 4:
        frase_partes.append(f'{palavras["verbos"]}.')
        frase_partes.append(palavras["interjeicoes"])
        test = True
    elif i == 5:
        frase_partes.append(f'{palavras["adverbios"]}.')
        frase_partes.append(palavras["interjeicoes"])
        test = True
    else: # i == 6
        frase_partes.append(f'{palavras["adjetivos"]}.')
        frase_partes.append(palavras["interjeicoes"])
        test = True

    # Conjunção (capitalizada se a frase anterior terminou)
    conjuncao = palavras["conjucoes"]
    if test:
        conjuncao = conjuncao.capitalize()
    frase_partes.append(conjuncao)

    # Terceira parte da frase
    frase_partes.append(palavras["preposicoes"])
    
    i = random.randint(1, 6)
    if i <= 3: # Casos 1, 2, 3
        palavras_finais = {
            1: random.choice(BANCO_DE_PALAVRAS["verbos"]),
            2: random.choice(BANCO_DE_PALAVRAS["adverbios"]),
            3: random.choice(BANCO_DE_PALAVRAS["adjetivos"])
        }
        frase_partes.append(palavras_finais[i])
    else: # Casos 4, 5, 6
        frase_partes.append(palavras["numerais"])
        palavras_finais = {
            4: random.choice(BANCO_DE_PALAVRAS["verbos"]),
            5: random.choice(BANCO_DE_PALAVRAS["adverbios"]),
            6: random.choice(BANCO_DE_PALAVRAS["adjetivos"])
        }
        frase_partes.append(palavras_finais[i])

    # Junta todas as partes com espaços e adiciona um ponto final
    return ' '.join(frase_partes) + "."

# Interface gráfica
class AppGeradorFrases:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Frases Motivacionais")
        self.largura, self.altura = 819, 474
        self.root.geometry(f"{self.largura}x{self.altura}")
        self.root.resizable(False, False)

        # Guarda a imagem de fundo atual para exportação
        self.imagem_fundo_pil = None
        self.frase_atual = ""
        
        # Canvas para exibir imagem e texto
        self.canvas = tk.Canvas(root, width=self.largura, height=self.altura)
        self.canvas.pack()

        # Frame para os botões
        frame_botoes = tk.Frame(root, bg='white')
        frame_botoes.place(relx=0.99, rely=0.99, anchor='se')

        # Botões
        btn_gerar = tk.Button(frame_botoes, text="Gerar Nova Frase", command=self.atualizar_frase_e_imagem)
        btn_gerar.pack(side=tk.LEFT, padx=5, pady=5)

        btn_exportar = tk.Button(frame_botoes, text="Exportar Imagem", command=self.exportar_imagem)
        btn_exportar.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Carrega a primeira frase e imagem
        self.atualizar_frase_e_imagem()

    # Escolhe uma nova imagem, gera uma nova frase e atualiza o canvas
    def atualizar_frase_e_imagem(self):
        # Escolhe uma imagem de fundo aleatória
        nomes_imagens = ["1.png", "2.png", "3.png"]
        try:
            caminho_imagem = random.choice(nomes_imagens)
            self.imagem_fundo_pil = Image.open(caminho_imagem)
        except (FileNotFoundError, IndexError):
            messagebox.showerror("Erro de Imagem", "Não foi possível encontrar as imagens '1.png', '2.png' ou '3.png'.")
            self.imagem_fundo_pil = Image.new('RGB', (self.largura, self.altura), color = 'grey')

        # Converte para formato do Tkinter e exibe no canvas
        self.imagem_fundo_tk = ImageTk.PhotoImage(self.imagem_fundo_pil)
        self.canvas.create_image(0, 0, anchor='nw', image=self.imagem_fundo_tk)

        # Gera a frase
        self.frase_atual = gerar_frase()

        # Adiciona o texto sobre a imagem
        self.canvas.delete("frase", "sombra") # Limpa texto anterior
        
        # Sombra para melhor legibilidade
        self.canvas.create_text(
            (self.largura / 2) + 2, (self.altura / 2) + 2,
            text=self.frase_atual,
            fill="black",
            font=("Arial", 28, "bold"),
            justify=tk.CENTER,
            width=self.largura - 60, # Largura máxima do texto para quebra de linha
            tags="sombra"
        )
        # Texto principal
        self.canvas.create_text(
            self.largura / 2, self.altura / 2,
            text=self.frase_atual,
            fill="white",
            font=("Arial", 28, "bold"),
            justify=tk.CENTER,
            width=self.largura - 60,
            tags="frase"
        )

    # Salva a imagem atual com o texto sobreposto em um novo arquivo PNG
    def exportar_imagem(self):
        if not self.imagem_fundo_pil or not self.frase_atual:
            messagebox.showwarning("Aviso", "Não há imagem para exportar.")
            return

        # Abre uma cópia da imagem de fundo para desenhar
        imagem_para_salvar = self.imagem_fundo_pil.copy()
        draw = ImageDraw.Draw(imagem_para_salvar)

        # Configura a fonte
        try:
            fonte = ImageFont.truetype("arialbd.ttf", 32) # Bold
        except IOError:
            fonte = ImageFont.load_default(size=32)

        # Prepara o texto para o desenho multiline
        def get_text_dimensions(draw_obj, text, font_obj):
            if hasattr(draw_obj, 'textbbox'):
                bbox = draw_obj.textbbox((0, 0), text, font=font_obj, align='center', spacing=4)
                return bbox[2] - bbox[0], bbox[3] - bbox[1]
            else: # Fallback para versões antigas do Pillow
                return draw_obj.textsize(text, font=font_obj, spacing=4)
        
        linhas = []
        palavras_frase = self.frase_atual.split()
        linha_atual = ""
        for palavra in palavras_frase:
            largura_teste, _ = get_text_dimensions(draw, linha_atual + " " + palavra if linha_atual else palavra, fonte)
            if largura_teste <= self.largura - 80: # Margem um pouco maior para segurança
                linha_atual += " " + palavra if linha_atual else palavra
            else:
                linhas.append(linha_atual)
                linha_atual = palavra
        linhas.append(linha_atual)
        
        texto_quebrado = "\n".join(linhas)
        
        # Usa textbbox para obter a altura total real e centralizar verticalmente
        if hasattr(draw, 'textbbox'):
            _, top, _, bottom = draw.textbbox((0,0), texto_quebrado, font=fonte, align='center', spacing=4)
            altura_total_texto = bottom - top
            pos_y_inicial = (self.altura - altura_total_texto) / 2
        else: # Fallback
            largura_total, altura_total_texto = get_text_dimensions(draw, texto_quebrado, fonte)
            pos_y_inicial = (self.altura - altura_total_texto) / 2

        # Desenha o texto (sombra primeiro, depois o texto branco)
        draw.text((self.largura/2 + 2, pos_y_inicial + 2), texto_quebrado, font=fonte, fill='black', anchor="ma", align='center', spacing=4)
        draw.text((self.largura/2, pos_y_inicial), texto_quebrado, font=fonte, fill='white', anchor="ma", align='center', spacing=4)
        
        # Abre a janela de "salvar como"
        caminho_arquivo = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
            title="Salvar imagem como..."
        )

        if caminho_arquivo:
            imagem_para_salvar.save(caminho_arquivo)
            messagebox.showinfo("Sucesso", f"Imagem salva em:\n{caminho_arquivo}")

# Execução do programa
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGeradorFrases(root)
    root.mainloop()
