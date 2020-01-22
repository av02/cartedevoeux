import tkinter
textes = {
    "question nom":{
        "fr":"quel est ton nom?",
        "en":"what's your name?",
        "es":"¿como te llamas?"
    },
    "nom_trop_long":{
        "fr":"ton nom est réelement si long?,
        "en":"your name is too long",
        "es":"tu nombre es demasiado largo"
    }
}

class ecran_base:
    """
    fenetre :  une fenetre tkinter
    """
    def __init__(self,fenetre):
        self.langue = "fr"
        self.fenetre = fenetre
        self.canva = tkinter.Canvas(fenetre,,height=350,width=350,bd=0)

        self.nom = tkinter.StringVar()
        self.choix_bouton = tkinter.StringVar()
        self.txtlangue = textes["question nom"][self.langue]
        
        self.question = self.canva.create_text(100,145,text = self.txtlangue)
        self.champs_nom = tkinter.Entry(self.fenetre,textvariable = self.nom,width=10)
        self.bouton_validation = tkinter.Button(self.fenetre,text = "✅",command= self._bouton_commande)
        self.menu_langue = tkinter.OptionMenu(self.fenetre,self.choix_bouton,"français","espagnol","anglais",command = self._langue )

        self.choix_bouton.set("français")

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
        self.question.itemconfig(text = textes["question_nom"][self.langue]
        try:
            self.message_erreur.itemconfig(text = textes["nom_trop_long"][self.langue]
                             

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
        self.message_erreur = self.canva.create_text(100,195,text = textes["nom_trop_long"][self.langue])
    
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
        
