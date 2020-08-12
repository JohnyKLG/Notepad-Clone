from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.scrolledtext as st

win = Tk()
win.iconbitmap('c:/Users/Jonathan/Desktop/note.ico')
win.title('Sem título - Bloco de notas')
win.geometry('944x450')
win.columnconfigure(0, weight=1)
win.rowconfigure(0, weight=1)

def novo():
    txt.delete(1.0, END)
    win.title('Sem título - Bloco de notas')
    b0.entryconfig(2, state=DISABLED)
def abrir():
    global path
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt.insert(END, text)
        path = filepath
    win.title(f"{path} - Bloco de notas")
    b0.entryconfig(2, state=NORMAL)
def salvar():
    arquivo = open(f"{path}", "w")
    text = txt.get(1.0, END)
    arquivo.write(text)
    win.title(f"{path} - Bloco de notas")
def salvar_como():
    global path
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt.get(1.0, END)
        output_file.write(text)
        path = filepath
    win.title(f"{path} - Bloco de notas")
    b0.entryconfig(2, state=NORMAL)
def sair():
    win.destroy()





def ajuda():
    window = Toplevel(win)
    window.title('Sobre o Bloco de notas')
    window.geometry('458x375')
    window.resizable(0,0)
    window.focus()

mn = Menu(win)
# Cascata do botão 0
b0 = Menu(mn, tearoff=0)
b0.add_command(label='Novo', command=novo)
b0.add_command(label='Abrir...', command=abrir)
b0.add_command(label='Salvar', command=salvar, state=DISABLED)
b0.add_command(label='Salvar como...', command=salvar_como)
b0.add_separator()
b0.add_command(label='Configurar Página...')
b0.add_command(label='Imprimir...')
b0.add_separator()
b0.add_command(label='Sair', command=sair)
# Cascata do botão 1
b1 = Menu(mn, tearoff=0)
b1.add_command(label='Desfazer', state=DISABLED)
b1.add_separator()
b1.add_command(label='Recortar', state=DISABLED)
b1.add_command(label='Copiar', state=DISABLED)
b1.add_command(label='Colar', state=DISABLED)
b1.add_command(label='Excluir', state=DISABLED)
b1.add_separator()
b1.add_command(label='Localizar...')
b1.add_command(label='Localizar próxima')
b1.add_command(label='Substituir...')
b1.add_command(label='Ir para...')
b1.add_separator()
b1.add_command(label='Selecionar tudo')
b1.add_command(label='Hora/data')
# Cascata do botão 2
b2 = Menu(mn, tearoff=0)
b2.add_command(label='Quebra automática de linha')
b2.add_command(label='Fonte...')
# Cascata do botão 3
b3 = Menu(mn, tearoff=0)
b3.add_command(label='Barra de status')
# Cascata do botão 4
b4 = Menu(mn, tearoff=0)
b4.add_command(label='Exibir Ajuda')
b4.add_separator()
b4.add_command(label='Sobre o Bloco de notas', command=ajuda)
# Botões do menu
mn.add_cascade(label='Arquivo', menu=b0)
mn.add_cascade(label='Editar', menu=b1)
mn.add_cascade(label='Formatar', menu=b2)
mn.add_cascade(label='Exibir', menu=b3)
mn.add_cascade(label='Ajuda', menu=b4)
win.config(menu=mn)
# Área de texto
def currentCur(event):
    cur = txt.index(CURRENT).split('.')
    if cur[1] == '0':
        cur[1] = '1'
    bs0.config(text='Ln '+cur[0]+', Col '+cur[1])
txt = st.ScrolledText(win)
txt.grid(column=0,row=0, sticky='nsew')
txt.bind('<Key>', currentCur)
txt.bind('<Button>', currentCur)
# Barra de status
bs0 = Label(win, text='Ln 1, Col 1', anchor=E)
bs0.grid(column=0,row=1, padx=(1, 165), sticky='nsew')

win.mainloop()