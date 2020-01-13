import random
import math

class formes:
    """
    classe qui permet de creer un objet etoile ou sapin


                création d'une étoile

        longueur est la distance du centre vers les points interieurs en pixels\n
        couleur est une couleur au format '#RGB' ou '#RRGGBB' ou 'color'\n
        centrex est  l'absice du centre\n
        centrey est l'ordonnée du centre\n\n\n

                création d'un sapin

        longueur est la hauteur de l'étoile\n
        couleur est une couleur au format '#RGB' ou '#RRGGBB' ou 'color'\n
        centrex est  l'absice de la base \n
        centrey est l'ordonnée de la base \n\n\n


                fonctions disponibles:

        tracer(canva): tracer l'objet  su le canva\n
        editer_couleur(couleur): changer la couleur\n
        editer_position(x,y):nouvelle position de l'objet \n
        clignoter(fen,frequence,liste_couleur): fait clignoter l'objet\n

    """
    def __init__(self,longueur:int,couleur:str,centrex:int,centrey:int,figure:str,couleurFond:str=''):
        """
        création d'un objet

        longueur est la distance du centre vers les points interieurs en pixels
        couleur est une couleur au format '#RGB' ou '#RRGGBB' ou 'color' 
        centrex est  l'absice du centre(etoiles)ou de la base(sapins)
        centrey est l'ordonnée du centre(etoiles)ou de la base(sapins)
        """
        self.longueur = longueur#largeur
        self.couleur = couleur#couleur contour
        self.couleurFond=couleurFond#couleur fond
        self.centre = {"x":centrex,"y":centrey}#centre ou base
        self.canva = None # canvas de definition
        self.id=None # identifiants 
        self.figure = figure
        self.points = self._pos_points(figure)#liste des points 

    def _pos_points(self,figure:str):
        if figure=="etoile":
            return self._pos_points_etoile()
        elif figure == "sapin":
            return self._pos_points_sapin()
        else:
            raise NameError('merci de saisir une forme valide')

    def _pos_points_etoile(self): 
        points=[]
        depart = random.randint(0,360)/180*math.pi
        for x in range(5):
            points.append((self.centre["x"]+math.cos(depart)*self.longueur,self.centre["y"]+math.sin(depart)*self.longueur))
            depart+=36/180*math.pi
            points.append((self.centre["x"]+math.cos(depart)*self.longueur*3,self.centre["y"]+math.sin(depart)*self.longueur*3))
            depart+=36/180*math.pi
        return points

    def _pos_points_sapin(self):
        return [
            (self.centre["x"],self.centre["y"] -self.longueur),#sommet
            (self.centre["x"]-self.longueur/4,self.centre["y"]-7*self.longueur/10),
            (self.centre["x"]-self.longueur/10,self.centre["y"]-7*self.longueur/10),
            (self.centre["x"]-self.longueur/3,self.centre["y"]-4*self.longueur/10),
            (self.centre["x"]-self.longueur/6,self.centre["y"]-4*self.longueur/10),
            (self.centre["x"]-4*self.longueur/10,self.centre["y"]-self.longueur/10),
            (self.centre["x"]-self.longueur/8,self.centre["y"]-self.longueur/10),
            (self.centre["x"]-self.longueur/8,self.centre["y"]),
            (self.centre["x"]+self.longueur/8,self.centre["y"]),
            (self.centre["x"]+self.longueur/8,self.centre["y"]-self.longueur/10),
            (self.centre["x"]+4*self.longueur/10,self.centre["y"]-self.longueur/10),
            (self.centre["x"]+self.longueur/6,self.centre["y"]-4*self.longueur/10),
            (self.centre["x"]+self.longueur/3,self.centre["y"]-4*self.longueur/10),
            (self.centre["x"]+self.longueur/10,self.centre["y"]-7*self.longueur/10),
            (self.centre["x"]+self.longueur/4,self.centre["y"]-7*self.longueur/10)
        ]

    def tracer(self,canva):
        """
        tracer l'objet sur le cannevas

        canva est un canva deja existant.
        """
        points= self.points
        self.canva=canva
        id = canva.create_polygon(points,outline=self.couleur,width=3,state='disabled',fill=self.couleurFond)
        self.id=id
    
    def _maj(self):
        """
        mettre a jour les propriétés de l'objet sur le canva
        """
        self.canva.itemconfig(self.id,outline=self.couleur,fill = self.couleurFond)

    def editer_couleur(self,couleur):
        """
        modifier la couleur de l'objet

        couleur est une couleur au format '#RGB' ou '#RRGGBB' ou 'color' 
        """
        if self.figure == "etoile":
            self.couleur=couleur
        elif self.figure == "sapin":
            self.couleurFond = couleur
        self._maj()
    
    def editer_position(self,x,y):
        """
        modifier la position de l'objet

        x est la nouvelle absice du centre
        y est la nouvelle ordonné du centre
        """
        self.canva.move(self.id,x-self.centre["x"],self.centre["y"])
        self.centre["x"]=x
        self.centre["y"]=y

    def clignoter(self,fen,frequence,liste_couleur:list,_Recursivite=0):
        """
        faire clignoter l'objet

        fen est une fenetre tKinter
        frequence est la frequence de clignotement en ms
        liste_couleur est une liste de l'ensemble des couleurs dans l'ordre d'apparition
        """
        couleur = liste_couleur[_Recursivite%len(liste_couleur)]
        self.editer_couleur(couleur)
        def _appel():
            self.clignoter(fen,frequence,liste_couleur,_Recursivite=_Recursivite+1)
        fen.after(frequence,_appel)
