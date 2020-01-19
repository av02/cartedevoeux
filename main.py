#importation des formes et du module tkinter
import formes.etoile as et
import formes.Fond as fd
import tkinter
import time
import formes.formes as f
import texte.nom as nom

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


#definition du cadre de dessin de l'etoile
canva = tkinter.Canvas(fenetre_principale,height=350,width=350)
canva.pack()


#definition d'une étoile
premiere_etoile = f.formes(12,"#FFD700",80,80,"etoile")
#definition du fond
fond = fd.fond("#ff2700","#c6c318","#a1b9fb",canva)
fond.tracer_fond()
#dessin de l'étoile

fond.clignoter(fenetre_principale,120,[["#ff2700","#c6c318","#a1b9fb"],["pink","yellow","green"]])
premiere_etoile.tracer(canva)



etoile2 = f.formes(24,"#AA45AA",270,270,"etoile")

sapin1 = f.formes(150,"black",120,300,"sapin","green")
sapin1.tracer(canva)
etoile2.tracer(canva)

premiere_etoile.clignoter(fenetre_principale,200,["#AA00AA","#FFD700"])
etoile2.clignoter(fenetre_principale,200,["pink","yellow","green"])

text = canva.create_text(220,110,text = "bonne année "+prenom)



fenetre_principale.mainloop()
