import tkinter as tk

from tkinter import Tk
from Function import*
from tkinter import ttk
from tkinter import  END
from tkinter import Tk, Canvas, Frame, BOTH, W , ttk

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()

    def create_widgets(self):
        self.ip_label=tk.Label(text = "Ipv4 :")
        self.ip_label.place(x=440,y=20)
        self.ip = tk.StringVar() 
        self.ip_choosen = tk.ttk.Combobox(width = 20, textvariable = self.ip)
        self.ip_choosen['values'] = ('With Class','No Class') 
        self.ip_choosen.place(x=500,y=20)


        bouton_generer = tk.Button( text='Validate', command=self.get_selected)
        bouton_generer.place(x=670,y=20)

    def get_selected(self):
        str_ip = self.ip_choosen.get()
        if(str_ip=="With Class"):
            self.ip_label=tk.Label(text = "Adress Ip")
            self.ip_label.place(x=250,y=100)
            self.ip_texte = tk.StringVar()
            self.input_ip = tk.Entry(self,width=20,textvariable=self.ip_texte)
            self.input_ip.place(x=320,y=100)

            bouton_generer = tk.Button( text='Result', command=self.resultat_With_Class)
            bouton_generer.place(x=320,y=150)
        if(str_ip=="No Class"):
            self.ip_label=tk.Label(text = "Adress Ip :")
            self.ip_label.place(x=250,y=100)
            self.cidr_label=tk.Label(text = "CIDR :")
            self.cidr_label.place(x=250,y=150)
            self.ip_texte = tk.StringVar()
            self.cidr_texte = tk.StringVar()
            self.input_ip = tk.Entry(self,width=20,textvariable=self.ip_texte)
            self.input_cidr = tk.Entry(self,width=20,textvariable=self.cidr_texte)
            self.input_ip.place(x=320,y=100)
            self.input_cidr.place(x=320,y=150)

            bouton_generer = tk.Button( text='Result', command=self.resultat_No_Class)
            bouton_generer.place(x=320,y=200)

    def resultat_No_Class(self):
        str_ip = self.input_ip.get()
        str_cidr = self.input_cidr.get()
        function = Function()
        result = function._ipv4_no_class(str_ip,int(str_cidr))
        self.adress_label=tk.Label(text = "Adress Ip")
        self.adress_label.place(x=0,y=300)
        self.result1_label=tk.Label(text = result[0])
        self.result1_label.place(x=0,y=330)


        self.mask_label=tk.Label(text = "Masque")
        self.mask_label.place(x=100,y=300)
        self.result3_label=tk.Label(text = result[1])
        self.result3_label.place(x=100,y=330)

        self.reseaux_label=tk.Label(text = "Adress Reseaux")
        self.reseaux_label.place(x=200,y=300)
        self.result4_label=tk.Label(text = result[2])
        self.result4_label.place(x=200,y=330)

        self.diffusion_label=tk.Label(text = "Adress Diffusion")
        self.diffusion_label.place(x=300,y=300)
        self.result5_label=tk.Label(text = result[3])
        self.result5_label.place(x=300,y=330)

        self.first_label=tk.Label(text = "First Adress")
        self.first_label.place(x=400,y=300)
        self.result6_label=tk.Label(text = result[4])
        self.result6_label.place(x=400,y=330)

        self.last_label=tk.Label(text = "Last Adress")
        self.last_label.place(x=500,y=300)
        self.result7_label=tk.Label(text = result[5])
        self.result7_label.place(x=500,y=330)

        self.disponible_label=tk.Label(text = "Nombre  Adress Disponible")
        self.disponible_label.place(x=600,y=300)
        self.result8_label=tk.Label(text = result[6])
        self.result8_label.place(x=600,y=330)

    def resultat_With_Class(self):
        str_ip = self.input_ip.get()
        function = Function()
        result = function._ipv4_with_class(str_ip)
        self.adress_label=tk.Label(text = "Adress Ip")
        self.adress_label.place(x=0,y=300)
        self.result1_label=tk.Label(text = result[0])
        self.result1_label.place(x=0,y=330)

        self.class_label=tk.Label(text = "Class")
        self.class_label.place(x=100,y=300)
        self.result2_label=tk.Label(text = result[1])
        self.result2_label.place(x=100,y=330)

        self.mask_label=tk.Label(text = "Masque")
        self.mask_label.place(x=200,y=300)
        self.result3_label=tk.Label(text = result[2])
        self.result3_label.place(x=200,y=330)

        self.reseaux_label=tk.Label(text = "Adress Reseaux")
        self.reseaux_label.place(x=300,y=300)
        self.result4_label=tk.Label(text = result[3])
        self.result4_label.place(x=300,y=330)

        self.diffusion_label=tk.Label(text = "Adress Diffusion")
        self.diffusion_label.place(x=400,y=300)
        self.result5_label=tk.Label(text = result[4])
        self.result5_label.place(x=400,y=330)

        self.first_label=tk.Label(text = "First Adress")
        self.first_label.place(x=500,y=300)
        self.result6_label=tk.Label(text = result[5])
        self.result6_label.place(x=500,y=330)

        self.last_label=tk.Label(text = "Last Adress")
        self.last_label.place(x=600,y=300)
        self.result7_label=tk.Label(text = result[6])
        self.result7_label.place(x=600,y=330)

        self.disponible_label=tk.Label(text = "Nombre  Adress Disponible")
        self.disponible_label.place(x=700,y=300)
        self.result8_label=tk.Label(text = result[7])
        self.result8_label.place(x=700,y=330)

app = Main()
app.title("Ip Configuration")
app.geometry("1000x800")
app.mainloop()