from flask import Flask
from flask_ask import Ask, statement, question
import random

app = Flask(__name__)
ask = Ask(app, '/')


qenfant = [("Blanche neige a mangé une poire empoisonnée",False,"C'était une pomme"),
          ("Dans la reine des neiges la soeur d'Anna s'appelle Elsa",True,""),
          ("Il y a 100 dalmatiens",False,"Il y en a 101"),
          ("L'animal d'aladin est un chat",False,"C'est un chimpanzé"),
          ("Le passe-temps de Belle dans la belle et la bête est de regarder des films",False,"Elle aime lire des livres"),
          ("Le nom original de Stitch dans Lilo et Stitch est expérience 626",True,""),
          ("Les cheveux de Raiponce sont capable de guérir toutes blessures",True,""),
          ("Mulan est d'origine japonaise",False,"elle est chinoise"),
          ("Dans Peter Pan pour se rendre au Pays Imaginaire il faut courir!",False,"Il faut voler"),
          ("Le caméléon de de Raiponse s'appelle Pascal",True,"")]

qcomplexe = [("La Première Croisade a commencé en 1096.", True, ""),
            ("Le bombardement de Pearl Harbor a été effectué le 7 décembre 1940.", False, "C'était le 7 décembre 1941"),
            ("Une tête humaine a en moyenne 110 000 follicules pileux.", True, ""),
            ("Un bébé a moins d'os qu'un adulte.", False,
             "C'est faux, c'est même le contraire, il en a plus et plusieurs os se souderont ensemble durant la croissance."),
            ("Cléopâtre VII était égyptienne d'origine.", False, "C'est faux, elle était d'origine grecque."),
            ("Un café décaféiné ne contient pas de caféine.", False, "C'est faux, il en contient mais beaucoup moins."),
            ("Les Fidji sont un archipel de plus de 300 îles situé en Océanie.", True, ""),
            ("Un kangourou roux peut parcourir 9 mètres en un bond.", True, ""),
            ("Un koala boit jusqu'à 4 litres d'eau par jour.", False,
             "C'est faux, il ne boit pas, le liquide provenant des feuilles d'eucalyptus lui suffit."),
            ("Le Japon est un archipel constitué de 6 852 îles.", True, "")]

qsimple = [("La capital de la France est Paris",True,""),
           ("Cristaline met en avant des bébés dans ses pubs",False,"C'est Evian qui le fait"),
           ("Booba et la Fouine prévoit de faire un octogone sans règle",False,"C'est Booba et Kaaris qui veulent le faire"),
           ("La couleur de Twitter est le vert",False,"C'est le bleu"),
           ("Asus fait des téléphones portables",True,""),
           ("Les ingénieurs sont en faculté des sciences",False,"Ils sont à l'EPL"),
           ("Belfius s'appelait auparavent Dexia",True,""),
           ("Le siège de l'Europe se trouve à Bruxelles",True,""),
           ("Charles Michel est le premier ministre belge",True,""),
           ("L'UCL s'est recemment renommé UCLouvain",True,"")]

now1 = None
now2 = None
point = 0

@ask.launch
def start():
    global point
    point = 0
    return question("Voulez-vous jouez ?")


@ask.intent('VraiFaux')
def vraifaux():
    return question("Quel mode de difficulté voulez vous jouer ? (enfant, simple ou complexe)")

@ask.intent('Complexe')
def complexe():
    global now1
    global now2
    now1 = qcomplexe
    now2 = random.randint(0,9)
    return question("Vrai ou faux : {}".format(qcomplexe[now2][0]))


@ask.intent('Enfant')
def enfant():
    global now1
    global now2
    now1 = qenfant
    now2 = random.randint(0, 9)
    return question("Vrai ou faux : {}".format(qenfant[now2][0]))

@ask.intent('Simple')
def simple():
    global now1
    global now2
    now1 = qsimple
    now2 = random.randint(0, 9)
    return question("Vrai ou faux : {}".format(qsimple[now2][0]))

@ask.intent('Vrai')
def repvrai() :
    global now1
    global now2
    global point
    if now1[now2][1] == True :
        point += 1
        return question("Bonne réponse. Dites continuer pour continuer ou stop pour arreter de jouer")
    else :
        return question("Mauvaise réponse : {}. Dites continuer pour continuer ou stop pour arreter de jouer".format(now1[now2][2]))

@ask.intent('Faux')
def repvrai() :
    global now1
    global now2
    global point
    if now1[now2][1] == False :
        point += 1
        return question("Bonne réponse : {}. Dites continuer pour continuer ou stop pour arreter de jouer".format(now1[now2][2]))
    else :
        return question("Mauvaise réponse. Dites continuer pour continuer ou stop pour arreter de jouer")

@ask.intent('Continuer')
def conti():
    if now1 == qenfant :
        return enfant()
    elif now1 == qsimple :
        return simple()
    elif now1 == qcomplexe :
        return complexe()

@ask.intent('NonIntent')
def non() :
    global point
    if point == 0 :
        return statement("Tant pis, 0 point.")
    elif point == 1 :
        return statement("Merci d'avoir jouer, vous finissez avec {} point.".format(point))
    else :
        return statement("Merci d'avoir jouer, vous finissez avec {} points.".format(point))


if __name__ == '__main__':
    app.run()