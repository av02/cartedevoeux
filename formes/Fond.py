import tkinter 
class fond:
    """
    descrption ici
    """
    def __init__(self,couleur1,couleur2,couleur3,canva):
        """
        docstring
        """
        self.couleur1 = couleur1
        self.couleur2 = couleur2
        self.couleur3 = couleur3
        self.canva = canva

    def tracer_fond(self):
        """
        docstring
        """
        self.fond1 = self.canva.create_rectangle(0,0,116,350,fill=self.couleur1)
        self.fond2 = self.canva.create_rectangle(116,350,232,0,fill=self.couleur2)
        self.fond3 = self.canva.create_rectangle(232,0,350,350,fill=self.couleur3)
    
    def changer_couleur(self,nouvelle_couleur1,nouvelle_couleur2,nouvelle_couleur3):
        """
        docstring
        """
        self.couleur1 = nouvelle_couleur1
        self.couleur2 = nouvelle_couleur2
        self.couleur3 = nouvelle_couleur3
        self.canva.itemconfig(self.fond1,fill=self.couleur1)
        self.canva.itemconfig(self.fond2,fill=self.couleur2)
        self.canva.itemconfig(self.fond3,fill=self.couleur3)


    def clignoter(self,fen,frequence,liste_couleur:list,_Recursivite=0):
        """
        faire clignoter l'objet

        fen est une fenetre tKinter
        frequence est la frequence de clignotement en ms
        liste_couleur est une liste de listes de 3 couleurs pour  l'ensemble des  couleurs dans l'ordre d'apparition
        """
        couleur = liste_couleur[_Recursivite%len(liste_couleur)]
        self.changer_couleur(couleur[0],couleur[1],couleur[2])
        def _appel():
            self.clignoter(fen,frequence,liste_couleur,_Recursivite=_Recursivite+1)
        fen.after(frequence,_appel)
