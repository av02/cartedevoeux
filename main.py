"""
un exemple simple avec toutes les fonctions disponible

"""
#importation des formes et du module tkinter
import formes.etoile as et
import formes.Fond as fd
import tkinter
import time
import formes.formes as f
import texte.nom as nom
import formes.flocon as flo

#une premiere fenetre pour demander le prenom
#TODO: ajouter un fond d'ecran
fenetre_start = tkinter.Tk()
fenetre_start.title("bonne année")
fenetre_start.geometry("350x350+700+300")
fenetre_start.configure(bg="#777777")

a = nom.ecran_base(fenetre_start)
fenetre_start.wait_window()
prenom =a.get_nom()


#creation d'une fenetre
fenetre_principale = tkinter.Tk()
fenetre_principale.title("bonne année")
fenetre_principale.geometry("350x350+700+300")
fenetre_principale.configure(bg="#777777")


#definition du cadre de dessin 
canva = tkinter.Canvas(fenetre_principale,height=350,width=350,bd=0)
canva.pack()


#definition du fond
fond = fd.fond("#ff2700","#c6c318","#a1b9fb")
fond.tracer_fond(canva)#dessiner le fond
fond.clignoter(fenetre_principale,120,[["#ff2700","#c6c318","#a1b9fb"],["pink","yellow","green"]])#faire clignoter


#definition d'une étoile puis tracé puis clignoter d'une etoile
premiere_etoile = f.formes(12,"#FFD700",80,80,"etoile")
premiere_etoile.tracer(canva)
premiere_etoile.clignoter(fenetre_principale,200,["#AA00AA","#FFD700"])


#une deuxieme etoile
etoile2 = f.formes(24,"#AA45AA",270,270,"etoile")
etoile2.tracer(canva)
etoile2.clignoter(fenetre_principale,200,["pink","yellow","green"])

#un sapin
sapin1 = f.formes(150,"black",120,300,"sapin","green")
sapin1.tracer(canva)

#le texte
text = canva.create_text(220,110,text = "bonne année "+prenom,font=('Savoye LET',40))

#faire neiger
flo.surcouche_neige(canva)

fenetre_principale.mainloop()
