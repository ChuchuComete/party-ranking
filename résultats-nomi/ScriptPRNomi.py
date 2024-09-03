import PIL
from PIL import Image, ImageDraw, ImageFont,ImageEnhance, ImageFilter,ImageOps
import os
import numpy as np
import configparser

VERSION = "1.0"
print(f"ScriptPRNomi.py version {VERSION}")

config = configparser.ConfigParser()
config.read('../config.txt')
pr_path = config["general"]["pr_path"]

#Données (Ce qu'il y a à modifier):

Chemin = f'{pr_path}/Images'
os.chdir(Chemin)

Bro=PIL.Image.open('Bronze2.png')
Arg=PIL.Image.open('Argent2.png')
Or=PIL.Image.open('Or2.png')

LayoutPR =  f"{pr_path}/résultats-nomi/LayoutPR.png"

#Polices

Mustica = 'MusticaPro-SemiBold 600.otf'
Comfortaa = 'Comfortaa-Regular.ttf'
njnaruto = 'njnaruto.ttf'
arlrdbd = 'arlrdbd.ttf'

def entreescores8(L,C,E,x1,CL,DL,k,Rang,Total,Nomi,Titre,Musique, Picker, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Mustica, size=60) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    fontpick = ImageFont.truetype(arlrdbd, size = 40)
    L2=L.copy()
    L2.remove(L2[Nomi-1])
    m=min(L2)
    M=max(L2)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if Nomi != False:
                if Inc+j==Nomi-1:
                    if L[Inc+j]<10:
                        draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-240,X-60),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-240,X-60),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-240,X-60),Bro)
                    else:
                        draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                else:
                    if L[Inc+j]<10:
                        if L[Inc+j] == m:
                            draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-240,X-60),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-240,X-60),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-240,X-60),Bro)
                    else:
                        if L[Inc+j] == m:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)

            else:
                if L[Inc+j]<10:
                    if L[Inc+j] == m:
                        draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Y+25,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                    if L[Inc+j]==1:
                        img.paste(Or,(Z-240,X-60),Or) #80
                    elif L[Inc+j]==2:
                        img.paste(Arg,(Z-240,X-60),Arg)
                    elif L[Inc+j]==3:
                        img.paste(Bro,(Z-240,X-60),Bro)
                else:
                    if L[Inc+j] == m:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((378,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2) 
    if Total<10:
        draw.text((1459,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2) 
    elif Total<100:
        draw.text((1444,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((1427,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)


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

    draw.text((420,942), Picker, fill = 'rgb(255, 255, 255)', font=fontpick)

    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()

def entreescores14(L,C,E,x1,CL,DL,k,Rang,Total,Nomi,Titre,Musique, Picker, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Mustica, size=60) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    fontpick = ImageFont.truetype(arlrdbd, size = 40)
    L2=L.copy()
    L2.remove(L2[Nomi-1])
    m=min(L2)
    M=max(L2)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if Nomi != False:
                if Inc+j==Nomi-1:
                    if L[Inc+j]<10:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-190,X-25),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-190,X-25),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-190,X-25),Bro)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                else:
                    if L[Inc+j]<10:
                        if L[Inc+j] == m:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-190,X-25),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-190,X-25),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-190,X-25),Bro)
                    else:
                        if L[Inc+j] == m:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)

            else:
                if L[Inc+j]<10:
                    if L[Inc+j] == m:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                    if L[Inc+j]==1:
                        img.paste(Or,(Z-190,X-25),Or) #80
                    elif L[Inc+j]==2:
                        img.paste(Arg,(Z-190,X-25),Arg)
                    elif L[Inc+j]==3:
                        img.paste(Bro,(Z-190,X-25),Bro)
                else:
                    if L[Inc+j] == m:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((378,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    if Total<10:
        draw.text((1459,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)
    elif Total<100:
        draw.text((1444,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((1427,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)

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

    draw.text((420,942), Picker, fill = 'rgb(255, 255, 255)', font=fontpick)

    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()

def entreescores18(L,C,E,x1,CL,DL,k,Rang,Total,Nomi,Titre,Musique, Picker, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(Mustica, size=60) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    fontpick = ImageFont.truetype(arlrdbd, size = 40)
    L2=L.copy()
    L2.remove(L2[Nomi-1])
    m=min(L2)
    M=max(L2)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if Nomi != False:
                if Inc+j==Nomi-1:
                    if L[Inc+j]<10:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-190,X-25),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-190,X-25),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-190,X-25),Bro)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                else:
                    if L[Inc+j]<10:
                        if L[Inc+j] == m:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-190,X-25),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-190,X-25),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-190,X-25),Bro)
                    else:
                        if L[Inc+j] == m:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)

            else:
                if L[Inc+j]<10:
                    if L[Inc+j] == m:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                    if L[Inc+j]==1:
                        img.paste(Or,(Z-190,X-25),Or) #80
                    elif L[Inc+j]==2:
                        img.paste(Arg,(Z-190,X-25),Arg)
                    elif L[Inc+j]==3:
                        img.paste(Bro,(Z-190,X-25),Bro)
                else:
                    if L[Inc+j] == m:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((378,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2) #draw.text((372,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    if Total<100:
        draw.text((1434,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2) #draw.text((1444,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((1427,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)
        
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
        w2 = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)

    draw.text((420,942), Picker, fill = 'rgb(255, 255, 255)', font=fontpick)

    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()


    
def entreescores36(L,C,E,x1,CL,DL,k,Rang,Total,Nomi,Titre,Musique, Picker, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(njnaruto, size=28) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    fontpick = ImageFont.truetype(arlrdbd, size = 40)
    L2=L.copy()
    L2.remove(L2[Nomi-1])
    m=min(L2)
    M=max(L2)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if Nomi != False:
                if Inc+j==Nomi-1:
                    if L[Inc+j]<10:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-22,X-80),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-22,X-80),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-22,X-80),Bro)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                else:
                    if L[Inc+j]<10:
                        if L[Inc+j] == m:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-22,X-80),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-22,X-80),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-22,X-80),Bro)
                    else:
                        if L[Inc+j] == m:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)

            else:
                if L[Inc+j]<10:
                    if L[Inc+j] == m:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                    if L[Inc+j]==1:
                        img.paste(Or,(Z-22,X-80),Or) #80
                    elif L[Inc+j]==2:
                        img.paste(Arg,(Z-22,X-80),Arg)
                    elif L[Inc+j]==3:
                        img.paste(Bro,(Z-22,X-80),Bro)
                else:
                    if L[Inc+j] == m:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
    if Rang <10:
        draw.text((395,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((372,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    if Total<100:
        draw.text((1444,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((1427,850), str(Total),fill = 'rgb(255, 255, 255)', font=font2)


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
        w2 = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)


    draw.text((420,942), Picker, fill = 'rgb(255, 255, 255)', font=fontpick)
    
    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()



def entreescores54(L,C,E,x1,CL,DL,k,Rang,Total,Nomi,Titre,Musique, Picker, output_path):
    c=len(C)
    N=len(L)
    img = PIL.Image.open(LayoutPR)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(njnaruto, size=28) 
    font2= ImageFont.truetype(Mustica, size=65)
    font3= ImageFont.truetype(Comfortaa, size=45)
    font4= ImageFont.truetype(Comfortaa, size=35)
    font5= ImageFont.truetype(Comfortaa, size=23)
    fontpick = ImageFont.truetype(arlrdbd, size = 40)
    L2=L.copy()
    L2.remove(L2[Nomi-1])
    m=min(L2)
    M=max(L2)
    Inc=0
    for i in range(c):
        Y=CL[i]
        Z=DL[i]
        for j in range(C[i]):
            X=x1+j*E
            if Nomi != False:
                if Inc+j==Nomi-1:
                    if L[Inc+j]<10:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-22,X-80),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-22,X-80),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-22,X-80),Bro)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 255)', font=font)
                else:
                    if L[Inc+j]<10:
                        if L[Inc+j] == m:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                        if L[Inc+j]==1:
                            img.paste(Or,(Z-22,X-80),Or)
                        elif L[Inc+j]==2:
                            img.paste(Arg,(Z-22,X-80),Arg)
                        elif L[Inc+j]==3:
                            img.paste(Bro,(Z-22,X-80),Bro)
                    else:
                        if L[Inc+j] == m:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                        elif L[Inc+j] == M:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                        else:
                            draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)

            else:
                if L[Inc+j]<10:
                    if L[Inc+j] == m:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Z,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
                    if L[Inc+j]==1:
                        img.paste(Or,(Z-22,X-80),Or) #80
                    elif L[Inc+j]==2:
                        img.paste(Arg,(Z-22,X-80),Arg)
                    elif L[Inc+j]==3:
                        img.paste(Bro,(Z-22,X-80),Bro)
                else:
                    if L[Inc+j] == m:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(0, 255, 0)', font=font)
                    elif L[Inc+j] == M:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 0, 0)', font=font)
                    else:
                        draw.text((Y,X), str(L[Inc+j]),fill = 'rgb(255, 255, 255)', font=font)
        Inc=Inc+C[i]
  

    if Rang <10:
        draw.text((550,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((522,170), str(Rang),fill = 'rgb(255, 255, 255)', font=font2)
    if Total<100:
        draw.text((1314,830), str(Total),fill = 'rgb(255, 255, 255)', font=font2)
    else:
        draw.text((1307,830), str(Total),fill = 'rgb(255, 255, 255)', font=font2)

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
        w2 = draw.textlength(Musique,font=font5)
        draw.text(((W2-w2)/2,H2c), Musique, fill = 'rgb(255, 255, 255)', font=font5)
        
    draw.text((535,962), Picker, fill = 'rgb(255, 255, 255)', font=fontpick)

    test="a" + str(k) + ".png"
    os.chdir(output_path)
    img.save(test)
    os.chdir(Chemin)
    return()

def verif_picker(dico):
    liste = []
    for elem in dico:
        if dico[elem] == False:
            liste.append(elem)
    print(f"❌ Utilisateurs qui posent problème : {', '.join(map(str, liste))}")
    

def creationimages8(R,C,Rang,Total,Titre,Musique, Picker, output_path, order):
    E=240 
    x1=130 
    y1=170
    z1=380
    y2=1825
    z2=2045
    CL=[y1,y2]
    DL=[z1,z2]
    r=len(R)


    Picker_Liste = Picker.copy()
    Picker.sort()
    
    dico = {}
    for i in range(len(order)):
        dico[order[i]] = i+1

    for i in range(len(Picker)):
        if Picker[i] not in order:
            dico[Picker[i]] = False
            
    Nomi = []
    for i in range(len(Picker_Liste)):
        Nomi.append(dico[Picker_Liste[i]])

    print(verif_picker(dico))

    for k in range(r):
        entreescores8(R[k],C,E,x1,CL,DL,k+1,Rang[k],Total[k],Nomi[k],Titre[k],Musique[k], Picker_Liste[k], output_path)
    return()


def creationimages14(R,C,Rang,Total,Titre,Musique, Picker, output_path, order):
    r=len(R)
    E=145
    x1=50
    y1=170 
    z1=180 
    y2=1820 
    z2=1845 
    CL=[y1,y2]
    DL=[z1,z2]


    Picker_Liste = Picker.copy()
    Picker.sort()

    dico = {}
    for i in range(len(order)):
        dico[order[i]] = i+1

    for i in range(len(Picker)):
        if Picker[i] not in order:
            dico[Picker[i]] = False

        
    Nomi = []
    for i in range(len(Picker_Liste)):
        Nomi.append(dico[Picker_Liste[i]])

    verif_picker(dico)

    for k in range(r):
        entreescores14(R[k],C,E,x1,CL,DL,k+1,Rang[k],Total[k],Nomi[k],Titre[k],Musique[k], Picker_Liste[k], output_path)
    return()

def creationimages18(R,C,Rang,Total,Titre,Musique, Picker, output_path, order):
    r=len(R)
    E=122 #Ecart suivant l'axe y
    x1=20 #Abscisse initiale 
    y1=170 
    z1=180
    y2=1810 
    z2=1835 
    CL=[y1,y2]
    DL=[z1,z2]

    Picker_Liste = Picker.copy()
    Picker.sort()

    dico = {}
    for i in range(len(order)):
        dico[order[i]] = i+1

    for i in range(len(Picker)):
        if Picker[i] not in order:
            dico[Picker[i]] = False

        
    Nomi = []
    for i in range(len(Picker_Liste)):
        Nomi.append(dico[Picker_Liste[i]])

    verif_picker(dico)

    for k in range(r):
        entreescores18(R[k],C,E,x1,CL,DL,k+1,Rang[k],Total[k],Nomi[k],Titre[k],Musique[k], Picker_Liste[k], output_path)
    return()


def creationimages36(R,C,Rang,Total,Titre,Musique, Picker, output_path, order):
    r=len(R)
    E=120 #Ecart suivant l'axe y pour les scores
    x1=83#Abscisse initiale 83
    y1=5 #Ordonnée colonne 1
    z1=15
    y2=135 #Ordonnée colonne 2
    z2=142
    y3=1660
    z3=1670
    y4=1790
    z4=1797
    CL=[y1,y2,y3,y4]
    DL=[z1,z2,z3,z4]

    Picker_Liste = Picker.copy()
    Picker.sort()

    dico = {}
    for i in range(len(order)):
        dico[order[i]] = i+1

    for i in range(len(Picker)):
        if Picker[i] not in order:
            dico[Picker[i]] = False
            
        
    Nomi = []
    for i in range(len(Picker_Liste)):
        Nomi.append(dico[Picker_Liste[i]])

    verif_picker(dico)

    for k in range(r):
        entreescores36(R[k],C,E,x1,CL,DL,k+1,Rang[k],Total[k],Nomi[k],Titre[k],Musique[k], Picker_Liste[k], output_path)
    return()

def creationimages54(R,C,Rang,Total,Titre,Musique, Picker, output_path, order):
    r=len(R)
    E=120 #Ecart suivant l'axe y pour les scores
    x1=83#Abscisse initiale 83
    y1=5 #Ordonnée colonne 1
    z1=15
    y2=135 #Ordonnée colonne 2
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

    Picker_Liste = Picker.copy()
    Picker.sort()

    dico = {}
    for i in range(len(order)):
        dico[order[i]] = i+1

    for i in range(len(Picker)):
        if Picker[i] not in order:
            dico[Picker[i]] = False
            
        
    Nomi = []
    for i in range(len(Picker_Liste)):
        Nomi.append(dico[Picker_Liste[i]])

    verif_picker(dico)

    for k in range(r):
        entreescores54(R[k],C,E,x1,CL,DL,k+1,Rang[k],Total[k],Nomi[k],Titre[k],Musique[k], Picker_Liste[k], output_path)
    return()
