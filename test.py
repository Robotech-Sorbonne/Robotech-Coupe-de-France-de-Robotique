import tkinter as tk
import random

with open("prenom.txt", "r") as file:
    prenoms = file.readlines()

class Personnage:
    def __init__(self, PV: int , nom : str , coord_x: int):
        self.__PV = PV
        self.__nom = nom 
        self.__coord_x = coord_x
        
          
    @property
    def PV(self):
        return self.__PV
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def coord_x(self):
        return self.__coord_x

    @PV.setter
    def PV(self, value: int):
        #if type(value) is not int:
         #  print(value) 
          # print("Non")
        #else:
         #   if value < 0:
          #      print("Mort")
            self.__PV = value
            
    @coord_x.setter
    def coord_x(self,value):
        if type(value) is not int:
            raise TypeError ("La valeur de coord_x doit être un entier.")
        else:
            self.__coord_x = value
            
            
    def allinfo(self):
        chaine = "Nom:"
        chaine += str(self.nom)
        chaine += "   Point de vie restant:"
        chaine += str(self.PV)
       
        return chaine
    
    #Méthode pour ajouter des personnages dans une liste
    #redondant avec la classe listePerso
    def AjouterPerso(perso, liste):
        if isinstance(perso, Personnage):
            liste.append(perso)
    
class Attaquant (Personnage):
    def __init__(self, PV: int, nom: str, coord_x: int, pt_attaque: int):
        super().__init__(PV, nom, coord_x)
        self.__pt_attaque = pt_attaque
        
    @property
    def pt_attaque(self):
        return self.__pt_attaque
    
    @pt_attaque.setter
    def pt_attaque(self, value: int):
        if type(value) is not int:
            print("La valeur entrée n'est pas un entier")
        else:
            self.__pt_attaque = value
            
    def attaquer(self, personnage):
        personnage.PV -= self.__pt_attaque
        
    def allinfo(self):
        chaine = "Nom:"
        chaine += str(self.nom)
        chaine += "   Point de vie restant:"
        chaine += str(self.PV)
        chaine += "  Point d'attaque"
        chaine += str(self.__pt_attaque)
        return chaine
        
class Soignant(Personnage):
    def __init__(self, PV: int, nom: str, coord_x: int, pt_soin: int):
        super().__init__(PV, nom, coord_x)
        self.__pt_soin = pt_soin

    @property
    def pt_soin(self):
        return self.__pt_soin

    @pt_soin.setter
    def pt_soin(self, value: int):
        if type(value) is not int:
            print("Donnée non valide")
        else:
            self.__pt_soin = value

    def soigner(self, personnage: Personnage):
        personnage.PV += self.__pt_soin

    def allinfo(self):
        chaine = "Nom:"
        chaine += str(self.nom)
        chaine += "    Point de vie restant:"
        chaine += str(self.PV)
        chaine += "   Point de soin:"
        chaine += str(self.pt_soin)
        return chaine    
    
class Guerrier(Attaquant): #1
    def __init__(self, PV: int, nom: str, coord_x: int, pt_attaque: int):
        super().__init__(PV, nom, coord_x,pt_attaque)

    def attaquer(self, personnage):
        personnage.PV -= self.pt_attaque

    def allinfo(self):
        chaine = super().allinfo()
      #  chaine += " --Point d'attaque: "
        return chaine
    
class Chevalier(Attaquant): #2
    def __init__(self, PV: int, nom: str, coord_x: int, pt_attaque: int):
        super().__init__(PV, nom, coord_x,pt_attaque)
        

    def attaquer(self, personnage):
        if (abs(personnage.coord_x -self.coord_x)<10):
             personnage.PV -= self.pt_attaque
        if (abs(personnage.coord_x -self.coord_x)>10):
            personnage.PV -= (self.pt_attaque) 
            # personnage.PV -= (self.pt_attaque)/2     
                          
class Archer(Attaquant): #3
    def __init__(self, PV: int, nom: str, coord_x: int, pt_attaque: int):
        super().__init__(PV, nom, coord_x, pt_attaque)
        

    def attaquer(self, personnage):
        if (abs(personnage.coord_x -self.coord_x)>10):
             personnage.PV -= self.pt_attaque
        if (abs(personnage.coord_x -self.coord_x)<10):
              personnage.PV -= ((self.pt_attaque))
            # personnage.PV -= (self.pt_attaque)/2
                 
class Soigneur(Soignant): #4
    def __init__(self, PV: int, nom: str, coord_x: int, pt_soin: int):
        super().__init__(PV, nom, coord_x, pt_soin)
        

    def Soigner(self, personnage):
        if (abs(personnage.coord_x -self.coord_x)>20):
             personnage.PV += self.pt_soin    
    
class Pretre(Soignant): #5
    def __init__(self, PV: int, nom: str, coord_x: int, pt_soin: int):
        super().__init__(PV, nom, coord_x, pt_soin)
        

    def Soigner(self, personnage):
        if (abs(personnage.coord_x -self.coord_x)<20):
             personnage.PV += self.pt_soin
    
class Paladin(Personnage): #6
    def __init__(self, PV: int, nom: str, coord_x: int, pt_attaque: int, pt_soin: int):
        super().__init__(PV, nom, coord_x)
        self.__pt_attaque = pt_attaque
        self.__pt_soin = pt_soin
       
    @property
    def pt_attaque(self):
        return self.__pt_attaque
    @property
    def pt_soin(self):
        return self.__pt_soin
        
    @pt_attaque.setter
    def pt_attaque(self, value: int):
        if type(value) is not int:
            print("La valeur entrée n'est pas un entier")
        else:
            self.__pt_attaque = value 
         
    @pt_soin.setter
    def pt_soin(self, value: int):
        if type(value) is not int:
            print("Donnée non valide")
        else:
            self.__pt_soin = value   
      
    def attaquer(self, personnage):
        personnage.PV -= self.__pt_attaque 

    def Soigner(self, personnage):
        personnage.PV += self.pt_soin 


    def allinfo(self):
        chaine = "Nom:" + str(self.nom)
        chaine += "   Point de vie restant:" + str(self.PV)
        chaine += "   Point d'attaque:" + str(self.pt_attaque)
        chaine += "   Point de soin:" + str(self.pt_soin)
        return chaine 
    
    
class ListePerso:
    def __init__(self, *Personnage):
        self.Personnage = list(Personnage)
        
    def ajouter(self, Personnage):
        self.Personnage.append(Personnage)
        
    def enlever(self, Personnage):
        self.Personnage.remove(Personnage)
    
    def generandom(self,nb_perso):
        
        for i in range(nb_perso):
            prenom_aleatoire = random.choice(prenoms).strip()
            PV_aleatoire = random.choice([100,110,120,130,140,150,160,170,180,190,200])
            #PV_aleatoire = random.randrange(100, 200,10)
            coord_x_aleatoire = random.randint(10, 10) # Normalement les personnages sont étalés sur un axe de 100
            
            classe = random.choice([3,3,3,3,3,3]) ## remettre 1,2,3,4,5,6
            
            coord_x_aleatoire = random.randint(0, 100)
            if (1 <= classe <= 3):
                pt_attaque_aleatoire = random.randrange(10, 50,5)
                if (classe==1):
                    self.ajouter(Guerrier(PV_aleatoire, prenom_aleatoire, coord_x_aleatoire, pt_attaque_aleatoire))
                elif (classe==2):
                    self.ajouter(Chevalier(PV_aleatoire, prenom_aleatoire, coord_x_aleatoire, pt_attaque_aleatoire))
                elif (classe==3):
                    self.ajouter(Archer(PV_aleatoire, prenom_aleatoire, coord_x_aleatoire, pt_attaque_aleatoire))    
            elif (4 <= classe <= 5):
                    pt_soin_aleatoire = random.randrange(10, 50,5)
                    if (classe==4):
                        self.ajouter(Soigneur(PV_aleatoire, prenom_aleatoire, coord_x_aleatoire, pt_soin_aleatoire))
                    elif (classe==5):
                        self.ajouter(Pretre(PV_aleatoire, prenom_aleatoire, coord_x_aleatoire, pt_soin_aleatoire)) 
            elif (classe==6):
                pt_attaque_aleatoire = random.randrange(10, 50,5)
                pt_soin_aleatoire = random.randrange(10, 50,5)    
                self.ajouter(Paladin(PV_aleatoire, prenom_aleatoire, coord_x_aleatoire, pt_attaque_aleatoire,pt_soin_aleatoire))        
               
    def AfficheListe(self):
        for perso in self.Personnage:
             print(perso.allinfo())
             
             
    def ClearListe(self):
        self.Personnage.clear() 
    
    def check_liste(self):
        if not self.Personnage:
            return False
        else:
            return True
             
class Jeu:
    def __init__(self, master):
        self.master = master
        self.master.title("Ma page")
        self.master.geometry("798x394")
        self.master.config(background='#030549')
        self.nb_perso = 20
        self.listeperso1 = ListePerso()
        self.listeperso2 = ListePerso()
        
        self.frame2 = tk.Frame(self.master, bg='#030549')

        self.messBienv = tk.Label(self.frame2, text="Bienvenue dans le Jeu", font=("Arial", 20), bg='#030549', fg='white')
        self.messBienv.pack()
        
        self.frame2.pack(fill=tk.X)
        
        self.messNbPerso = tk.Label(self.master, text="Veuillez choisir le nombre de personnage par joueur:", font=("Arial", 10), bg='#030549', fg='white')
        self.messNbPerso.pack(anchor=tk.NW, padx=10, pady=10)

        self.bouton_quitter = tk.Button(self.master, text="Quitter", fg="red", command=self.master.destroy)
        self.bouton_quitter.pack(side=tk.RIGHT, anchor=tk.SW, padx=10, pady=10)

        self.frame_J1 = tk.Frame(self.master, bg='#030549')
        self.frame_J1.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.NONE, padx=10, pady=10)

        self.text_widget1 = tk.Text(self.frame_J1)
        self.text_widget1.config(width=15, height=1)
        self.text_widget1.insert(tk.END, "Joueur 1")
        self.text_widget1.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=5)

        self.liste1 = tk.Listbox(self.frame_J1)
        self.liste1.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=5)

        self.frame_J2 = tk.Frame(self.master, bg='#030549')
        self.frame_J2.pack(side=tk.RIGHT, anchor=tk.NE, fill=tk.NONE, padx=10, pady=10)

        self.text_widget2 = tk.Text(self.frame_J2)
        self.text_widget2.config(width=15, height=1)
        self.text_widget2.insert(tk.END, "Joueur 2")
        self.text_widget2.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=5)

        self.liste2 = tk.Listbox(self.frame_J2)
        self.liste2.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=5)
    
        self.bouton_generer1 = tk.Button(self.frame_J1, text="Générer",command=self.commande_1)
        self.bouton_generer1.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=5)
        
        self.bouton_generer2 = tk.Button(self.frame_J2, text="Générer",command=self.commande_2)
        self.bouton_generer2.pack(side=tk.TOP, anchor=tk.NW, padx=60, pady=5)
         
        self. bouton_Valid = tk.Button(self.master, text="Valider\n vos \npersonnages",command=self.Erase_gener )  
        self.bouton_Valid.config(height=3,width=80)
        self.bouton_Valid.pack(anchor=tk.CENTER, padx=10, pady=90)
        
        self.liste1.bind('<<ListboxSelect>>', self.on_select1)
        self.liste2.bind('<<ListboxSelect>>', self.on_select2)
        
        self.bouton_Attaquer = tk.Button(master, text="Attaquer",command=self.command_attaquer)
        self.bouton_Attaquer.config(height=1, width=10)

        self.bouton_Soigner = tk.Button(master, text="Soigner",command=self.command_soigner)
        self.bouton_Soigner.config(height=1, width=10)
        
        self.messT ="C'est au Joueur N°1 de jouer"
        
        self.messTourJ1 = tk.Label(self.frame2, text=self.messT, font=("Arial", 10), bg='#030549', fg='white')

        self.messFin = tk.Label(self.master, text="La partie est terminée",font=("Arial", 15), bg='#030549', fg='white')
        
        chaine1 =""
        global P1
        
        chaine2 =""
        global P2
        
        self.label_chaine1 = tk.Label(self.frame_J1, text=chaine1, font=("Arial", 10), bg='#030549',fg='white', height=6, width=20, justify="left", wraplength=100)  # bg='#030549'
        self.label_chaine2 = tk.Label(self.frame_J2, text=chaine2, font=("Arial", 10), bg='#030549',fg='white', height=6, width=20, justify="left", wraplength=100)  # bg='#030549'
    
    
    def jouer(self):
        self.master.mainloop()
        
    def clear_listbox(self,listbox):
        listbox.delete(0, self.nb_perso)    
        
    def insertbox1(self):
        for item in self.listeperso1.Personnage:
            self.liste1.insert(tk.END, item.nom) 
            
    def insertbox2(self):
        for item in self.listeperso2.Personnage:
            self.liste2.insert(tk.END, item.nom)         
            
    def commande_1(self):
         self.clear_listbox(self.liste1)
         self.listeperso1.ClearListe()
         self.listeperso1.generandom(self.nb_perso)   
         self.insertbox1()
         
    def commande_2(self):
         self.clear_listbox(self.liste2)
         self.listeperso2.ClearListe()
         self.listeperso2.generandom(self.nb_perso)   
         self.insertbox2() 
         
         
         
    def Erase_gener(self):
        try:
            if not (self.listeperso1.check_liste() and self.listeperso2.check_liste()):
                raise Exception("Générer les personnages avant de valider votre choix.")
        
            self.bouton_generer1.pack_forget()
            self.bouton_generer2.pack_forget()
            self.bouton_Valid.pack_forget()
            self.messNbPerso.pack_forget()
            self.label_chaine1.pack(side=tk.TOP, anchor=tk.NW, padx=30, pady=5)
            self.label_chaine2.pack(side=tk.TOP, anchor=tk.NW, padx=30, pady=5)
            self.bouton_Attaquer.pack(side=tk.LEFT,padx=5)#, padx=10, pady=50)
            self.bouton_Soigner.pack(side=tk.LEFT,padx=5)#, padx=10, pady=50)
            self.messTourJ1.pack(side=tk.LEFT,padx=250)
            
        except Exception as e:
            tk.messagebox.showinfo("Information", str(e))     
    
    global indice1        
    global P1
    def on_select1(self,event):
        global P1
        global indice1
        widget = event.widget
      #  print(widget==liste1)#reconnait quel liste a été utilisé
        selection = widget.curselection()
        if selection:
            global P1
            global indice1
            index = selection[0]
            self.indice1=index
            self.P1 = self.listeperso1.Personnage[index]
            self.chaine1 = self.P1.allinfo()
            self.label_chaine1.config(text=self.chaine1)
            
    global indice2
    def on_select2(self,event):
          global P2
          global indice2
          widget = event.widget
          selection = widget.curselection()
          if selection:
              global P2
              global indice2
              index = selection[0]
              self.indice2=index
              self.chaine2 = self.listeperso2.Personnage[index].allinfo()
              self.P2 = self.listeperso2.Personnage[index]
              self.label_chaine2.config(text=self.chaine2)
           #   print(hasattr(self.P2,"pt_attaque"))

          #    hasattr(obj, 'mon_attribut'):

    
    def command_attaquer(self):
        self.ActionAttaque()
        self.change_message()
          
    
    def change_message(self):
        if self.messT == "C'est au Joueur N°1 de jouer":
            self.messT = "C'est au Joueur N°2 de jouer"
        else:
            self.messT = "C'est au Joueur N°1 de jouer"
        self.messTourJ1.config(text=self.messT)
        
    def ActionAttaque(self): 
        if self.messT == "C'est au Joueur N°1 de jouer":
            try:
                if not (hasattr(self.P1,"pt_attaque")):
                    raise Exception("L adversaire ne pas attaquer .")
                #    self.change_message()
                #    return
                self.listeperso1.Personnage[self.indice1].attaquer(self.listeperso2.Personnage[self.indice2])
                print("attaqué:" + str(self.listeperso2.Personnage[self.indice2].PV)) #DEBUG
                print("attaquant:" + str(self.listeperso1.Personnage[self.indice1].PV)) #DEBUG
                self.chaine2=self.listeperso2.Personnage[self.indice2].allinfo()
                self.label_chaine2.config(text=self.chaine2)
                if (self.listeperso2.Personnage[self.indice2].PV<1):
                    self.listeperso2.enlever(self.listeperso2.Personnage[self.indice2])
                    self.indice2 = 0##pour pas avoir erreur indexlist
                    self.label_chaine2.pack_forget()
                    #print (len(self.listeperso2.Personnage))
                    if len(self.listeperso2.Personnage) == 0 :                       
                        self.EndGame()
                        return
                   # self.listeperso2.AfficheListe()
                    self.clear_listbox(self.liste2)
                    self.insertbox2()
                    self.chaine2=self.listeperso2.Personnage[0].allinfo()
                    self.label_chaine2.config(text=self.chaine2)
                    self.label_chaine2.pack(side=tk.TOP, anchor=tk.NW, padx=30, pady=5)
            except Exception as e:
                   tk.messagebox.showinfo("Erreur1", str(e))
                   return
        else:  
            try:
                if not (hasattr(self.P2,"pt_attaque")):
                   
                   raise Exception("Ce personnage n'a pas la capacité d'attaquer.")
                   #self.change_message()
                   #return 
                self.listeperso2.Personnage[self.indice2].attaquer(self.listeperso1.Personnage[self.indice1])
                print("attaqué:" + str(self.listeperso2.Personnage[self.indice2].PV())) ##For DEBUG
                print("attaquant:" + str(self.listeperso1.Personnage[self.indice1].PV)) #For DEBUG
                self.chaine1=self.listeperso1.Personnage[self.indice1].allinfo()
                self.label_chaine1.config(text=self.chaine1)
                if (self.listeperso1.Personnage[self.indice1].PV<1):
                    self.listeperso1.enlever(self.listeperso1.Personnage[self.indice1])
                    self.indice1 = 0##pour pas avoir erreur indexlist
                    self.label_chaine1.pack_forget()
                  #  print (len(self.listeperso1.Personnage))
                    if len(self.listeperso1.Personnage) == 0 :                       
                        self.EndGame()
                        return
                  #  self.listeperso1.AfficheListe()
                    self.clear_listbox(self.liste1)
                    self.insertbox1()
                    self.chaine1=self.listeperso1.Personnage[0].allinfo()
                    self.label_chaine1.config(text=self.chaine1)
                    self.label_chaine1.pack(side=tk.TOP, anchor=tk.NW, padx=30, pady=5)
            except Exception as e:
                    print("Le probleme est là ")
                   # print(hasattr(self.P2,"pt_attaque"))
                    tk.messagebox.showinfo("Erreur2", str(e))
                    return
    
   
    def command_soigner(self): #liste
        if self.messT == "C'est au Joueur N°1 de jouer":
            try:
                if not (hasattr(self.P1,"pt_soin")):
                    raise Exception("Ce personnage n'a pas la capacité d'attaquer.")
                    return
                self.PageDeSoin()                
                #self.change_message()
            except Exception as e:
                    tk.messagebox.showinfo("Erreur3", str(e))
        elif self.messT == "C'est au Joueur N°2 de jouer":
           try:
               if not (hasattr(self.P2,"pt_soin")):
                   raise Exception("Ce personnage n'a pas la capacité d'attaquer.")
                   return
               self.PageDeSoin()                
               #self.change_message()
           except Exception as e:
                   tk.messagebox.showinfo("Erreur4", str(e))             

    
    def PageDeSoin(self): #liste1
       self.Page2 = tk.Toplevel(self.master)
       self.listBoxSoin = tk.Listbox(self.Page2)
       self.listBoxSoin.pack()
       if self.messT == "C'est au Joueur N°1 de jouer":
           for item in self.listeperso1.Personnage:
               self.listBoxSoin.insert(tk.END, item.nom)
       else :
           for item in self.listeperso2.Personnage:
               self.listBoxSoin.insert(tk.END, item.nom)
       self.listBoxSoin.bind("<<ListboxSelect>>", self.on_select3)
  
       
    def on_select3(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            if self.messT == "C'est au Joueur N°1 de jouer":
                print("J1")
                self.listeperso1.Personnage[self.indice1].soigner(self.listeperso1.Personnage[index])
                print(self.listeperso1.Personnage[index].allinfo())
                self.Page2.destroy()
                self.change_message()
                if index == self.indice1 :
                    print("boom1")
                    self.chaine1=self.listeperso1.Personnage[self.indice1].allinfo()
                    self.label_chaine1.config(text=self.chaine1)
            elif self.messT == "C'est au Joueur N°2 de jouer":
                print("J2")
                self.listeperso2.Personnage[self.indice2].soigner(self.listeperso2.Personnage[index])
                print(self.listeperso2.Personnage[index].allinfo())
                self.Page2.destroy()
                self.change_message()
                if index == self.indice2 :
                    print("boom2")
                    self.chaine2=self.listeperso2.Personnage[self.indice2].allinfo()
                    self.label_chaine2.config(text=self.chaine2)
            else :
                print("Ya un problème")                
   
    def EndGame(self):
        self.frame2.pack_forget()
        self.bouton_Attaquer.pack_forget()
        self.bouton_Soigner.pack_forget()
        self.label_chaine1.pack_forget()
        self.label_chaine2.pack_forget()
        self.liste1.pack_forget()
        self.liste2.pack_forget()
        self.text_widget1.pack_forget()
        self.text_widget2.pack_forget()
        self.messFin.config(height=50,width=50)
        self.messFin.pack(anchor=tk.CENTER)
        
        


if __name__ == '__main__':
    root = tk.Tk()
    jeu = Jeu(root)
    jeu.jouer()
   

    
    
    