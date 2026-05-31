import PIL
from PIL import ImageDraw, ImageFont
import os
import configparser


VERSION = "1.1.0"
print(f"ScriptPR.py version {VERSION}")


config = configparser.ConfigParser()
config.read('../config.txt')
pr_path = config["general"]["pr_path"]

#Données (Ce qu'il y a à modifier):

Chemin = f'{pr_path}/images'
os.chdir(Chemin)

LayoutPR =  f"{pr_path}/résultats/layoutPR.png"

#Polices

Mustica = 'MusticaPro-SemiBold 600.otf'
Comfortaa = 'Comfortaa-Regular.ttf'
njnaruto = 'njnaruto.ttf'

#Utile

def average(R):
    L_Average = []
    for i in range(len(R)):
        Somme = 0
        for j in range(len(R[i])):
            Somme += R[i][j]
        L_Average.append(Somme/len(R[i]))
    return L_Average

#Programme

def entreescoressolo(L,C,E,x1,CL,DL,k,Rang,Total,Titre,Musique, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Mustica, size=60) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    m=min(L)
    M=max(L)
    Inc=0
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((378,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
        
    W1,H1=(1920,20)
    H1b=30
    H1c=40
    
    if len(Titre)<=33:
        w1 = draw.textlength(Titre,font=font3)
        draw.text(((W1-w1)/2,H1), Titre, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Titre)<=69:
        w1 = draw.textlength(Titre,font=font4)
        draw.text(((W1-w1)/2,H1b), Titre, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w1 = draw.textlength(Titre,font=font5)
        draw.text(((W1-w1)/2,H1c), Titre, fill = 'rgb(255, 255, 255)', font=font5)


    W2,H2=(1920,1000)
    H2b=1010
    H2c=1020
    if len(Musique)<=33:
        w2 = draw.textlength(Musique,font=font3)
        draw.text(((W2-w2)/2,H2), Musique, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Musique)<=69:
        w2 = draw.textlength(Musique,font=font4)
        draw.text(((W2-w2)/2,H2b), Musique, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w2  = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)


    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()


def entreescores8(L,C,E,x1,CL,DL,k,Rang,Total,Titre,Musique, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Mustica, size=60) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    m=min(L)
    M=max(L)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if type(L[Inc+j]) == int:
                if L[Inc+j] == m:
                    draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
            else:
                if L[Inc+j] == m:
                    draw.text((Y+10,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Y+10,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Y+10,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((378,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2) 
    draw.text((1427,850), str(round(Total,2)),fill = 'rgb(255, 255, 255)', font=font2)


    W1,H1=(1920,20)
    H1b=30
    H1c=40
    
    if len(Titre)<=33:
        w1 = draw.textlength(Titre,font=font3)
        draw.text(((W1-w1)/2,H1), Titre, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Titre)<=69:
        w1 = draw.textlength(Titre,font=font4)
        draw.text(((W1-w1)/2,H1b), Titre, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w1 = draw.textlength(Titre,font=font5)
        draw.text(((W1-w1)/2,H1c), Titre, fill = 'rgb(255, 255, 255)', font=font5)


    W2,H2=(1920,1000)
    H2b=1010
    H2c=1020
    if len(Musique)<=33:
        w2 = draw.textlength(Musique,font=font3)
        draw.text(((W2-w2)/2,H2), Musique, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Musique)<=69:
        w2 = draw.textlength(Musique,font=font4)
        draw.text(((W2-w2)/2,H2b), Musique, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w2  = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)


    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()
def entreescores14(L,C,E,x1,CL,DL,k,Rang,Total,Titre,Musique, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Mustica, size=60) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    m=min(L)
    M=max(L)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if L[Inc+j]<10:
                if L[Inc+j] == m:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
            else:
                if L[Inc+j] == m:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((378,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    draw.text((1427,850), str(round(Total,2)),fill = 'rgb(255, 255, 255)', font=font2)

    W1,H1=(1920,20)
    H1b=30
    H1c=40
    
    if len(Titre)<=33:
        w1 = draw.textlength(Titre,font=font3)
        draw.text(((W1-w1)/2,H1), Titre, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Titre)<=69:
        w1 = draw.textlength(Titre,font=font4)
        draw.text(((W1-w1)/2,H1b), Titre, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w1 = draw.textlength(Titre,font=font5)
        draw.text(((W1-w1)/2,H1c), Titre, fill = 'rgb(255, 255, 255)', font=font5)

    W2,H2=(1920,1000)
    H2b=1010
    H2c=1020
    if len(Musique)<=33:
        w2 = draw.textlength(Musique,font=font3)
        draw.text(((W2-w2)/2,H2), Musique, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Musique)<=69:
        w2 = draw.textlength(Musique,font=font4)
        draw.text(((W2-w2)/2,H2b), Musique, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w2  = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)
    
    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()

def entreescores18(L,C,E,x1,CL,DL,k,Rang,Total,Titre,Musique, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Mustica, size=60) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    m=min(L)
    M=max(L)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if L[Inc+j]<10:
                if L[Inc+j] == m:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
            else:
                if L[Inc+j] == m:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((378,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2) 
    draw.text((1427,850), str(round(Total,2)),fill = 'rgb(255, 255, 255)', font=font2)
        
    W1,H1=(1920,20)
    H1b=30
    H1c=40
    
    if len(Titre)<=33:
        w1 = draw.textlength(Titre,font=font3)
        draw.text(((W1-w1)/2,H1), Titre, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Titre)<=69:
        w1 = draw.textlength(Titre,font=font4)
        draw.text(((W1-w1)/2,H1b), Titre, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w1 = draw.textlength(Titre,font=font5)
        draw.text(((W1-w1)/2,H1c), Titre, fill = 'rgb(255, 255, 255)', font=font5)

    W2,H2=(1920,1000)
    H2b=1010
    H2c=1020
    if len(Musique)<=33:
        w2 = draw.textlength(Musique,font=font3)
        draw.text(((W2-w2)/2,H2), Musique, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Musique)<=69:
        w2 = draw.textlength(Musique,font=font4)
        draw.text(((W2-w2)/2,H2b), Musique, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w2  = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)

    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()


def entreescores36(L,C,E,x1,CL,DL,k,Rang,Total,Titre,Musique, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(njnaruto, size=25) #'MusticaPro-SemiBold 600.otf', size=70 ou 'njnaruto.ttf', size=50
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45) #52 segoes
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    m=min(L)
    M=max(L)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if L[Inc+j]<10:
                if L[Inc+j] == m:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
            else:
                if L[Inc+j] == m:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((372,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)

    draw.text((1427,850), str(round(Total,2)),fill = 'rgb(255, 255, 255)', font=font2)


    W1,H1=(1920,20)
    H1b=30
    H1c=40
    
    if len(Titre)<=33:
        w1, h1 = draw.textsize(Titre,font=font3)
        draw.text(((W1-w1)/2,H1), Titre, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Titre)<=69:
        w1, h1 = draw.textsize(Titre,font=font4)
        draw.text(((W1-w1)/2,H1b), Titre, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w1, h1 = draw.textsize(Titre,font=font5)
        draw.text(((W1-w1)/2,H1c), Titre, fill = 'rgb(255, 255, 255)', font=font5)


    W2,H2=(1920,1000)
    H2b=1010
    H2c=1020
    if len(Musique)<=33:
        w2, h2 = draw.textsize(Musique,font=font3)
        draw.text(((W2-w2)/2,H2), Musique, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Musique)<=69:
        w2, h2 = draw.textsize(Musique,font=font4)
        draw.text(((W2-w2)/2,H2b), Musique, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w2, h2 = draw.textsize(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)


    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()


def entreescores54(L,C,E,x1,CL,DL,k,Rang,Total,Titre,Musique, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(njnaruto, size=28) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    m=min(L)
    M=max(L)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if L[Inc+j]<10:
                if L[Inc+j] == m:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
            else:
                if L[Inc+j] == m:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                elif L[Inc+j] == M:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                else:
                    draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((550,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((522,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    draw.text((1427,850), str(round(Total,2)),fill = 'rgb(255, 255, 255)', font=font2)

    W1,H1=(1920,10)
    H1b=20
    H1c=30
    
    if len(Titre)<=33:
        w1 = draw.textlength(Titre,font=font3)
        draw.text(((W1-w1)/2,H1), Titre, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Titre)<=69:
        w1 = draw.textlength(Titre,font=font4)
        draw.text(((W1-w1)/2,H1b), Titre, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w1 = draw.textlength(Titre,font=font5)
        draw.text(((W1-w1)/2,H1c), Titre, fill = 'rgb(255, 255, 255)', font=font5)


    W2,H2=(1920,1015)
    H2b=1025
    H2c=1035
    if len(Musique)<=33:
        w2 = draw.textlength(Musique,font=font3)
        draw.text(((W2-w2)/2,H2), Musique, fill = 'rgb(255, 255, 255)', font=font3)
    elif len(Musique)<=69:
        w2 = draw.textlength(Musique,font=font4)
        draw.text(((W2-w2)/2,H2b), Musique, fill = 'rgb(255, 255, 255)', font=font4)
    else:
        w2  = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)

    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()

#Fonctions Création Images

def creationimagessolo(R,C,Rang,Total,Titre,Musique,output_path):
    E=240 
    x1=130 
    y1=170
    z1=380
    y2=1825
    z2=2045
    CL=[y1,y2]
    DL=[z1,z2]
    r=len(R)
    Av = average(R)
    for k in range(r):
        entreescoressolo(R[k],C,E,x1,CL,DL,k+1,Rang[k],Av[k],Titre[k],Musique[k], output_path)
    return()

def creationimages8(R,C,Rang,Total,Titre,Musique,output_path):
    E=240 
    x1=130 
    y1=163
    z1=380
    y2=1818
    z2=2045
    CL=[y1,y2]
    DL=[z1,z2]
    r=len(R)
    Av = average(R)

    for k in range(r):
        entreescores8(R[k],C,E,x1,CL,DL,k+1,Rang[k],Av[k],Titre[k],Musique[k], output_path)
    return()

def creationimages14(R,C,Rang,Total,Titre,Musique,output_path):
    E=145
    x1=50
    y1=170 
    z1=180 
    y2=1820 
    z2=1845 
    CL=[y1,y2]
    DL=[z1,z2]
    r=len(R)
    Av = average(R)

    for k in range(r):
        entreescores14(R[k],C,E,x1,CL,DL,k+1,Rang[k],Av[k],Titre[k],Musique[k], output_path)
    return()


def creationimages18(R,C,Rang,Total,Titre,Musique,output_path):
    E=122 
    x1=20
    y1=170 
    z1=180
    y2=1810 
    z2=1835 
    CL=[y1,y2]
    DL=[z1,z2]
    r=len(R)
    Av = average(R)

    for k in range(r):
        entreescores18(R[k],C,E,x1,CL,DL,k+1,Rang[k],Av[k],Titre[k],Musique[k], output_path)
    return()

def creationimages36(R,C,E,x1,CL,DL,Rang,Total,Titre,Musique, output_path):
    E=120 #Ecart suivant l'axe y pour les scores
    x1=83#Abscisse initiale 83
    y1=5 #Ordonnée colonne 1 5
    z1=8 #15
    y2=135 #Ordonnée colonne 2
    z2=139 #142
    y3=1660
    z3= 1660  #1670 
    y4=1790
    z4= 1794   #1797
    CL=[y1,y2,y3,y4]
    DL=[z1,z2,z3,z4]
    r=len(R)
    Av = average(R)
    
    for k in range(r):
        entreescores36(R[k],C,E,x1,CL,DL,k+1,Rang[k],Av[k],Titre[k],Musique[k], output_path)
    return()

def creationimages54(R,C,Rang,Total,Titre,Musique,output_path):
    E=120
    x1=83
    y1=5 
    z1=15
    y2=135 
    z2=142
    y3=265
    z3=275
    y4=1530
    z4=1540
    y5=1660
    z5=1670
    y6=1790
    z6=1797 
    CL=[y1,y2,y3,y4,y5,y6]
    DL=[z1,z2,z3,z4,z5,z6]
    r=len(R)
    Av = average(R)

    for k in range(r):
        entreescores54(R[k],C,E,x1,CL,DL,k+1,Rang[k],Av[k],Titre[k],Musique[k], output_path)
    return()

