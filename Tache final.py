from tkinter import*
fenetre=Tk()
fenetre.title('Hascoet Émilie Bilan Conversion')
fenetre.config(width=450,height=520, bg='#c7f9bd')

Entree=Entry()
Entree.place(x=165,y=60)

Entree2=Entry()
Entree2.place(x=165,y=100)

Entree3=Entry()
Entree3.place(x=165,y=140)


Texte0=Label(text="Conversion Décimal-Binaire-Hexadécimal",fg='purple',bg='#c7f9bd',font=('verdana',12))
Texte0.place(x=50,y=10)


Texte=Label(text="Décimal",bg='#c7f9bd')
Texte.place(x=80,y=60)

Texte2=Label(text="Binaire",bg='#c7f9bd')
Texte2.place(x=82,y=100)

Texte3=Label(text="Hexadécimal",bg='#c7f9bd')
Texte3.place(x=70,y=140)

def Erreur():
    fen2=Tk()
    fen2.title('Compatibility error')
    fen2.config(width=300,height=85, bg='#cfbdf9')

    text=Label(fen2, text='Attention!',fg='red',bg='#cfbdf9', font=('bold',(12)))
    text.place(x=107,y=0)
    text2=Label(fen2, text="Le nombre entré n'est pas écrit à la bonne base",bg='#cfbdf9', font=('arial',(10)))
    text2.place(x=7,y=26)

    def Compris():
        fen2.destroy()

    Ok=Button(fen2, text='Compris',bg='#bde7f9', command=Compris)
    Ok.place(x=116,y=54)
    fen2.mainloop()

def Erreur2():
    fen3=Tk()
    fen3.title('Compatibility error')
    fen3.config(width=340,height=85, bg='#cfbdf9')

    text3=Label(fen3, text='Attention!',fg='red',bg='#cfbdf9', font=('bold',(12)))
    text3.place(x=127,y=0)
    text4=Label(fen3, text="Les nombres entrés doivent être compris entre 0 et 255",bg='#cfbdf9', font=('arial',(10)))
    text4.place(x=7,y=26)

    def Ok():
        fen3.destroy()

    Ok2=Button(fen3, text='Compris',bg='#bde7f9', command=Ok)
    Ok2.place(x=131,y=54)
    fen3.mainloop()

def Decimal():

    dec=str(Entree.get())
    resultat=''

    for lettre in dec:
        n2=ord(lettre)

        if n2<=47 or n2>=58:
            Erreur()

    n1=int(Entree.get())
    while n1 !=0 :
        reste=n1%2
        n1=n1//2
        resultat=str(reste)+resultat

    Entree2.delete(0,END)
    Entree2.insert(0,resultat)


    n2=int(Entree.get())
    resultat=''

    while n2 !=0 :
        reste=n2%16
        n2=n2//16
        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    Entree3.delete(0,END)
    Entree3.insert(0,resultat)


Bouton=Button(text='valider',bg='#f9efbd', command=Decimal)
Bouton.place(x=320,y=58)


def Binaire():

    bin=str(Entree2.get())

    for lettre in bin:
        n2=ord(lettre)
        if n2>=50 or n2<=47:
            Erreur()

    n1=int(Entree2.get())

    valeur=0
    puissance=1

    while n1!=0 :
        if n1%10==1:
            valeur=valeur+puissance
        puissance=puissance*2
        n1=n1//10

    Entree.delete(0,END)
    Entree.insert(0,valeur)

    resultat=''

    while valeur !=0 :
        reste=valeur%16
        valeur=valeur//16

        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    Entree3.delete(0,END)
    Entree3.insert(0,resultat)


Bouton2=Button(text='valider',bg='#f9efbd', command=Binaire)
Bouton2.place(x=320,y=98)


def Hexadecimal():

    nombre=str(Entree3.get().upper())

    for lettre in nombre:
        n2=ord(lettre)

        if n2<=47 or 58<=n2<=64 or n2>=71:
            Erreur()

    decimal=0
    puissance=16** (len(nombre)-1)

    for chiffre in nombre :
        if chiffre == 'A':
            decimal = decimal + 10*puissance
        elif chiffre == 'B':
            decimal = decimal + 11*puissance
        elif chiffre == 'C':
            decimal = decimal + 12*puissance
        elif chiffre == 'D':
            decimal = decimal + 13*puissance
        elif chiffre == 'E':
            decimal = decimal + 14*puissance
        elif chiffre == 'F':
            decimal = decimal + 15*puissance
        else :
            decimal = decimal + int(chiffre)*puissance
        puissance=puissance//16

    Entree.delete(0,END)
    Entree.insert(0,decimal)

    resultat=''

    while decimal !=0 :
        reste=decimal%2
        decimal=decimal//2
        resultat=str(reste)+resultat

    Entree2.delete(0,END)
    Entree2.insert(0,resultat)

Bouton3=Button(text='valider',bg='#f9efbd', command=Hexadecimal)
Bouton3.place(x=320,y=138)



Texte4=Label(text='Couleur, RGB <--> Hexadecimal',fg='purple',bg='#c7f9bd',font=('verdana',12))
Texte4.place(x=80,y=200)

Texte5=Label(text='Rouge',fg='red',bg='#c7f9bd',font=('bold'))
Texte5.place(x=90,y=240)

Texte5=Label(text='Green',fg='green',bg='#c7f9bd',font=('bold'))
Texte5.place(x=190,y=240)

Texte5=Label(text='Blue',fg='blue',bg='#c7f9bd',font=('bold'))
Texte5.place(x=290,y=240)

Entree4=Entry(width=3, fg='red', font=('bold',10))
Entree4.place(x=104,y=322)

Entree5=Entry(width=3, fg='green', font=('bold',10))
Entree5.place(x=204,y=322)

Entree6=Entry(width=3, fg='blue', font=('bold',10))
Entree6.place(x=297,y=322)

def PlusRouge():
    n1=int(Entree4.get())

    if n1>=255:
        resultat=0
    else:
        resultat=n1+1

    Entree4.delete(0,END)
    Entree4.insert(0,resultat)

Bouton4=Button(text='+', fg='red', width=1, font=('bold'), command=PlusRouge)
Bouton4.place(x=107,y=280)

def MoinsRouge():
    n1=int(Entree4.get())

    if n1>255:
        resultat=0
    elif n1==0:
        resultat=255
    else:
        resultat=n1-1

    Entree4.delete(0,END)
    Entree4.insert(0,resultat)

Bouton4bis=Button(text='-', fg='red', font=('bold'), command=MoinsRouge)
Bouton4bis.place(x=107,y=350)

def PlusVert():
    n1=int(Entree5.get())

    if n1>=255:
        resultat=0
    else:
        resultat=n1+1

    Entree5.delete(0,END)
    Entree5.insert(0,resultat)

Bouton5=Button(text='+', fg='green', width=1, font=('bold'), command=PlusVert)
Bouton5.place(x=207,y=280)

def MoinsVert():
    n1=int(Entree5.get())

    if n1>255:
        resultat=0
    elif n1==0:
        resultat=255
    else:
        resultat=n1-1

    Entree5.delete(0,END)
    Entree5.insert(0,resultat)

Bouton5bis=Button(text='-', fg='green', font=('bold'), command=MoinsVert)
Bouton5bis.place(x=207,y=350)

def PlusBleue():
    n1=int(Entree6.get())

    if n1>=255:
        resultat=0
    else:
        resultat=n1+1

    Entree6.delete(0,END)
    Entree6.insert(0,resultat)

Bouton6=Button(text='+', fg='blue', width=1, font=('bold'), command=PlusBleue)
Bouton6.place(x=300,y=280)

def MoinsBleue():
    n1=int(Entree6.get())

    if n1>255:
        resultat=0
    elif n1==0:
        resultat=255
    else:
        resultat=n1-1

    Entree6.delete(0,END)
    Entree6.insert(0,resultat)

Bouton6bis=Button(text='-', fg='blue', font=('bold'), command=MoinsBleue)
Bouton6bis.place(x=300,y=350)

Entree7=Entry(width=7, font=('bold',20))
Entree7.place(x=160,y=400)

def RGB():
    n1=int(Entree4.get())
    n2=int(Entree5.get())
    n3=int(Entree6.get())

    if n1>255 or n2>255 or n3>255:
        Erreur2()

    r=255-n1
    g=255-n2
    b=255-n3

    resultat=''

    while n1 !=0 :
        reste=n1%16
        n1=n1//16

        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    if len(resultat)==0:
        resultat='00'
    if len(resultat)==1:
        resultat="0"+resultat

    n1=resultat

    resultat=''

    while n2 !=0 :
        reste=n2%16
        n2=n2//16

        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    if len(resultat)==0:
        resultat='00'
    if len(resultat)==1:
        resultat="0"+resultat

    n2=resultat

    resultat=''

    while n3 !=0 :
        reste=n3%16
        n3=n3//16

        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    if len(resultat)==0:
        resultat='00'
    if len(resultat)==1:
        resultat="0"+resultat

    n3=resultat

    resultat=''

    while r !=0 :
        reste=r%16
        r=r//16

        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    if len(resultat)==0:
        resultat='00'
    if len(resultat)==1:
        resultat="0"+resultat

    r=resultat

    resultat=''

    while g !=0 :
        reste=g%16
        g=g//16

        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    if len(resultat)==0:
        resultat='00'
    if len(resultat)==1:
        resultat="0"+resultat

    g=resultat

    resultat=''

    while b !=0 :
        reste=b%16
        b=b//16

        if reste<10:
            resultat=str(reste)+resultat
        if reste==10:
            resultat="A"+resultat
        if reste==11:
            resultat="B"+resultat
        if reste==12:
            resultat="C"+resultat
        if reste==13:
            resultat="D"+resultat
        if reste==14:
            resultat="E"+resultat
        if reste==15:
            resultat="F"+resultat

    if len(resultat)==0:
        resultat='00'
    if len(resultat)==1:
        resultat="0"+resultat

    b=resultat


    codehexa=str(n1+n2+n3)
    compl=str(r+g+b)

    Entree7.delete(0,END)
    Entree7.insert(0,codehexa)
    Entree7.configure(fg='#'+codehexa, bg='#'+compl)

Bouton7=Button(text='valider',bg='#f9efbd', command=RGB)
Bouton7.place(x=350,y=320)

def CodeHexa():
    n1=str(Entree7.get())
    if len(n1)!=6:
        Erreur()

    n2=reversed(str(n1[0]) +str(n1[1]))
    resultat=''

    for lettre in n2:

        n1=ord(lettre)

        if 65<=n1<=70:
            n1=n1-55

        elif 48<=n1<=57:
            n1=n1-48

        elif 97<=n1<=102:
            n1=n1-87
        else:
            Erreur()

        while n1 !=0 :
            reste=n1%2
            n1=n1//2
            resultat=str(reste)+resultat

        if len(resultat)==0:
            resultat='0000'
        if len(resultat)==1:
            resultat='000'+resultat
        if len(resultat)==2:
            resultat='00'+resultat
        if len(resultat)==3:
            resultat='0'+resultat

    resultat=int(resultat)
    valeur1=0
    puissance=1

    while resultat!=0 :
        if resultat%10==1:
            valeur1=valeur1+puissance
        puissance=puissance*2
        resultat=resultat//10

    Entree4.delete(0,END)
    Entree4.insert(0,valeur1)


    n1=str(Entree7.get())
    n2=reversed(str(n1[2]) +str(n1[3]))

    resultat=''

    for lettre in n2:

        n1=ord(lettre)

        if 65<=n1<=70:
            n1=n1-55

        elif 48<=n1<=57:
            n1=n1-48

        elif 97<=n1<=102:
            n1=n1-87
        else:
            Erreur()

        while n1 !=0 :
            reste=n1%2
            n1=n1//2
            resultat=str(reste)+resultat

        if len(resultat)==0:
            resultat='0000'
        if len(resultat)==1:
            resultat='000'+resultat
        if len(resultat)==2:
            resultat='00'+resultat
        if len(resultat)==3:
            resultat='0'+resultat

    resultat=int(resultat)
    valeur2=0
    puissance=1

    while resultat!=0 :
        if resultat%10==1:
            valeur2=valeur2+puissance
        puissance=puissance*2
        resultat=resultat//10

    Entree5.delete(0,END)
    Entree5.insert(0,valeur2)

    n1=str(Entree7.get())
    n2=reversed((n1[4]) +str(n1[5]))

    resultat=''

    for lettre in n2:

        n1=ord(lettre)

        if 65<=n1<=70:
            n1=n1-55

        elif 48<=n1<=57:
            n1=n1-48

        elif 97<=n1<=102:
            n1=n1-87
        else:
            Erreur()

        while n1 !=0 :
            reste=n1%2
            n1=n1//2
            resultat=str(reste)+resultat

        if len(resultat)==0:
            resultat='0000'
        if len(resultat)==1:
            resultat=str('000')+resultat
        if len(resultat)==2:
            resultat=str('00')+resultat
        if len(resultat)==3:
            resultat=str('0')+resultat

    resultat=int(resultat)
    valeur3=0
    puissance=1

    while resultat!=0 :
        if resultat%10==1:
            valeur3=valeur3+puissance
        puissance=puissance*2
        resultat=resultat//10

    Entree6.delete(0,END)
    Entree6.insert(0,valeur3)

    RGB()

Bouton8=Button(text='valider le code hexadécimal',bg='#f9efbd', command=CodeHexa)
Bouton8.place(x=135,y=455)

fenetre.mainloop()