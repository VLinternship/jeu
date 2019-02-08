import sys
import random
import salles


def partie1():
    premierchoix=(int(input ("choisis une porte 1 ou 2:")))

    # Pas dedans 
    if premierchoix not in [1,2]:
        print("Vous êtes tombés dans un trou, VOUS ETES MORT")
        sys.exit()

    if premierchoix == 1:
        print("Vous etes dans la salle des coffres vous avez fait le bon choix!")
    else:
        print("Vous etes dans la salle 2 avec les monstres,vous êtes morts")
        sys.exit()
    

triche = input("Veux tu activer le mode triche oui ou non: ")

if triche == "non":
        print("hello")
        partie1()

recompenses = ["de l or","des bijoux", " mille serpents", " une épée"]
sacADos = []
#### ajoute a 'sacados' le fromage les frites

print("I"+str(sacADos))
salles.salle1(sacADos)
lampetorche="une lampetorche"
epee= " une épée"
print("On continue")
deuxiemechoix=(int(input("choisis le bon coffre 1 ou 2: ")))
r = random.randint(1, 2)
print("Le nombre aleatoire est " + str(r))
if deuxiemechoix == r:
	print ("vous a gagné le tresor")
else:
	print("vous avez perdu")
	sys.exit()

r2 = random.choice(recompenses)
print("Dans le coffre il y a " + str(r2))


if r2==" mille serpents":
        print ("Vous êtes morts")
        sys.exit()


if r2== "de l or":
    acheterepeeavcor=(input("Vous etes riche vous pouvez achetez une épée le faite vous oui ou non: "))
    if acheterepeeavcor=="oui":
        print("Bravo,vous avez acheter un épée")
        sacADos.append(epee)
    elif acheterepeeavcor=="non":
        print("Vous n'avez pas acheter l'épée")        
        sacADos.append(r2)
elif r2== "des bijoux":
    acheterepeeavcbijoux=(input("Vous êtes riche voulez vous acheter une épée oui ou non:"))
    if acheterepeeavcbijoux=="oui":
        print("Vous avez acheter une épée")
        sacADos.append(epee)
    elif acheterepeeavcbijoux=="":
        print("Vous n'avez pas acheter l'épée")
elif r2== " une épée":
    print("Bravo,vous avez choisis le bon coffre")       
    sacADos.append(r2)
else:
    sacADos.append(r2)
    

print("Le sac a dos contient " + str(sacADos))

premiercombat=(input("Un troll fonce sur vous que faites courez ou combattez?"))
if premiercombat=="courez":
    print("Vous courez vous refugiez derrière une porte")
    print("Vous courez sans regarder et vous tombez dans un trou")
    sys.exit()
if premiercombat=="combattez":
    premiercombattroll=(input("Il s'approche de plus en plus et il est de plus en plus grand.Voulez-vous vraiment le combattre?"))
    if premiercombattroll=="non":
            print("Vous courez vous refugiez derrière une porte")
            print("Vous courez sans regarder ou vous allez et vous tombez dans un trou")
            sys.exit()
    if premiercombattroll=="oui":
            print("le troll court et te frappe violament")
            if epee not in sacADos:
                print("Vous n'avez pas d'épée le troll vous a percuté vous n'avez pas pu vous defendre")
                print("Vous êtes morts!")
                sys.exit()
            if epee not in sacADos:
                print("Vous n'avez pas d'épée le troll vous a percuté vous n'avez pas pu vous defendre")
                print("Vous êtes morts")
                sys.exit()
            if epee in sacADos:
                print("Le troll vous as percuté mais grâce a votre épée vous avez pus vous defendre")
                print("Vous avez battu le troll vous continuez votre chemin")

carteoulampetorche=(input("A terre vous voyez deux objet une lampe-torche et une carte vous n'avez presque plus de place dans votre sac vous ne pouvez prendre qu'un objet alors carte ou lampe-torche"))
if carteoulampetorche=="carte":
    coffreousortie=(input("Sur cette carte vous voyez deux un chemin qui emmene vers un coffre et un qui emmene vers la sortie,alors tu veux sortir ou aller chercher le coffre(sortir ou coffre)"))
    if coffreousortie=="coffre":
            mangerun=(input("Vous avez choisi d'aller chercher le coffre mais vous ne voyez rien souhaitez vous manger quelque chose pour liberer de la place dans votre sac pour prendre la lampe-torche. Voulez-vous manger quelque chose?"))
            if mangerun=="oui":
                mangerdeux=(input("Qu'est ce que vous voulez manger fromages ou frites"))
                if mangerdeux=="fromages":
                    print("Vous avez manger le fromage")
                    print("Apres avoir manger le fromage vous vous senté pas bien le fromage etait pourri")
                    print("Vous êtes morts")
                    sys.exit()
                if mangerdeux=="frites":
                    print("Vous avez manger les frites")
                    print("Tres bon choix les frites vous ont donné de l'energie,")
                    prendrelalampetorche=(input("Maintenant que vous avez de la place voys prenez la lampe-torche (oui ou non ) "))
                    if prendrelalampetorche=="oui":
                        sacADos.append(lampetorche)
                    if prendrelalampetorche=="non":
                        print("Vous avez choisi de ne pas prendre la lampe-torche vous continuez votre chemin mais vous vous êtes perdu et vous êtes morts")
                        sys.exit()
                    print("Avec ta carte et ta lampe-torche tu te dirige vers le coffre pour avoir ton tresor et repartir tranquille")
                    choixsalledescoffres=(input("la salle des coffre est devant toi tu rentre ou pas(oui ou non)"))
                    if choixsalledescoffres=="non":
                        print("Vous êtes morts de peur a vous demander si vous allez mourir dans cette salle ")
                        sys.exit()
                    if choixsalledescoffres=="oui":
                        print("Vous arrivé dans la salle des coffres il ya 5 coffres devant vous choisisez lequelle")
                        dernierchoix=(int(input("1,2,3,4,5")))
                        if dernierchoix==1:
                            print("Bravo vous avez gagnez le tresor vous avait fini une des fin il y'en a plein d'autre recommencer et faite d'autre choix pour arriver a d'autre fin ")
                        if dernierchoix==2:
                            print("Mauvais coffre perdu")
                            sys.exit()
                        if dernierchoix==3:
                            print("Mauvais coffre perdu")
                            sys.exit()
                        if dernierchoix==4:
                            print("Mauvais coffre perdu")
                            sys.exit()
                        if dernierchoix==5:
                            print("Mauvais coffre perdu")
                            sys.exit()

            if mangerun=="non":
                print("vous avez decide de ne pas prendre la lampe-torche vous continuez votre route lorsque vous êtes perdu dans le noir")
                print("Vous êtes morts")
                sys.exit()
    if coffreousortie=="sortir":
        mangersortie=(input("Vous avez choisi de sortir vous ne voyez rien voulez manger quelque chose pour liberer de la place et pouvoir prendre la lampe-torche"))
        if mangersortie=="non":
            print("Vous continuez votre chemin vers la sortie dans le noir vous avez peur et vous avez faim vous mourrez de faim de peur et de fatigue")
            sys.exit()
        if mangersortie=="oui":
            mangersortiefritesoufromages=(input("Que voulez vous manger fromages ou frites?"))
            if mangersortiefritesoufromages=="fromages":
                 print("Vous avez manger le fromage")
                 print("Apres avoir manger le fromage vous vous senté pas bien le fromage etait pourri")
                 print("Vous êtes morts")
                 sys.exit()
            if mangersortiefritesoufromages=="frites":
                 print("Vous avez manger les frites")
                 print("Tres bon choix les frites vous ont donné de l'energie,")
                 prendrelalampetorche=(input("Maintenant que vous avez de la place voulez vous  prendre la lampe-torche (oui ou non ) "))
                 if prendrelalampetorche=="oui":
                     sacADos.append(lampetorche)
                 if prendrelalampetorche=="non":
                     print("Vous avez choisi de ne pas prendre la lampe-torche vous continuez votre chemin mais vous vous êtes perdu et vous êtes morts ")
                     sys.exit()
                 print("grâce a votre carte vous trouvez la sortie vous avait fini la premiere fin il y'en a plein d'autre recommencer et faite d'autre choix pour arriver a d'autre fin ")
                 sys.exit()
if carteoulampetorche=="lampetorche":
    print ("Qu'est ce que vous allez faire avec une lampe-torche sans carte pendent des jours et des jours vous chercher la sortie et un jour la lampe-torche s'éteint et vous mourez par la suite.") 
    sys.exit()       