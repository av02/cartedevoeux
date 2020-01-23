import tkinter 
class fond:
    """
    permet de creer le fond du canva
    """
    def __init__(self,*couleur):
        self.couleur = couleur
        self.fond=[]
        self.canva =[]

    def tracer_fond(self,canva):
        """
        permet de tracer le fond 
        """
        self.canva.append(canva)
        for i in range(35):
            self.fond.append(canva.create_polygon([(350*i/10,0),(350*(i+1)/10,0),((350*(i+1)/10)-350,350),((350*i/10)-350,350)],fill=list(self.couleur)[i%len(list(self.couleur))]))
        

    def changer_couleur(self,couleur:list):
        """
        permet de changer les couleurs
        """
        self.couleur = couleur
        for canva in self.canva:
            for i in range(35):
                canva.itemconfig(self.fond[i],fill=self.couleur[i%len(self.couleur)])


    def clignoter(self,fen,frequence,couleur,_Recursivite=0):
        """
        faire clignoter l'objet

        fen est une fenetre tKinter
        frequence est la frequence de clignotement en ms
        couleur est un ensemble de couleurs
        """
        self.couleur = couleur[_Recursivite%len(couleur)]
        self.changer_couleur(self.couleur)
        def _appel():
            self.clignoter(fen,frequence,couleur,_Recursivite+1)
        fen.after(frequence,_appel)
