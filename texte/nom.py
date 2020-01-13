import tkinter
textes = {
    "question nom":{
        "fr":"quel est ton nom?",
        "an":"what's your name?",
        "es":"¿como te llamas?"
    }
}

class nom:
    def __init__(self):
        self.langue = "fr"
        pass


    def demander_nom(self,fenetre):
        #creer un label/champs de txt
        #ajouter du txt
        #recuperer le nom
        #fermer le label
        #return un label complet
        def command():
            print("coucou")
        self.nom = tkinter.StringVar()
        self.txtlangue = tkinter.StringVar()
        self.txtlangue.set(textes["question nom"][self.langue])
        self.texte = tkinter.Label(fenetre,textvariable = self.txtlangue,bg='red')
        self.texte.pack()
        self.champs = tkinter.Entry(fenetre,textvariable = self.nom,validatecommand = command)
        self.champs.pack()

        v = tkinter.StringVar()

        v.set("français")

        def langue(choix): 
            if choix == "français":
                self.langue = "fr"
            elif choix == "anglais":
                self.langue = "an"
            elif choix == "espagnol":
                self.langue = "es"
            self.txtlangue.set(textes["question nom"][self.langue])

        om = tkinter.OptionMenu(fenetre,v,"français","espagnol","anglais",command = langue )
        om.pack()
        
