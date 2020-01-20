import tkinter
import random
class flocons:
    """
    canva : un canva tkinter
    permet de generer un flocon aleatoire
    """
    def __init__(self,canva):
        self.canva = canva
        self.largeur=random.randint(1,5)
        self.x = random.randint(0,canva.x)
        self.y = 0
        self.id = self._flocon(self.x,self.y,self.largeur)

   
    def _flocon(self, posx,posy,largeur):
        id = self.canva.create_oval(posx,posy,posx+largeur,posy+largeur,width=0,fill="#FFFAFA")
        return id

    def deplacer(self):
        y = random.randint(0,5)
        self.y+=y
        x = random.randint(-1,1)
        self.x = x
        self.canva.move(self.id,x,y)



tous_flocons = []

def surcouche_neige(canva):
    """
    canva :  le canva où ajouter la surcouche
    
    permet de faire neiger sur le canva.
    """
    for i in range(0,6):
        tous_flocons.append(flocons(canva))
    for flocon in tous_flocons:
        if flocon.y > canva.y:
            del flocon

        else:
            flocon.deplacer()
            pass
    canva.after(10,mouvement, canva)


