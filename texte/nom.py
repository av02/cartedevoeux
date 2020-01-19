import tkinter
textes = {
    "question nom":{
        "fr":"quel est ton nom?",
        "en":"what's your name?",
        "es":"¿como te llamas?"
    }
}

class ecran_base:
    """
    fenetre :  une fenetre tkinter
    """
    def __init__(self,fenetre):
        self.langue = "fr"
        self.fenetre = fenetre

        self.nom = tkinter.StringVar()
        self.txtlangue = tkinter.StringVar()
        self.choix_bouton = tkinter.StringVar()
        self.txtlangue.set(textes["question nom"][self.langue])
        
        self.question = tkinter.Label(self.fenetre,textvariable = self.txtlangue)#TODO edit bg:backgroung is not transparent
        self.champs_nom = tkinter.Entry(self.fenetre,textvariable = self.nom,width=10)
        self.bouton_validation = tkinter.Button(self.fenetre,text = "✅",command= self._bouton_commande)
        self.menu_langue = tkinter.OptionMenu(self.fenetre,self.choix_bouton,"français","espagnol","anglais",command = self._langue )

        self.choix_bouton.set("français")

        self.question.place(x=100,y=145)
        self.champs_nom.place(x=100,y=170)
        self.bouton_validation.place(x=220,y=170)
        self.menu_langue.place(x=265,y=325)
        

    def _langue(self,choix):
        """
        méthode interne
        change la langue de la question
        """ 
        if choix == "français":
            self.langue = "fr"
        elif choix == "anglais":
            self.langue = "en"
        elif choix == "espagnol":
            self.langue = "es"
        self.txtlangue.set(textes["question nom"][self.langue])

    def _bouton_commande(self):
        """
        méthode interne, reaction au bouton pour renvoyer le nom
        """
        nom = self.nom.get()
        if len(nom)>15:
            self._message_erreur()
        else:
            self.destroy()
            self.nom = nom
            
        
    def _message_erreur(self):
        """
        afficher une erreur si le nom est trop long
        """
        self.message_erreur = tkinter.Label(self.fenetre,text = "ton nom est réélement si long?")
        self.message_erreur.place(x=100,y=195)
    
    def get_nom(self):
        """
        permet de recuperer le nom une fois saisi
        """
        return self.nom

    def destroy(self):
        """
            supprime la page de demande
        """
        self.fenetre.destroy()
        """self.bouton_validation.destroy()
        self.champs_nom.destroy()
        self.menu_langue.destroy()
        self.question.destroy()
        try:
            self.message_erreur.destroy()
        except:
            pass"""
