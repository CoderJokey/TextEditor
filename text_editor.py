# Librerie del programma implementate
##########################################################
from asyncore import write
from cProfile import label
from gettext import NullTranslations
from pydoc import text
from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter import colorchooser
from tkinter.ttk import Style
from turtle import title
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
##########################################################
##########################################################
# Spazio Dedicato Alle Funzioni
def darkMode():
    if darkmode.get() == 1:
        window.config(background="black")
        percorso.config(background="midnightblue", foreground="White")
        menu_app.config(background="navy", foreground="white", activebackground="purple4", activeforeground="white")
        barra_di_menu.config(background="slateblue3", foreground="white", activebackground="slateblue1", activeforeground="white")
        view.config(background="slateblue3", foreground="white", activebackground="slateblue1", activeforeground="white")
        opzioni.config(background="slateblue3", foreground="white", activebackground="slateblue1", activeforeground="white")
        help_op.config(background="slateblue3", foreground="lightgreen", activebackground="slateblue1", activeforeground="white")
    elif darkmode.get() == 0:
        window.config(background='white')
        percorso.config(background="white", foreground="black")
        menu_app.config(background="white", foreground="black", activebackground="lightgray", activeforeground="black")
        barra_di_menu.config(background="white", foreground="black", activebackground="lightgray", activeforeground="black")
        view.config(background="white", foreground="black", activebackground="lightgray", activeforeground="black")
        opzioni.config(background="white", foreground="black", activebackground="lightgray", activeforeground="black")
        help_op.config(background="white", foreground="black", activebackground="lightgray", activeforeground="red")
    else:
        messagebox.showerror("PythonGuides", "[Code Error 3967] Dark Mode Inactive")

def ErroreFunzione():
    messagebox.showinfo("Message", "Istruzione in via di sviluppo")
    pass

def OpzioniTextEditor():
    messagebox.showinfo("Message", """
                        Versione 1.0 SNAPSHOT
                        In develpment""")
    pass
    
#color picker      
def FontChooseColor():
    color_code = colorchooser.askcolor(title="Colore del Font")
    percorso.config(foreground=color_code[1])
    pass
    
def BackGroundColorChooser():
    my_color = colorchooser.askcolor(title="Background Color")
    percorso.config(background=my_color[1])
    pass

def BottoneCliccato():
    try:
        files = [('All Files', '*.*')]
        f = asksaveasfile(filetypes=files, defaultextension=files, mode="w")
        f.write(percorso.get("1.0", END))
        f.close()
        pass
    except AttributeError:
        messagebox.showinfo("Message", "File impossibile da salvare!")
    
def NewScript():
    percorso.delete("1.0", "end")
    pass
    
def CiaoMondo():
    messagebox.showinfo("Message", "La sofia è nabba")
    pass
    
def FontChoose():
    root = Tk()
    root.geometry("500x350")
    root.title("Scegli Font")
    root.resizable(False, False)
    font_disponibili = sorted(set(font.families()))
    listbox = Listbox(root, selectmode=SINGLE, width=45, height=15)
    listbox.pack(expand=False, side=TOP)
    for f in font_disponibili:
        listbox.insert("end", f)
    
    #definire bene questa parte
    def setFont():
        for i in listbox.curselection():
            fonts = font.Font(family=listbox.get(i), size=14)
        percorso.configure(font=fonts)
    # proseguimento del programma
    btm = Button(root, text="Scegli", font="Ubuntu", width=10, height=1, 
    activebackground="white", activeforeground="darkblue", command=setFont)
    btm.place(y=140)
    btm.pack()
    root.mainloop()
    pass
  
def OpenFile():
    files = [('All Files', '*.*')]
    file = filedialog.askopenfile(filetypes=files, defaultextension=files, mode="r")
    percorso.insert("1.0", file.read())
    pass

def SizeFont():
    root = Tk()
    root.geometry("500x350")
    root.title("Scegli Dimesione")
    root.resizable(False, False)
    font_size = [8, 9, 10 , 11, 12, 13, 14, 16, 18, 20, 22, 24, 28, 32, 36, 40, 48, 56, 64]
    listbox = Listbox(root, selectmode=SINGLE, width=20, height=15)
    listbox.pack(expand=False, side=TOP)
    for f in font_size:
        listbox.insert("end", f)
    
    #definire bene questa parte
    def setFont():
        for i in listbox.curselection():
            fonts = font.Font(size=listbox.get(i))
        percorso.configure(font=fonts)
             
    btm = Button(root, text="Scegli", font=("Ubuntu", 12, "bold"), width=10, height=1, 
    activebackground="white", activeforeground="darkblue",
    command=setFont)
    btm.place(y=140)
    btm.pack()
    root.mainloop()
    pass

def FontStyle():
    root = Tk()
    root.geometry("500x350")
    root.title("Scegli Dimesione")
    font_style = ["italic", "roman", "bold", "normal", "underline", "overstrike"]
    listbox = Listbox(root, selectmode=SINGLE, width=20, height=15)
    listbox.pack(expand=False, side=TOP)
    for f in font_style:
        listbox.insert("end", f)
    
    #definire bene questa parte
    def setFont():
        for i in listbox.curselection():
            if listbox.get(i) == "italic":
                fonts = font.Font(slant=listbox.get(i))
            elif listbox.get(i) == "roman":
                fonts = font.Font(slant=listbox.get(i), underline=0, overstrike=0)
            elif listbox.get(i) == "bold":
                fonts = font.Font(weight=listbox.get(i))
            elif listbox.get(i) == "normal":
                fonts = font.Font(weight=listbox.get(i), underline=0, overstrike=0)
            elif listbox.get(i) == "underline":
                fonts = font.Font(underline=1)
            elif listbox.get(i) == "overstrike":
                fonts = font.Font(overstrike=1)
        
        percorso.configure(font=fonts)
             
    btm = Button(root, text="Scegli", font=("Ubuntu", 12, "bold"), width=10, height=1, 
    activebackground="white", activeforeground="darkblue",
    command=setFont)
    btm.place(y=140)
    btm.pack()
    root.mainloop()

#################################################################################
# Main program                                                                  #
# Dove comincia il programma                                                    #
#################################################################################
window = Tk()
window.configure(bg="white")
window.geometry("600x450")
window.title("Text Editor Python")
window.iconphoto(False, tk.PhotoImage(file="/home/giamma/Immagini/immagine.png"))
# Barra di menu (FILE)
menu_app = Menu(window, background="lightgray", foreground="black", activebackground="white", 
activeforeground="black")
barra_di_menu = Menu(menu_app, tearoff=1, background="white", foreground="black", font="Ubuntu")
barra_di_menu.add_command(label="Nuovo", command=NewScript)
barra_di_menu.add_command(label="Apri File", command=OpenFile)
barra_di_menu.add_command(label="Salva File", command=lambda:BottoneCliccato())
barra_di_menu.add_separator()
menu_app.add_cascade(label="File", menu=barra_di_menu)
minimap = BooleanVar()
minimap.set(True)
darkmode = BooleanVar()
darkmode.set(False)
#Barra di menu (VIEW)
view = Menu(menu_app, tearoff=0, font="Ubuntu", background="white")
view.add_checkbutton(label="Vedi Minimappa", onvalue=1, offvalue=0, variable=minimap)
view.add_checkbutton(label="Dark Mode", onvalue=1, offvalue=0, variable=darkmode, command=darkMode)
menu_app.add_cascade(label="View", menu=view)
# Barra di menu (OPTIONS)
# Scelta del font personalizzata
opzioni = Menu(menu_app, tearoff=0, font="Ubuntu", background="white")
opzioni.add_command(label="TextEditor Info", command=OpzioniTextEditor)
opzioni.add_command(label="Colore del Font", command=FontChooseColor)
opzioni.add_command(label="Colore di Sfondo", command=lambda:BackGroundColorChooser())
opzioni.add_command(label="Cambia Font", command=lambda:FontChoose())
opzioni.add_command(label="Font Style", command=lambda:FontStyle())
opzioni.add_command(label="Font Size", command=lambda:SizeFont())
menu_app.add_cascade(label="Options", menu=opzioni)
# Barra di menu (HELP)
help_op = Menu(menu_app, tearoff=0, font="Ubuntu", background="white")
help_op.add_command(label="Sofia Developer", command=CiaoMondo)
help_op.add_command(label="Settings", command=ErroreFunzione)
menu_app.add_cascade(label="Help", menu=help_op)
# Testo
percorso = Text(window, fg="black", bg="azure", font=("Courier New", 14))
percorso.event_add("<<Save>>", "Control-s")
percorso.pack(expand=True, fill=BOTH)
# Registrazione totale
window.config(menu=menu_app)
window.mainloop()