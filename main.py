from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import filedialog
import os
import pygame


class PlayTk:

    def __init__(self):

        pygame.mixer.init()

        self.window = ThemedTk(theme='black')
        self.window.title('Tocador de Musica')
        self.window.resizable(0,0)
        self.window.geometry('300x400+300+50')
        self.window.config(bg='#333333')

        self.img_adicionar = PhotoImage(file='imagem/add.png')
        self.img_proximo = PhotoImage(file='imagem/next.png')
        self.img_parar = PhotoImage(file='imagem/pause.png')
        self.img_play = PhotoImage(file='imagem/play.png')
        self.img_voltar = PhotoImage(file='imagem/previus.png')
        self.img_remover = PhotoImage(file='imagem/remove.png')

        self.status = 0

        self.local = ""

        self.list = Listbox(self.window, bg='#333333',height=12,fg='gray', font='Arial 12',
                            selectbackground='#333333')
        self.list.pack(fill=X, padx= 15, pady=15)

        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady=10)

        self.botao_remove = ttk.Button(self.frame, image= self.img_remover,command=self.retirar_musica)
        self.botao_remove.grid(row=0,column=0, padx=1)

        self.botao_add = ttk.Button(self.frame, image= self.img_adicionar, command=self.selecionar_musica)
        self.botao_add.grid(row=0, column=1,padx=1)

        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(pady=10)

        self.botao_voltar = ttk.Button(self.frame2, image= self.img_voltar, command=self.voltar_musica)
        self.botao_voltar.grid(row=1, column=0, padx=1)

        self.botao_play = ttk.Button(self.frame2, image=self.img_play,command=self.tocar_musica)
        self.botao_play.grid(row=1, column=1, padx=1)

        self.botao_proximo = ttk.Button(self.frame2, image=self.img_proximo, command=self.proxima_musica)
        self.botao_proximo.grid(row=1, column=2, padx=1)

        self.volume = ttk.Scale(self.window, from_=0, to=1, command=self.volume_musica)
        self.volume.pack(fill=X, padx=10, pady=1)

        self.window.mainloop()

    def selecionar_musica(self):
        self.local = filedialog.askdirectory()
        arquivo = os.listdir(self.local)

        for arquivo in arquivo:
            self.list.insert(END,str(arquivo))

    def retirar_musica(self):
        self.list.delete(ANCHOR)#faz alguma ação no objeto selecionado pelo mouse

    def proxima_musica(self):
        try:
            proxima = self.list.curselection()[0] + 1
            self.list.select_clear(0, END)
            self.list.activate(proxima)
            self.list.select_set(proxima)
            self.list.yview(proxima)
        except:
            self.tela_erro("Não tem musica para avançar")

    def voltar_musica(self):
        try:
            voltar = self.list.curselection()[0] - 1
            self.list.select_clear(0, END)
            self.list.activate(voltar)
            self.list.select_set(voltar)
            self.list.yview(voltar)
        except:
            self.tela_erro("Não tem musica para voltar")

    def tocar_musica(self):
        try:
            if self.status == 0:
                pygame.mixer.music.load(str(self.local) + "/" + str(self.list.get(ANCHOR)))
                pygame.mixer.music.play()
                self.botao_play.config(image=self.img_parar)
                self.status = 1
            else:
                pygame.mixer.music.pause()
                self.botao_play.config(image=self.img_play)
                self.status = 0
        except:
            self.tela_erro('Não existe musica na lista')

    def tela_erro(self, message):
        window = Toplevel()
        window.title('ERRO')
        window.geometry('300x300+300+50')
        window.resizable(0,0)
        window.config(bg="#444444")

        mensagem = ttk.Label(window, text=str(message))
        mensagem.pack(expand=YES)#expandi o texto para a tela toda

        btn = ttk.Button(window, text='OK', command=window.destroy)
        btn.pack()

    def volume_musica(self, var):
        pygame.mixer.music.set_volume(self.volume.get())


PlayTk()
